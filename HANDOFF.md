# Connector Handoff

## Connector Reference

### Niceboard (`niceboard`)

- Extraction: parses Schema.org `JobPosting` JSON-LD, then job-card HTML.
- URL pattern: Niceboard-powered board roots or job listing pages.
- Rate limits: one page request per target; honor `429` responses.

### WordPress Job Manager (`wp_job_manager`)

- Extraction: fetches `/wp-json/wp/v2/job-listings`, then falls back to page JSON-LD/cards.
- URL pattern: a WordPress site root or `/wp-json/wp/v2/job-listings`.
- Rate limits: one API/page request per target; honor WordPress limits.

### JobKit (`jobkit`)

- Extraction: parses `JobPosting` JSON-LD, then HTML job cards.
- URL pattern: JobKit board root or jobs page.
- Rate limits: one page request per target with a 20-second timeout.

### Jobboardly (`jobboardly`)

- Extraction: parses `JobPosting` JSON-LD and paginated HTML cards.
- URL pattern: Jobboardly board root or listing page.
- Rate limits: one page request per target; callers should schedule pagination conservatively.

### Jobiqo (`jobiqo`)

- Extraction: parses `JobPosting` JSON-LD and HTML search cards.
- URL pattern: Jobiqo board root or search page.
- Rate limits: one page request per target; honor provider throttling.

### JBoard.io (`jboard_io`)

- Extraction: parses JBoard.io `JobPosting` JSON-LD and HTML cards.
- URL pattern: JBoard.io board root or jobs page.
- Rate limits: one page request per target with a 20-second timeout.

### JobBoardFire (`jobboardfire`)

- Extraction: parses `JobPosting` JSON-LD and HTML cards.
- URL pattern: JobBoardFire board root or jobs page.
- Rate limits: one page request per target; honor `429`.

### SmartJobBoard (`smartjobboard`)

- Extraction: parses `JobPosting` JSON-LD and `/jobs/` HTML cards.
- URL pattern: SmartJobBoard `/jobs/` page.
- Rate limits: one page request per target; use conservative scheduling.

### JobBoard.io (`jobboard_io`)

- Extraction: parses JobBoard.io/ZipRecruiter `JobPosting` JSON-LD and HTML cards.
- URL pattern: JobBoard.io board root or jobs page.
- Rate limits: one page request per target; honor provider limits.

### Wiley Madgex (`wiley_madgex`)

- Extraction: parses Madgex `JobPosting` JSON-LD and `/jobs/` HTML cards.
- URL pattern: Madgex-powered board `/jobs/` page.
- Rate limits: one page request per target with a 20-second timeout.

### Workday (`workday`)

- Extraction: sends the public CXS XHR POST payload and normalizes `jobPostings`.
- URL pattern: `https://{tenant}.{wd_instance}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs`.
- Rate limits: one POST per target with a 20-second timeout; honor `429` and provider backoff.

### iCIMS (`icims`)

- Extraction: parses iframe career-page JSON-LD and embedded JSON.
- URL pattern: `https://careers-{company}.icims.com/jobs/search?ss=1&in_iframe=1`.
- Rate limits: one page request per target; honor provider throttling.

### ADP (`adp`)

- Extraction: parses the public Workforce Now requisitions JSON response.
- URL pattern: `/mascsr/default/careercenter/public/events/staffing/v1/job-requisitions?cid={cid}`.
- Rate limits: one request per target; honor `429` responses.

### Dayforce (`dayforce`)

- Extraction: parses the public job-board search JSON response.
- URL pattern: `https://jobs.dayforcehcm.com/api/{company}/{locale}/jobboard/search`.
- Rate limits: one request per target with a 20-second timeout.

### Eightfold AI (`eightfold_ai`)

- Extraction: parses the public apply/jobs JSON response.
- URL pattern: `https://{company}.eightfold.ai/api/apply/v2/jobs?domain={company}.com`.
- Rate limits: one request per target; honor provider throttling.

### Oracle Recruiting (`oracle_recruiting`)

- Extraction: parses the public Recruiting Cloud requisitions JSON response.
- URL pattern: `/hcmRestApi/resources/latest/recruitingCEJobRequisitions?finder=findReqs;siteNumber={site}`.
- Rate limits: one request per target; honor API limits.

### Phenom People (`phenom_people`)

- Extraction: parses `phApp.ddo`/embedded page JSON and JSON-LD career data.
- URL pattern: a Phenom public career page or its job-search XHR endpoint.
- Rate limits: one page request per target with a 20-second timeout.

### SAP SuccessFactors (`sap_successfactors`)

- Extraction: parses HTML/JSON-LD first, then XML job nodes.
- URL pattern: `https://career{dc}.successfactors.com/career?company={company}`.
- Rate limits: one request per target; honor provider throttling.

### Taleo (`taleo`)

- Extraction: parses CareerSection HTML/JSON-LD and embedded XHR-shaped data.
- URL pattern: `https://{company}.taleo.net/careersection/{section}/jobsearch.ftl`.
- Rate limits: one page request per target; back off on `429`.

### UltiPro (`ultipro`)

- Extraction: parses UKG Pro/UltiPro public recruiting JSON.
- URL pattern: `/JobBoard/{board_id}/OpportunityDetail` or the public search POST endpoint.
- Rate limits: one request per target with a 20-second timeout.

### Recooty (`recooty`)

- Extraction: parses public career-page JSON-LD and embedded JSON.
- URL pattern: `https://{company}.recooty.com/`.
- Rate limits: one page request per target; honor `429` responses.

### WeRecruit (`werecruit`)

- Extraction: parses public career-page JSON-LD and embedded JSON.
- URL pattern: `https://{company}.werecruit.io/`.
- Rate limits: one page request per target with a 20-second timeout.

### TalentReef (`talentreef`)

- Extraction: parses public JSON first, then HTML/JSON-LD portal data.
- URL pattern: `https://secure.talentreef.com/{company}`.
- Rate limits: one request per target; honor provider throttling.

### PageUp (`pageup`)

- Extraction: parses listing-page JSON-LD and embedded JSON.
- URL pattern: `https://careers.pageuppeople.com/{instance}/cw/en/listing`.
- Rate limits: one page request per target; back off on `429`.

### Avature (`avature`)

- Extraction: parses search-page JSON-LD and embedded JSON.
- URL pattern: `https://{company}.avature.net/careers/SearchJobs`.
- Rate limits: one page request per target with a 20-second timeout.

### BrassRing (`brassring`)

- Extraction: parses search HTML and embedded XHR JSON/JSON-LD data.
- URL pattern: `https://sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid={pid}&siteid={sid}`.
- Rate limits: one request per target; honor provider throttling.

### Cornerstone OnDemand (`csod`)

- Extraction: parses public career-site JSON-LD and embedded JSON.
- URL pattern: `https://{company}.csod.com/ux/ats/careersite/{id}/home`.
- Rate limits: one page request per target; honor `429`.

### Paradox Olivia (`paradox`)

- Extraction: parses public JSON/GraphQL-shaped responses, then career-page JSON-LD and embedded JSON.
- URL pattern: `https://careers.{company}.com` or an Olivia public job-search endpoint.
- Rate limits: one request per target with a 20-second timeout; use provider backoff.

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
