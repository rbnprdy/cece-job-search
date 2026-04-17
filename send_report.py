#!/usr/bin/env python3
"""
Send the latest job search report via Gmail SMTP.

Reads credentials from .smtp_credentials (simple key=value file).
Attaches jobs.xlsx and inlines the report markdown as both plain text and
basic HTML in the body.

Usage:
    python send_report.py [YYYY-MM-DD]

If no date is provided, uses reports/latest.md.
Exits 0 on success, nonzero on failure.
"""
from __future__ import annotations

import os
import sys
import ssl
import smtplib
from datetime import date
from email.message import EmailMessage
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent
CRED_PATH = WORKSPACE / ".smtp_credentials"
XLSX_PATH = WORKSPACE / "jobs.xlsx"
REPORTS_DIR = WORKSPACE / "reports"


def load_credentials() -> dict:
    if not CRED_PATH.exists():
        sys.stderr.write(
            f"[send_report] Credentials file not found at {CRED_PATH}. "
            "Skipping email. Create the file with smtp_user=, smtp_password=, and recipients= lines.\n"
        )
        sys.exit(2)
    creds = {}
    for line in CRED_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        creds[k.strip()] = v.strip()
    required = {"smtp_user", "smtp_password", "recipients"}
    missing = required - creds.keys()
    if missing:
        sys.stderr.write(f"[send_report] Missing required keys in credentials file: {missing}\n")
        sys.exit(2)
    return creds


def pick_report(arg: str | None) -> Path:
    if arg:
        p = REPORTS_DIR / f"{arg}.md"
        if p.exists():
            return p
        sys.stderr.write(f"[send_report] Report for date {arg} not found at {p}\n")
    latest = REPORTS_DIR / "latest.md"
    if latest.exists():
        return latest
    # Fall back to today's date
    today_path = REPORTS_DIR / f"{date.today().isoformat()}.md"
    if today_path.exists():
        return today_path
    sys.stderr.write(f"[send_report] No report found to send.\n")
    sys.exit(3)


def markdown_to_html(md: str) -> str:
    """Very lightweight md-to-html. We don't need anything fancy for inline email bodies."""
    try:
        import markdown  # type: ignore

        return markdown.markdown(md, extensions=["extra", "sane_lists"])
    except ImportError:
        # Fall back: wrap in <pre> to preserve formatting without any rendering
        escaped = (
            md.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        return f"<pre style='font-family: -apple-system, Arial, sans-serif; white-space: pre-wrap;'>{escaped}</pre>"


def build_subject(md: str) -> str:
    """Extract counts from the report for a concise subject line."""
    today = date.today().strftime("%m/%d")
    new_count = "?"
    updated_count = "?"
    for line in md.splitlines():
        line = line.strip()
        if line.startswith("- **") and "new**" in line:
            # e.g. "- **8 new** jobs added"
            try:
                new_count = line.split("**")[1].split()[0]
            except Exception:
                pass
        if "updated" in line.lower() and line.startswith("-"):
            # e.g. "- **0** updates, ..."
            try:
                parts = line.split("**")
                for i, p in enumerate(parts):
                    if p and p[0].isdigit() and "updated" in " ".join(parts[i : i + 3]).lower():
                        updated_count = p.split()[0]
                        break
            except Exception:
                pass
    return f"Cece job search — {today}: {new_count} new, {updated_count} updates"


def main() -> int:
    creds = load_credentials()
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    report_path = pick_report(arg)
    md = report_path.read_text()

    recipients = [r.strip() for r in creds["recipients"].split(",") if r.strip()]
    if not recipients:
        sys.stderr.write("[send_report] No recipients configured.\n")
        return 4

    msg = EmailMessage()
    msg["From"] = creds["smtp_user"]
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = build_subject(md)
    msg.set_content(md)
    msg.add_alternative(markdown_to_html(md), subtype="html")

    # Attach xlsx
    if XLSX_PATH.exists():
        data = XLSX_PATH.read_bytes()
        msg.add_attachment(
            data,
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename="jobs.xlsx",
        )

    host = creds.get("smtp_host", "smtp.gmail.com")
    port = int(creds.get("smtp_port", "465"))

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(host, port, context=context, timeout=30) as server:
            server.login(creds["smtp_user"], creds["smtp_password"])
            server.send_message(msg)
    except smtplib.SMTPAuthenticationError as e:
        sys.stderr.write(
            f"[send_report] SMTP authentication failed. "
            f"Verify that 2FA is enabled on the bot account and the App Password is correct.\nError: {e}\n"
        )
        return 5
    except Exception as e:
        sys.stderr.write(f"[send_report] Send failed: {e}\n")
        return 6

    print(
        f"[send_report] Sent report ({report_path.name}) to {len(recipients)} recipient(s): "
        f"{', '.join(recipients)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
