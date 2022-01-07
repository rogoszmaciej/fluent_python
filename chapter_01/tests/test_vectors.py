def test_vector_has_string_reprezentation(vector):
    assert str(vector) == "Vector(3, 4)"


def test_vectors_are_added(vector):
    new_vector = vector + vector

    assert new_vector.x == 6
    assert new_vector.y == 8


def test_vector_absolute_value_is_evaluated(vector):
    assert abs(vector) == 5


def test_vector_is_multiplied_by_scalar(vector):
    new_vector = vector * 5

    assert new_vector.x == 15
    assert new_vector.y == 20
