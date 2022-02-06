import pytest
from chapter_05.typing import DemoPlainClass


def test_type_annotations_are_interpreted_as_expected():
    assert DemoPlainClass.__annotations__ == {"a": int, "b": float}
    with pytest.raises(AttributeError):
        DemoPlainClass.a
    assert DemoPlainClass.b == 1.1
    assert DemoPlainClass.c == "test"
