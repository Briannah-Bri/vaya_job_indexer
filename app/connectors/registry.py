from .base import BaseConnector
from .platforms.bamboohr import BambooHRConnector
from .platforms.comeet import ComeetConnector
from .platforms.deel import DeelConnector
from .platforms.firststage import FirststageConnector
from .platforms.freshteam import FreshteamConnector
from .platforms.gem import GemConnector
from .platforms.gohire import GoHireConnector
from .platforms.hibob import HiBobConnector
from .platforms.hirehive import HirehiveConnector
from .platforms.jazzhr import JazzHRConnector
from .platforms.join_com import JoinComConnector
from .platforms.jobvite import JobviteConnector
from .platforms.kula import KulaConnector
from .platforms.manatal import ManatalConnector
from .platforms.personio import PersonioConnector
from .platforms.rippling import RipplingConnector
from .platforms.rival import RivalConnector
from .platforms.the_panther import ThePantherConnector
from .platforms.teamtailor import TeamtailorConnector
from .platforms.trinet import TriNetConnector
from .platforms.zoho_recruit import ZohoRecruitConnector


CONNECTORS: dict[str, type[BaseConnector]] = {
    "teamtailor": TeamtailorConnector,
    "rippling": RipplingConnector,
    "deel": DeelConnector,
    "gem": GemConnector,
    "kula": KulaConnector,
    "hibob": HiBobConnector,
    "join_com": JoinComConnector,
    "zoho_recruit": ZohoRecruitConnector,
    "trinet": TriNetConnector,
    "rival": RivalConnector,
    "firststage": FirststageConnector,
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
