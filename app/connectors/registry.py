from .base import BaseConnector
from .platforms.applicantpro import ApplicantProConnector
from .platforms.adp import ADPConnector
from .platforms.bamboohr import BambooHRConnector
from .platforms.avature import AvatureConnector
from .platforms.brassring import BrassRingConnector
from .platforms.careerplug import CareerPlugConnector
from .platforms.comeet import ComeetConnector
from .platforms.csod import CornerstoneConnector
from .platforms.deel import DeelConnector
from .platforms.dayforce import DayforceConnector
from .platforms.eightfold_ai import EightfoldAIConnector
from .platforms.firststage import FirststageConnector
from .platforms.freshteam import FreshteamConnector
from .platforms.gem import GemConnector
from .platforms.gohire import GoHireConnector
from .platforms.hibob import HiBobConnector
from .platforms.hirehive import HirehiveConnector
from .platforms.hirebridge import HirebridgeConnector
from .platforms.hireology import HireologyConnector
from .platforms.hiringthing import HiringThingConnector
from .platforms.isolvedhire import iSolvedHireConnector
from .platforms.jazzhr import JazzHRConnector
from .platforms.join_com import JoinComConnector
from .platforms.jobvite import JobviteConnector
from .platforms.kula import KulaConnector
from .platforms.manatal import ManatalConnector
from .platforms.icims import ICIMSConnector
from .platforms.oracle_recruiting import OracleRecruitingConnector
from .platforms.paycom import PaycomConnector
from .platforms.paycor import PaycorConnector
from .platforms.paylocity import PaylocityConnector
from .platforms.phenom_people import PhenomPeopleConnector
from .platforms.personio import PersonioConnector
from .platforms.pageup import PageUpConnector
from .platforms.paradox import ParadoxConnector
from .platforms.recooty import RecootyConnector
from .platforms.rippling import RipplingConnector
from .platforms.rival import RivalConnector
from .platforms.sap_successfactors import SAPSuccessFactorsConnector
from .platforms.taleo import TaleoConnector
from .platforms.talentreef import TalentReefConnector
from .platforms.the_panther import ThePantherConnector
from .platforms.teamtailor import TeamtailorConnector
from .platforms.trinet import TriNetConnector
from .platforms.trakstar import TrakstarConnector
from .platforms.ultipro import UltiProConnector
from .platforms.werecruit import WeRecruitConnector
from .platforms.workday import WorkdayConnector
from .platforms.zoho_recruit import ZohoRecruitConnector


CONNECTORS: dict[str, type[BaseConnector]] = {
    "teamtailor": TeamtailorConnector,
    "workday": WorkdayConnector,
    "icims": ICIMSConnector,
    "adp": ADPConnector,
    "dayforce": DayforceConnector,
    "eightfold_ai": EightfoldAIConnector,
    "oracle_recruiting": OracleRecruitingConnector,
    "phenom_people": PhenomPeopleConnector,
    "sap_successfactors": SAPSuccessFactorsConnector,
    "taleo": TaleoConnector,
    "ultipro": UltiProConnector,
    "recooty": RecootyConnector,
    "werecruit": WeRecruitConnector,
    "talentreef": TalentReefConnector,
    "pageup": PageUpConnector,
    "avature": AvatureConnector,
    "brassring": BrassRingConnector,
    "csod": CornerstoneConnector,
    "paradox": ParadoxConnector,
    "applicantpro": ApplicantProConnector,
    "careerplug": CareerPlugConnector,
    "hirebridge": HirebridgeConnector,
    "hireology": HireologyConnector,
    "hiringthing": HiringThingConnector,
    "isolvedhire": iSolvedHireConnector,
    "paycom": PaycomConnector,
    "paycor": PaycorConnector,
    "paylocity": PaylocityConnector,
    "trakstar": TrakstarConnector,
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
