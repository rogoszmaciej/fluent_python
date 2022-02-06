from dataclasses import InitVar, asdict, dataclass, field
from typing import Callable, ClassVar, List, NamedTuple


class CoordinateBase:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon


class Coordinate(CoordinateBase):
    def __eq__(self, other: "Coordinate"):
        return self.lat == other.lat and self.lon == other.lon


class CoordinateNamedTuple(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"
        return f"{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}"


@dataclass
class CoordinateDataClass:
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"
        return f"{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}"

    def dict(self) -> dict:
        return asdict(self)


@dataclass
class ClubMember:
    name: str
    guests: List[str] = field(default_factory=list)


@dataclass
class HackerClubMember(ClubMember):
    # This needs to be set as the field is not intended as an instance-level field
    all_handles: ClassVar[set[str]] = set()
    handle: str = ""

    def __post_init__(self):
        cls = self.__class__
        if self.handle == "":
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f"handle {self.handle!r} already exists."
            raise ValueError(msg)
        cls.all_handles.add(self.handle)


@dataclass
class DataclassInitVar:
    db: InitVar[Callable]
    user: str
    password: str

    def __post_init__(self, db: str):
        pass


@dataclass
class City:
    continent: str
    name: str
    country: str
