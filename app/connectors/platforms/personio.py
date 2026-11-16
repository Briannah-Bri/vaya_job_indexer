import re
import xml.etree.ElementTree as ET

from ..base import BaseConnector
from ..common import fetch, require_jobs
from ..errors import FetchError
from ..models import NormalizedJob


class PersonioConnector(BaseConnector):
    """Parse Personio's public XML ``position`` feed."""

    def fetch_jobs(self, target_url: str) -> list[NormalizedJob]:
        try:
            root = ET.fromstring(fetch(target_url, "application/xml, text/xml"))
        except (UnicodeDecodeError, ET.ParseError) as exc:
            raise FetchError(200, f"invalid Personio XML from {target_url}") from exc
        jobs = []
        for node in root.iter():
            if node.tag.rsplit("}", 1)[-1] != "position":
                continue
            fields = {
                child.tag.rsplit("}", 1)[-1]: " ".join("".join(child.itertext()).split())
                for child in node
            }
            title = fields.get("name") or fields.get("title")
            if not title:
                raise FetchError(200, f"Personio position has no title at {target_url}")
            location = fields.get("office") or fields.get("location")
            url = fields.get("jobUrl") or fields.get("url") or target_url
            jobs.append(NormalizedJob(title, "Personio employer", location,
                                      fields.get("description"), url,
                                      fields.get("employmentType")))
        return require_jobs(jobs, target_url)
