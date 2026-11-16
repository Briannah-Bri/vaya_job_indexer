from .base import BaseConnector
from .platforms.bamboohr import BambooHRConnector
from .platforms.comeet import ComeetConnector
from .platforms.freshteam import FreshteamConnector
from .platforms.gohire import GoHireConnector
from .platforms.hirehive import HirehiveConnector
from .platforms.jazzhr import JazzHRConnector
from .platforms.jobvite import JobviteConnector
from .platforms.manatal import ManatalConnector
from .platforms.personio import PersonioConnector
from .platforms.the_panther import ThePantherConnector
from .platforms.teamtailor import TeamtailorConnector


CONNECTORS: dict[str, type[BaseConnector]] = {
    "teamtailor": TeamtailorConnector,
    "personio": PersonioConnector,
    "bamboohr": BambooHRConnector,
    "jazzhr": JazzHRConnector,
    "jobvite": JobviteConnector,
    "freshteam": FreshteamConnector,
    "comeet": ComeetConnector,
    "hirehive": HirehiveConnector,
    "gohire": GoHireConnector,
    "manatal": ManatalConnector,
    "the-panther": ThePantherConnector,
}


def get_connector(platform_slug: str) -> BaseConnector:
    try:
        connector_type = CONNECTORS[platform_slug]
    except KeyError as exc:
        raise ValueError(f"Unknown platform: {platform_slug}") from exc
    return connector_type()
