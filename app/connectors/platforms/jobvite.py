import xml.etree.ElementTree as ET

from ..base import BaseConnector
from ..common import company_from_url, fetch, html_jobs, html_text, require_jobs
from ..errors import FetchError
from ..models import NormalizedJob


class JobviteConnector(BaseConnector):
    """Fetch Jobvite XML feeds or HTML job lists."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        body = fetch(target_url, "application/rss+xml, application/xml, text/html")
        if target_url.rstrip("/").endswith("feed"):
            try:
                root = ET.fromstring(body)
            except ET.ParseError as exc:
                raise FetchError(200, f"invalid Jobvite XML from {target_url}") from exc
            jobs = []
            for item in root.iter():
                if item.tag.rsplit("}", 1)[-1] not in {"item", "entry"}:
                    continue
                fields = {child.tag.rsplit("}", 1)[-1]: " ".join(child.itertext()).strip()
                          for child in item}
                if fields.get("title"):
                    jobs.append(NormalizedJob(fields["title"], company_from_url(target_url),
                                              fields.get("location"), fields.get("description"),
                                              fields.get("link", target_url), fields.get("type")))
            return require_jobs(jobs, target_url)
        return require_jobs(html_jobs(html_text(body, target_url), target_url), target_url)
