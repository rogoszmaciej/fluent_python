from collections import namedtuple
from dataclasses import FrozenInstanceError, dataclass, fields

from chapter_05.dataclasses import (
    Coordinate,
    CoordinateBase,
    CoordinateDataClass,
    CoordinateNamedTuple,
    DataclassInitVar,
)


def test_objects_with_same_attributes_are_not_equal_by_default():
    c1 = CoordinateBase(lat=10.01, lon=20.35)
    c2 = CoordinateBase(lat=10.01, lon=20.35)

    # Using equality operator returns false
    assert not c1 == c2
    # Values of particular attributes are equal
    assert (c1.lat, c1.lon) == (c2.lat, c2.lon)


def test_comparing_objects_works_as_expected():
    c1 = Coordinate(lat=10.01, lon=20.35)
    c2 = Coordinate(lat=10.01, lon=20.35)
    c3 = Coordinate(lat=10.00, lon=20.00)

    assert c1 == c2
    assert c1 != c3 != c2


def test_collections_namedtuple_can_be_compared_out_of_the_box():
    Coordinate_nt = namedtuple("Coordinate_nt", "lat lon")
    c1 = Coordinate_nt(lat=10.01, lon=20.35)

    assert issubclass(Coordinate_nt, tuple)
    assert c1 == Coordinate_nt(lat=10.01, lon=20.35)


def test_typing_namedtuple():
    c1 = CoordinateNamedTuple(lat=10.01, lon=20.35)
    c2 = CoordinateNamedTuple(lat=10.01, lon=20.35)
    c3 = CoordinateNamedTuple(lat=-20.00, lon=-55.55)

    assert c1 == c2
    assert str(c3) == "20.0°S, 55.5°W"


def test_dataclass():
    c1 = CoordinateDataClass(lat=10.01, lon=20.35)
    c2 = CoordinateDataClass(lat=10.01, lon=20.35)

    assert c1 == c2
    assert str(c1) == "10.0°N, 20.4°E"
    assert c1.dict() == {"lat": 10.01, "lon": 20.35}


def test_dataclass_mutability():
    @dataclass
    class SomeClass:
        test: str

    @dataclass(frozen=True)
    class OtherClass:
        test: str

    some_class = SomeClass(test="some-str")
    other_class = OtherClass(test="some-str")
    some_class.test = "changed-str"
    try:
        other_class.test = "changed-str"
    except FrozenInstanceError:
        pass

    assert some_class.test == "changed-str"
    assert other_class.test == "some-str"


def test_collections_namedtuple_fields_are_initialized_with_string():
    City = namedtuple("City", "name population country")
    city = City(name="Tokyo", population=50000, country="JP")

    assert city.name == "Tokyo"
    assert city.population == 50000
    assert city.country == "JP"


def test_collections_namedtuple_fields_are_initialized_with_iterable():
    City = namedtuple("City", ["name", "population", "country"])
    city = City(name="Delhi", population=99999, country="IN")

    assert city.name == "Delhi"
    assert city.population == 99999
    assert city.country == "IN"


def test_collections_namedtuple_is_initialized_from_tuple():
    City = namedtuple("City", ["name", "population", "country"])
    city = City._make(("Delhi", 99999, "IN"))

    assert city.name == "Delhi"
    assert city.population == 99999
    assert city.country == "IN"
    assert city._asdict() == {"name": "Delhi", "population": 99999, "country": "IN"}


def test_dataclass_init_var_is_not_listed_in_fields():
    def db_init():
        pass

    instance = DataclassInitVar(db=db_init, user="Maciej Rogosz", password="testpass")

    assert "db" not in fields(instance)
