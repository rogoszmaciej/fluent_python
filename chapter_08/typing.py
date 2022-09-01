import sys
from collections import Counter
from collections.abc import Sequence
from random import shuffle
from typing import (
    Any,
    Callable,
    Hashable,
    Iterable,
    NoReturn,
    Optional,
    Protocol,
    TypeVar,
)

# NamesList is a typing alias for Iterable holding str values
NamesList = Iterable[str]


def transform_names(names: Optional[NamesList] = None) -> list[str]:
    uppercase = []
    if names is None:
        names = []
    for name in names:
        uppercase.append(name.upper())
    return uppercase


# T type implicate type returned in the list is the same as type of elements in the Sequence
T = TypeVar("T")


def size_users(user_names: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError("size must be >= 1")
    result = list(user_names)
    shuffle(result)
    return result[:size]


def mode(data: Iterable[float]) -> float:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError("no mode for empty data")
    return pairs[0][0]


# The type says that object may be Hashable or any subclass of it
HashableT = TypeVar("HashableT", bound=Hashable)


def mode_bound(data: Iterable[HashableT], lookup: int) -> HashableT:
    pairs = Counter(data).most_common(lookup)
    if len(pairs) == 0:
        raise ValueError("no mode for empty data")
    return pairs[0][0]


# AnyStr is a type that is either bytes or str
AnyStr = TypeVar("AnyStr", bytes, str)


def get_str(data: AnyStr) -> str:
    if isinstance(data, str):
        return data
    return data.decode("utf-8")


# Implement a class subclassing Protocol to mark what methods it needs to implement
class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool:
        ...


LT = TypeVar("LT", bound=SupportsLessThan)


# The ellipsis in tuple indicates it can contain any numbet of 'LT' objects
def sort_values_and_trim(data: tuple[LT, ...], size: int) -> tuple[LT, ...]:
    return tuple(sorted(data)[:size])


# Using a parametrized Callable can point what kind of callable we expect
def plural(word: str, number: int) -> str:
    if not number:
        word = "none"
    elif number > 1:
        word = word + "s"
    return f"We got {number} {word}."


def print_sth(word: str, number: int, print_func: Callable[[str, int], str]) -> str:
    return print_func(word, number)


# Callable for functions with flexible signatures
# Callable[..., ReturnType]

# Callable with no specified arguments
# Callable[[], ReturnType]


# NoReturn means function never returns anything
# __ in front of variable means its positional only!
def sys_exit(__status: object = ...) -> NoReturn:
    sys.exit(__status)


# This annotation means that:
# - all positional arguments in content are all type str
# - all keyword arguments in attrs are all type str


def tag(
    name: str,
    /,
    *content: str,
    class_: Optional[str] = None,
    **attrs: str,
) -> str:
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs["class"] = class_
    attr_pairs = (f" {attr}={value}" for attr, value in sorted(attrs.items()))
    attr_str = "".join(attr_pairs)
    if content:
        elements = (f"<{name}{attr_str}>{c}</{name}>" for c in content)
        return "\n".join(elements)
    else:
        return f"<{name}{attr_str} />"
