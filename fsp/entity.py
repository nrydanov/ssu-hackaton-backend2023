from dataclasses import dataclass, field
from datetime import datetime

from .db.models import Claim, Gender

from .db.models import State


@dataclass
class User:
    email: str
    password: str
    claims: list = field(default_factory=lambda: [Claim.ATHLETE])


@dataclass
class Event:
    name: str
    date_started: str
    date_ended: str
    location: str
    about: str
    id: str = None


@dataclass
class Profile:
    phone: str
    address: str
    passport: str
    birthday: datetime.date
    gender: Gender
    organization: str
    name: str
    surname: str
    patronymic: str
    insurance: str


@dataclass
class EventRequest:
    id: int
    event_id: int
    state: State
    datetime_create: datetime
    representative_FK: int = None
    partner_FK: int = None


@dataclass
class Team:
    name: str
    rating: int
