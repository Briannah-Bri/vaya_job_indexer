# Connector Handoff

## Connector Reference

### Teamtailor (`teamtailor`)

- Extraction: parses career-page JSON-LD `JobPosting` records, then embedded application JSON.
- URL pattern: `https://{company}.teamtailor.com/jobs` or a company career-site root.
- Rate limits: one request per target with a 20-second timeout; callers should back off on `429`.

### Personio (`personio`)

- Extraction: parses XML `<position>` nodes from the public XML feed.
- URL pattern: `https://{company}.jobs.personio.de/xml` with optional `language` query parameter.
- Rate limits: one feed request per target; use conservative scheduling and honor `429`.

### BambooHR (`bamboohr`)

- Extraction: parses the public JSON careers list.
- URL pattern: `https://{company}.bamboohr.com/careers/list`.
- Rate limits: one JSON request per target with a 20-second timeout.

### JazzHR (`jazzhr`)

- Extraction: parses JSON-LD first, then embedded JSON from the public apply widget.
- URL pattern: `https://{company}.applytojob.com/apply` or `/apply/jobs/`.
- Rate limits: one request per target; callers should back off on `429`.

### Jobvite (`jobvite`)

- Extraction: parses XML `<item>`/`<entry>` records for feed URLs, or JSON-LD for HTML career pages.
- URL pattern: `https://jobs.jobvite.com/{company}/jobs/feed` or the company career page.
- Rate limits: one request per target; honor the origin's published limits.

### Freshteam (`freshteam`)

- Extraction: parses career-page JSON-LD, then embedded application JSON.
- URL pattern: `https://{company}.freshteam.com/jobs`.
- Rate limits: one request per target with a 20-second timeout.

### Comeet (`comeet`)

- Extraction: parses the public positions JSON API, with JSON-LD/embedded JSON fallback for career pages.
- URL pattern: `/careers-api/2.0/company/{uid}/positions?token={token}` or a public career page.
- Rate limits: one request per target; preserve any API token and honor provider limits.

### Hirehive (`hirehive`)

- Extraction: parses public career-page JSON-LD, then embedded application JSON.
- URL pattern: `https://{company}.hirehive.com/`.
- Rate limits: one request per target with a 20-second timeout.

### GoHire (`gohire`)

- Extraction: parses the public jobs JSON API, with career-page JSON fallback.
- URL pattern: `https://api.gohire.io/v1/jobs?company={slug}` or a career page.
- Rate limits: one request per target; callers should back off on `429`.

### Manatal (`manatal`)

- Extraction: parses the public career-page jobs JSON API.
- URL pattern: `https://api.manatal.com/open/v3/career-page/{slug}/jobs/`.
- Rate limits: one request per target; follow API pagination and provider limits.

### The Panther (`the-panther`)

- Extraction: parses `application/ld+json` `JobPosting` records when present, then falls back to The Panther Group's public RSS endpoint (`/rss/rss.smpl?arg=list_posts&pp=100&pid=gwt&view=0`).
- URL pattern: `https://jobs.thepanthergrp.com/` or `/index.smpl?arg=jb_search_results&view=0`.
- Rate limits: makes one page request plus one RSS request per target with a 20-second timeout; callers should schedule requests conservatively and honor `429` responses.
