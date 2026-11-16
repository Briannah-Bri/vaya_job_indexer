# Connector Handoff

## Connector Reference

### ApplicantPro (`applicantpro`)

- Extraction: parses public career-page JSON-LD and embedded JSON.
- URL pattern: `https://{company}.applicantpro.com/jobs/`.
- Rate limits: one page request per target; honor `429` responses.

### CareerPlug (`careerplug`)

- Extraction: parses public career-page JSON-LD and embedded JSON.
- URL pattern: `https://{company}.careerplug.com/jobs`.
- Rate limits: one page request per target with a 20-second timeout.

### Hirebridge (`hirebridge`)

- Extraction: parses JSON-LD/HTML first, then XML job-list nodes.
- URL pattern: `https://recruit.hirebridge.com/v3/careerportal/onlineapply/...`.
- Rate limits: one request per target; honor provider throttling.

### Hireology (`hireology`)

- Extraction: parses public JSON, then HTML/JSON-LD career data.
- URL pattern: `https://careers.hireology.com/{company}`.
- Rate limits: one request per target; back off on `429`.

### HiringThing (`hiringthing`)

- Extraction: parses JSON-LD/embedded JSON first, then XML job nodes.
- URL pattern: `https://{company}.hiringthing.com/`.
- Rate limits: one request per target with a 20-second timeout.

### iSolved Hire (`isolvedhire`)

- Extraction: parses public career-page JSON-LD and embedded JSON.
- URL pattern: `https://{company}.isolvedhire.com/jobs/`.
- Rate limits: one page request per target; honor `429`.

### Paycom (`paycom`)

- Extraction: parses public ATS JSON-LD and embedded JSON.
- URL pattern: `https://www.paycomonline.net/v4/ats/web.php/jobs?clientkey={key}`.
- Rate limits: one page request per target with a 20-second timeout.

### Paycor (`paycor`)

- Extraction: parses public JSON, then HTML/JSON-LD career data.
- URL pattern: `https://recruitingbypaycor.com/career/CareerHome.action?clientId={id}`.
- Rate limits: one request per target; honor provider throttling.

### Paylocity (`paylocity`)

- Extraction: parses embedded `window.pageData` JSON, then JSON-LD.
- URL pattern: `https://recruiting.paylocity.com/recruiting/jobs/All/{guid}/{company}`.
- Rate limits: one page request per target; back off on `429`.

### Trakstar (`trakstar`)

- Extraction: parses public career-page JSON-LD and embedded JSON.
- URL pattern: `https://{company}.hire.trakstar.com/`.
- Rate limits: one page request per target with a 20-second timeout.

### Rippling (`rippling`)

- Extraction: parses the public ATS JSON response.
- URL pattern: `https://api.rippling.com/platform/api/ats/v1/board/{board_slug}/jobs`.
- Rate limits: one request per target; honor API throttling and `429` responses.

### Deel (`deel`)

- Extraction: parses `__NEXT_DATA__` embedded JSON, then Schema.org JSON-LD.
- URL pattern: `https://jobs.deel.com/{company}`.
- Rate limits: one page request per target with a 20-second timeout.

### Gem (`gem`)

- Extraction: parses the public job-board JSON response.
- URL pattern: `https://api.gem.com/job_board/v0/{board_token}/job_posts`.
- Rate limits: one request per target; preserve provider throttling.

### Kula (`kula`)

- Extraction: parses `__NEXT_DATA__` embedded JSON, then Schema.org JSON-LD.
- URL pattern: `https://careers.kula.ai/{company}`.
- Rate limits: one page request per target with a 20-second timeout.

### HiBob (`hibob`)

- Extraction: parses the public career jobs JSON API.
- URL pattern: `https://{company}.careers.hibob.com/api/jobs`.
- Rate limits: one request per target; honor `429` responses.

### Join.com (`join_com`)

- Extraction: parses `__NEXT_DATA__` embedded JSON, then Schema.org JSON-LD.
- URL pattern: `https://join.com/companies/{company}`.
- Rate limits: one page request per target with a 20-second timeout.

### Zoho Recruit (`zoho_recruit`)

- Extraction: parses JSON, XML, or public careers-page JSON-LD.
- URL pattern: `/recruit/WebFormServeServlet` or `/jobs/Careers`.
- Rate limits: one request per target; honor provider throttling.

### TriNet (`trinet`)

- Extraction: parses Hirebridge/TriNet Schema.org JSON-LD and embedded career-page JSON.
- URL pattern: TriNet public career portal URLs such as `https://jobs.trinet.com/`.
- Rate limits: one page request per target with a 20-second timeout.

### Rival (`rival`)

- Extraction: parses public career-page JSON-LD and embedded JSON.
- URL pattern: `https://careers.rival-hr.com/{company}`.
- Rate limits: one page request per target with a 20-second timeout.

### Firststage (`firststage`)

- Extraction: parses public career-page JSON-LD and embedded JSON.
- URL pattern: `https://{company}.firststage.co/`.
- Rate limits: one page request per target with a 20-second timeout.

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
