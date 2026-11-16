import xml.etree.ElementTree as ET

from ..base import BaseConnector
from ..common import company_from_url, fetch, html_jobs, html_text, require_jobs
from ..errors import FetchError
from ..models import NormalizedJob


class HiringThingConnector(BaseConnector):
    """Extract HiringThing JSON-LD, embedded JSON, or XML jobs."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        body = fetch(target_url, "text/html, application/xml")
        html = html_text(body, target_url)
        jobs = html_jobs(html, target_url, company_from_url(target_url))
        if jobs:
            return jobs
        try:
            root = ET.fromstring(body)
        except ET.ParseError as exc:
            raise FetchError(200, f"invalid HiringThing feed at {target_url}") from exc
        jobs = []
        for node in root.iter():
            fields = {child.tag.rsplit("}", 1)[-1]: " ".join(child.itertext()).strip()
                      for child in node}
            title = fields.get("title") or fields.get("name")
            if title:
                jobs.append(NormalizedJob(title, company_from_url(target_url),
                                          fields.get("location"), fields.get("description"),
                                          fields.get("url", target_url)))
        return require_jobs(jobs, target_url)
