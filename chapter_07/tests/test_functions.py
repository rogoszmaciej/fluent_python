from functools import partial
from operator import mul
from types import FunctionType

import pytest
from chapter_07.functions import CallableClass, factorial, function_for_partial


def test_function_can_be_aliased():
    def some_function(n):
        return 1 if n < 2 else n * some_function(n - 1)

    test = some_function
    assert list(map(test, range(11))) == [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


def test_functions_are_objects():
    assert factorial.__doc__ == "returns n."
    assert isinstance(factorial, FunctionType)
    assert callable(factorial)


def test_using_lambda_function():
    fruits = ["strawberry", "fig", "apple"]

    assert sorted(fruits, key=lambda word: word[::-1]) == ["apple", "fig", "strawberry"]


def test_class_is_callable():
    callable_class = CallableClass(value=10)

    assert callable(callable_class)
    assert callable_class() == 10


def test_function_has_to_be_called_with_keyword_arguments_only():
    def my_func(*, a, b):
        return a, b

    with pytest.raises(TypeError):
        my_func(1, 2)
    assert my_func(a=1, b=2) == (1, 2)


def test_function_has_to_be_called_with_positional_arguments_only():
    def my_func(a, b, /):
        return a, b

    with pytest.raises(TypeError):
        my_func(a=1, b=2)
    assert my_func(1, 2) == (1, 2)


def test_new_callable_is_created_using_partial():
    partial_1 = partial(function_for_partial, a=10)
    partial_2 = partial(function_for_partial, a="abc")
    triple = partial(mul, 3)

    assert partial_1(b=15) == "Param a: 10, param b: 15"
    assert partial_2(b="def") == "Param a: abc, param b: def"
    assert triple(7) == 21
