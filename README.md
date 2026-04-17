# Cece's Job Search Tracker

Automated job search for Cece (AuD, ~2–3 yrs post-degree, multi-VA experience, research fellowships). Runs twice weekly (Mon + Thu at 8 am local). Reports emailed from `cece.jobs.bot@gmail.com` to `ruben.purdy@gmail.com` and `ceciliamlacey@gmail.com`.

## What's in this folder

- **jobs.xlsx** — the structured tracker. One row per job. Three tabs:
  - `Active` — open positions Cece might pursue
  - `Closed` — positions that have been taken down or marked withdrawn
  - `Log` — one row per automated run (date, counts, queries used)
- **jobs/** — one markdown file per job (`{job_id}.md`) with the full description, responsibilities, notes, and status history. Unstructured content lives here so the spreadsheet stays clean.
- **reports/** — one dated markdown file per run, summarizing new finds and updates. A copy is also emailed.

## Cece's priorities (in order)

1. **Non-clinical transitions** — research, teaching (university), administration, public-school practice leadership. She's getting tired of direct patient care and wants more control over her practice.
2. **Hybrid clinical + research** — roles that combine clinic with research or admin responsibilities.
3. **Adjacent roles that leverage her AuD + VA + research background** — clinical research coordinator/associate, clinical trial manager, clinical scientist / medical affairs, implementation scientist, program manager on NIH/VA hearing studies, clinical educator, regulatory/clinical affairs at device cos, health services research coordinator, etc.
4. **Pure clinical in Tier 1 locations** — always surface, she'll decide if the role is appealing.
5. **Pure clinical in Tier 2** — only if exceptional.

## Location filter (HARD — no exceptions)

A job must be in one of these metros OR fully remote. Anything else is rejected.

- **Tier 1 (wide search, liberal inclusion):** NYC metro, SF Bay Area (incl. Stanford/Palo Alto), San Diego, Boston metro (incl. Cambridge), Fully Remote
- **Tier 2 (selective — skip generic non-VA clinical):** Seattle, Chicago, Portland OR, Philadelphia, DC metro, Tucson, Pittsburgh

## Experience filter (use judgment — be flexible)

Cece has ~2–3 years post-AuD plus 4 years of AuD training. Many postings count degree/clinical-extern years toward "experience," especially for non-clinical roles.

- **Include:** 0–4 years required, "AuD required" with no year floor, or unspecified.
- **Include with judgment:** up to 5 years — AuD training years often count (especially for non-clinical). Gap noted in the Notes column.
- **Include as a stretch (with note):** up to 6 years for rare non-clinical fits that match her fellowship experience.
- **Exclude:** 7+ years firmly required, "Director / Chief / Service Chief" at large institutions, or PhD-required research positions.

## Employer preference

- Non-profit / government preferred (VA, federal, academic medical centers, public schools, large non-profit hospitals) — enables PSLF.
- Industry (Cochlear, Starkey, Phonak, Oticon, Advanced Bionics, etc.) considered.
- Pure sales roles excluded; franchise retail hearing clinics excluded unless role is explicitly non-clinical (corporate research/training/ops).

## Job ID scheme

Job IDs are `YYMMDD-NNN` based on the date the job was first seen, e.g. `260417-003`. Stable across updates — if a listing gets reposted, it keeps its original ID.

## Columns in jobs.xlsx

| Column | Notes |
|---|---|
| Job ID | Stable identifier |
| Status | New / Active / Applied / Closed / Withdrawn |
| Priority | High / Medium / Low — auto-set based on fit (non-clinical + tier-1 location = High) |
| Title | Role title |
| Employer | Organization |
| Employer Type | VA-Federal / Academic / Hospital-NonProfit / Hospital-ForProfit / Industry / Public-School / Other |
| Category | Research / Teaching / Admin / Clinical-Admin / Clinical-Research / Clinical / Industry / Other |
| Location | City, State or "Remote" |
| Location Tier | 1 / 2 / Other |
| Remote? | Yes / No / Hybrid |
| Salary | As posted (range when available) |
| Date Posted | From listing |
| Date Found | When our search first saw it |
| Last Checked | When we last verified the listing is live |
| Deadline | Application deadline if posted |
| Apply URL | Direct application link |
| Source | USAJobs / LinkedIn / Indeed / employer site / AAA / ASHA / etc. |
| Research Flag | "Y" if mentions research, fellowship, principal investigator, etc. |
| Notes | One-line hook for why this might fit |
| Details File | Relative path to jobs/{id}.md |
