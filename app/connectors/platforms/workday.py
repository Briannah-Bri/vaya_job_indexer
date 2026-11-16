from ..base import BaseConnector
from ..common import company_from_url, fetch_json_post, require_jobs
from ..errors import FetchError
from ..models import NormalizedJob


class WorkdayConnector(BaseConnector):
    """Fetch Workday's public CXS jobs endpoint with its XHR POST payload."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        payload = fetch_json_post(
            target_url,
            {"appliedFacets": {}, "limit": 20, "offset": 0, "searchText": ""},
        )
        if not isinstance(payload, dict) or not isinstance(payload.get("jobPostings"), list):
            raise FetchError(200, f"invalid Workday jobs response from {target_url}")
        jobs = []
        for item in payload.get("jobPostings", []):
            title = item.get("title")
            if title:
                jobs.append(
                    NormalizedJob(
                        title, company_from_url(target_url), item.get("locationsText"),
                        item.get("jobDescription"), item.get("externalUrl", target_url),
                    )
                )
        return require_jobs(jobs, target_url)
