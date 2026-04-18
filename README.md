# Cece's Job Search Tracker

Automated job search for Cece (AuD, ~2–3 yrs post-degree, multi-VA experience,
research fellowships). Scheduled runs via Claude Cowork. Emails reports out of
`cece.jobs.bot@gmail.com`.

## How it's organized

The per-job markdown files in `jobs/` are the single source of truth. Each file
has a YAML frontmatter block with structured fields and a free-form markdown
body. `jobs.xlsx` and `jobs/README.md` are **regenerated** from those files on
every run; don't edit them by hand.

- `jobs/{job_id}.md` — every job, active or closed. Files stay here forever.
  Active vs Closed is determined by the `status` field in frontmatter, not by
  directory. To close a job, edit frontmatter in place (set `status: Closed`,
  add `date_closed` and `closure_reason`) — do not move or delete the file.
- `jobs/closed/{job_id}.md` — **legacy** directory. Pre-existing closed files
  here are still read by the regenerator, but new closures go in place in
  `jobs/`. Avoiding file moves/deletes is required because the scheduled
  runner is unattended and Cowork prompts for user confirmation on deletes.
- `jobs/README.md` — auto-generated index table with clickable links to each
  job's md file (Job ID, Title, and File columns are all links).
- `runs.yml` — append-only list of runs, one entry per run; drives the Log tab
- `jobs.xlsx` — generated tracker with tabs `Active`, `Closed`, `Log`
- `regenerate_tracker.py` — rebuilds `jobs.xlsx` and `jobs/README.md` from the
  md files + runs.yml
- `reports/` — one dated markdown report per run, plus a copy emailed out
- `send_report.py` / `.smtp_credentials` / `backup.sh` — delivery plumbing

## Cece's priorities (in order)

1. **Non-clinical transitions** — research, teaching (university),
   administration, public-school practice leadership. She's getting tired of
   direct patient care and wants more control over her practice.
2. **Hybrid clinical + research** — roles that combine clinic with research or
   admin responsibilities.
3. **Adjacent roles that leverage her AuD + VA + research background** —
   clinical research coordinator/associate, clinical trial manager, clinical
   scientist / medical affairs, implementation scientist, program manager on
   NIH/VA hearing studies, clinical educator, regulatory/clinical affairs at
   device cos, health services research coordinator, etc.
4. **Pure clinical in Tier 1 locations** — always surface, she'll decide if
   the role is appealing.
5. **Pure clinical in Tier 2** — only if exceptional.

## Location filter (HARD — no exceptions)

A job must be in one of these metros OR fully remote. Anything else is rejected.

- **Tier 1 (wide search, liberal inclusion):** NYC metro, SF Bay Area (incl.
  Stanford/Palo Alto), San Diego, Boston metro (incl. Cambridge), Fully Remote
- **Tier 2 (selective — skip generic non-VA clinical):** Seattle, Chicago,
  Portland OR, Philadelphia, DC metro, Tucson, Pittsburgh

## Experience filter (use judgment — be flexible)

Cece has ~2–3 years post-AuD plus 4 years of AuD training. Many postings count
degree/clinical-extern years toward "experience," especially for non-clinical
roles.

- **Include:** 0–4 years required, "AuD required" with no year floor, or
  unspecified.
- **Include with judgment:** up to 5 years — AuD training years often count
  (especially for non-clinical). Gap noted in the `notes:` field.
- **Include as a stretch (with note):** up to 6 years for rare non-clinical
  fits that match her fellowship experience.
- **Exclude:** 7+ years firmly required, "Director / Chief / Service Chief" at
  large institutions, or PhD-required research positions.

## Employer preference

- Non-profit / government preferred (VA, federal, academic medical centers,
  public schools, large non-profit hospitals) — enables PSLF.
- Industry (Cochlear, Starkey, Phonak, Oticon, Advanced Bionics, etc.)
  considered.
- Pure sales roles excluded; franchise retail hearing clinics excluded unless
  role is explicitly non-clinical (corporate research/training/ops).

## Job ID scheme

Job IDs are `YYMMDD-NNN` based on the date the job was first seen, e.g.
`260417-003`. Stable across updates — if a listing gets reposted, it keeps its
original ID.

## Frontmatter schema

Each `jobs/**/*.md` file must begin with a YAML frontmatter block. Fields:

| Key | Required | Notes |
|---|---|---|
| `job_id` | yes | Stable identifier, matches filename stem |
| `status` | yes | `New` / `Active` / `Applied` / `Closed` / `Withdrawn` |
| `priority` | yes | `High` / `Medium` / `Low` |
| `title` | yes | Role title |
| `employer` | yes | Organization |
| `employer_type` | yes | `VA-Federal` / `Academic` / `Hospital-NonProfit` / `Hospital-ForProfit` / `Industry` / `Public-School` / `Other` |
| `category` | yes | `Research` / `Teaching` / `Admin` / `Clinical-Admin` / `Clinical-Research` / `Clinical` / `Industry` / `Other` |
| `location` | yes | City, State or `Remote` |
| `loc_tier` | yes | `"1"` / `"2"` / `"Other"` — quote as string |
| `remote` | yes | `Yes` / `No` / `Hybrid` — quote `"No"` (YAML coerces unquoted No to bool) |
| `salary` | no | As posted (range when available) |
| `date_posted` | no | From listing |
| `date_found` | yes | When our search first saw it, `"YYYY-MM-DD"` |
| `last_checked` | yes | When we last verified the listing is live, `"YYYY-MM-DD"` |
| `deadline` | no | Application deadline if posted |
| `apply_url` | yes | Direct application link |
| `source` | yes | USAJobs / LinkedIn / Indeed / employer site / AAA / ASHA / etc. |
| `research_flag` | no | Boolean — `true` if research/fellowship/PI/etc. mentioned |
| `notes` | no | Hook for why this might fit (one paragraph) |
| `date_closed` | closed-only | `"YYYY-MM-DD"` when moved to `jobs/closed/` |
| `closure_reason` | closed-only | One-sentence reason |

The `details_file` xlsx column is **derived** from the file path — don't set it
in frontmatter.

## Regenerating the tracker

After editing any `jobs/**/*.md` file or appending to `runs.yml`:

```
python regenerate_tracker.py
```

This rewrites `jobs.xlsx` (Active / Closed / Log tabs) and `jobs/README.md`
from scratch. Exit 0 on success; non-zero means a frontmatter validation error
— the message names the offending file.
