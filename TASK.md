# Cece audiology job search — task instructions

You are running an automated job search for Cece, an audiologist. This document is fully self-contained — do not assume any context from prior sessions.

All paths below are relative to `/mnt/cece-job-search/` (the folder this file lives in) unless otherwise noted.

## Candidate profile

- Cece has an AuD from a top-10 audiology program.
- ~2–3 years post-degree, with experience at multiple VA medical centers and research fellowships. No PhD.
- She is exploring a transition AWAY from direct patient care. Her priorities, in order:
  1. Non-clinical roles: research, teaching (university), administration, public-school practice leadership.
  2. Hybrid clinical + research, or clinical-admin (e.g., lead audiologist with admin responsibilities).
  3. Adjacent roles that leverage her AuD + VA + research background (see "Adjacent roles" section below).
  4. Pure clinical in Tier 1 locations (always surface these — she might still consider them if the role is good).
  5. Pure clinical in Tier 2 only if exceptional.
- Non-profit / government strongly preferred (VA, federal, academic medical centers, public schools, large non-profits) — enables PSLF loan forgiveness.
- Industry considered (Cochlear, Starkey, Phonak, Oticon, Advanced Bionics, ReSound, GN, Sonova, WS Audiology, Natus, Demant, research arms of these companies).
- No salary filter.

## HARD LOCATION FILTER

A job MUST be in one of these locations OR fully remote. Reject all others regardless of fit:

- **Tier 1 (wide search, be liberal about inclusion — this includes pure clinical roles):** NYC metro (incl. northern NJ, Long Island), SF Bay Area (incl. Oakland, Berkeley, Palo Alto, Stanford), San Diego, Boston metro (incl. Cambridge), Fully Remote.
- **Tier 2 (selective — do NOT include generic non-VA pure-clinical positions here):** Seattle, Chicago, Portland OR, Philadelphia, Washington DC metro (incl. Bethesda, Baltimore), Tucson, Pittsburgh.
- **Anywhere else:** REJECT. Do not include even if the role is exceptional.

## EXPERIENCE RANGE FILTER (use judgment — be flexible)

Cece has ~2–3 years post-AuD experience plus 4 years of AuD training. Many postings count degree/clinical-extern years toward "experience required," especially for non-clinical roles.

- **Include:** Roles requiring 0–4 years experience, roles that say "early-career", "new graduate", "1+ years", "AuD required", or don't specify.
- **Include with judgment (the gray zone):** Roles requiring up to 5 years. For non-clinical roles (research, teaching, admin, adjacent), AuD training years often count — include these and note the stated requirement clearly so she can make her own call. For pure clinical roles with a firm 5-year floor, still include for Tier 1 locations but mark the gap.
- **Include as a stretch with a clear note:** Roles requiring up to 6 years for truly rare/unique non-clinical fits (e.g., a specific research program that matches her fellowships).
- **EXCLUDE:** Roles firmly requiring 7+ years, or explicitly titled "Director / Chief / Service Chief / Principal" at large institutions, or PhD-required research roles.
- Judge by stated years-required, not title alone. A "Senior Audiologist" at a small program requiring 3–4 years is fine.

When including roles in the gray zone, always note the stated experience requirement in the notes column so Cece can make an informed call.

## EXCLUSIONS

- Pure sales / hearing-aid sales rep roles.
- PhD-required research roles (she has AuD, not PhD).
- Franchise hearing clinics (Miracle-Ear, HearingLife, Connect Hearing retail stores, etc.) unless the role is clearly non-clinical (corporate research, training, clinical ops).

## ADJACENT ROLES TO INCLUDE

Do not limit the search to roles with "audiologist" in the title. Cece's AuD + VA + research fellowship background transfers well to:

- **Clinical research coordinator / Clinical research associate** at audiology, ENT, or hearing-loss-related studies
- **Clinical trial manager / Clinical trials operations** (hearing devices, otology, vestibular, tinnitus, Ménière's, cochlear implants)
- **Clinical scientist / Medical affairs** at hearing device manufacturers
- **Implementation scientist / Implementation science coordinator** in hearing or communication disorders
- **Program manager / Program coordinator** for NIH-funded hearing studies, VA research programs, or university audiology programs
- **Clinical educator / Training specialist** at device manufacturers or academic programs
- **Regulatory affairs / Clinical affairs** at hearing device companies (entry-to-mid)
- **Rehabilitation research specialist** at VA RR&D or similar
- **Hearing loss advocacy / program leadership** at non-profits (HLAA, AG Bell, etc.)
- **Clinical data coordinator** on hearing / communication studies
- **Lecturer / Adjunct instructor / Clinical instructor** at AuD programs (often lower experience requirement than tenure-track)
- **Health services research coordinator** in otolaryngology/ENT departments

Flag these as "Adjacent role — AuD+VA+research background transfers."

## Files

Working directory: `/mnt/cece-job-search/`. Contents:

- `jobs.xlsx` — tracker with tabs: `Active`, `Closed`, `Log`.
- `jobs/` — one markdown file per job, named `{job_id}.md`.
- `reports/` — one dated markdown report per run, plus `latest.md` mirror.
- `README.md` — reference for schema and conventions.
- `send_report.py` — Python script that emails the latest report via SMTP.
- `.smtp_credentials` — credentials file for send_report.py. May not exist yet; if absent, skip email.
- `backup.sh` — commits and pushes changes to origin/main.
- `TASK.md` — this file.

Job IDs are `YYMMDD-NNN`. IDs are STABLE — never renumber existing jobs.

## Pipeline — execute in order

### Pass A: Direct board browsing (primary source)

Browse these with WebFetch, then parse listings:

1. **AAA HEARCareers:** https://hearcareers.audiology.org/jobs
2. **USAJobs:** https://www.usajobs.gov/Search/Results?soc=Audiologists — filter by NY, CA, MA, IL, PA, WA, OR, DC, AZ, remote/telework
3. **Chronicle of Higher Ed:** https://jobs.chronicle.com/jobs/speech-and-hearing-sciences/
4. **CAPCSD Job Board:** https://members.capcsd.org/jobboard
5. **ASHA Career Center:** https://careers.asha.org/jobs
6. **LinkedIn:** site:linkedin.com/jobs searches for audiologist + clinical research coordinator hearing, per metro
7. **Indeed:** targeted searches per metro and remote
8. **Device manufacturer careers pages** (rotate 2–3 per run): Cochlear Americas, Starkey, Phonak/Sonova, Oticon/Demant, Advanced Bionics, ReSound/GN, Natus
9. **Academic medical center careers pages** (rotate 2–3 per run): UCSF, Stanford, UCSD, Scripps, Rady Children's, Mass Eye and Ear, MGH, Brigham, Boston Children's, NYU Langone, Columbia, Mount Sinai, Weill Cornell, NYEE, UW, Seattle Children's, Penn Medicine, CHOP, Johns Hopkins, Children's National, Northwestern, U of Chicago, Rush, Lurie Children's, UPMC, OHSU, University of Arizona, Banner Health
10. **Public school districts** (target-metro only): NYC DOE, SFUSD, SDUSD, Boston Public Schools, Seattle Public Schools, Philadelphia, Chicago Public Schools, DC Public Schools

### Pass A2: Supplementary web search

Run 4–6 WebSearch queries. Vary each run. Seeds:

- `"clinical research coordinator" OR "clinical research associate" hearing OR audiology OR otology {metro}`
- `audiologist faculty OR lecturer OR "clinical instructor" {metro} 2026`
- `"clinical scientist" OR "medical affairs" audiology hearing devices remote 2026`
- `"implementation science" hearing OR audiology coordinator 2026`
- `"program manager" NIH hearing study 2026`
- `rehabilitation research audiology VA 2026`

### Pass A3: Dedupe and filter

For each candidate:

1. Apply HARD LOCATION FILTER. Not in target metro or remote → REJECT.
2. Apply EXPERIENCE RANGE FILTER (with the judgment flexibility described above).
3. Apply EXCLUSIONS.
4. Dedupe by Apply URL and by (Employer, Title) fuzzy match against Active and Closed. If in Closed with reason "location" or firm "seniority > 7 yrs," skip.

For each surviving NEW job:

- Assign next Job ID for today.
- Create `jobs/{id}.md`.
- Append row to `Active` tab. Status="New", Date Found=today, Last Checked=today.
- Priority:
  - **High:** Non-clinical (Research/Teaching/Admin) in Tier 1 or Remote, OR adjacent role in Tier 1/Remote that fits.
  - **Medium:** Non-clinical/adjacent in Tier 2; hybrid clinical+research in Tier 1/Remote; clinical-admin matching experience in Tier 1.
  - **Low:** Pure clinical in Tier 1 (surface these — she'll decide); Tier 2 clinical-admin.
- Research Flag "Y" if research/fellowship/trial/investigator/implementation science mentioned.
- If the role is in the experience gray zone (requires 4–6 years), add a note to the Notes column: "Stated req: {N} yrs — borderline for Cece's 2–3 post-AuD experience; AuD training years may count, worth inquiring."

### Pass B: Refresh existing jobs

1. For every Active row, WebFetch the Apply URL. Max 25 per run.
2. Gone/closed/filled → move to `Closed` tab with Date Closed=today and Reason.
3. Still live → Last Checked=today; update changed fields and append to status history in `jobs/{id}.md`.

### Pass C: Report

1. Create `reports/{YYYY-MM-DD}.md` and mirror to `reports/latest.md`:
   - Summary (X new, Y updated, Z closed, Total Active)
   - New High-Priority Jobs
   - New Medium-Priority Jobs
   - New Low-Priority Jobs
   - Adjacent roles subsection within each priority block
   - Updates to Existing Jobs
   - Closed / Removed
   - Queries and sources covered
   - At bottom: "Full tracker: jobs.xlsx"
2. Append Log row.
3. Save `jobs.xlsx`. Recalc: `python /mnt/.claude/skills/xlsx/scripts/recalc.py /mnt/cece-job-search/jobs.xlsx` and verify zero errors. (If that path doesn't exist in the current session, discover it with `find /sessions -path '*/skills/xlsx/scripts/recalc.py' 2>/dev/null | head -1`.)

### Pass D: Email via SMTP script

Run:

```
python /mnt/cece-job-search/send_report.py
```

If credentials file missing (exit 2), log "Email skipped: credentials not configured" and move on. Do NOT use any Gmail MCP connector — we chose SMTP to keep credentials scoped to this task.

If exit code 5 (auth failure), log prominently and do not retry — likely app password expired.

### Final step — back up to GitHub

After the email send step has completed successfully, run:

```
bash /mnt/cece-job-search/backup.sh "Scheduled run $(date -u +%Y-%m-%d)"
```

(Adjust the path if the folder is mounted elsewhere in this session — use `$PWD` if you're already in the folder.) The script commits any changes and pushes to origin/main. If it exits non-zero, include the error in your completion summary; do not retry.

## Recipients

Configured in `.smtp_credentials` (currently Ruben and Cece).

## Important rules

- **NEVER invent jobs.**
- **NEVER renumber existing Job IDs.**
- **RESPECT the hard location filter.**
- **Use judgment on experience.** The 2-3 yr vs 5 yr bar is softer for non-clinical roles where AuD training may count. When in doubt, include and note the gap rather than exclude silently.
- If a URL won't load after 2 retries, note it and move on.
- Keep reports under 2000 words. Lead with High priority.
- Use Arial font when editing xlsx. Preserve conditional formatting.
- Load xlsx with `openpyxl.load_workbook` (NOT `data_only=True`).
- End with: "Run complete: X new, Y updated, Z closed. Report: reports/{date}.md. Email: {sent | skipped | failed}"
