from array import array


def test_list_and_array_are_created():
    test_list = [i for i in range(0, 10)]
    test_array = array("I", (i for i in range(0, 10)))

    for li, ai in zip(test_list, test_array):
        assert li == ai


def test_tuples_can_be_used_as_records():
    variable = [("USA", "31195855")]

    for passport in sorted(variable):
        assert passport[0] == "USA"
        assert passport[1] == "31195855"

    for country, _ in variable:
        assert country == "USA"


def test_tuples_can_be_unpacked():
    def get_name():
        return "John", "Doe"

    country, id = ("USA", "some-id")

    assert country == "USA"
    assert id == "some-id"

    first_name, last_name = get_name()

    assert first_name == "John"
    assert last_name == "Doe"


def test_asterisk_can_be_used_to_grab_excess_items():
    a, b, *rest_1 = range(5)
    c, d, *rest_2 = range(2)
    e, *rest_3, f = range(6)

    assert a == 0
    assert b == 1
    assert c == 0
    assert d == 1
    assert e == 0
    assert f == 5
    assert rest_1 == [2, 3, 4]
    assert not rest_2
    assert rest_3 == [1, 2, 3, 4]


def test_nested_tuples_can_be_unpacked():
    variable = ("Tokyo", "JP", 36.933, (35.689722, 139.691667))

    city, country, _, (lat, lon) = variable

    assert city == "Tokyo"
    assert country == "JP"
    assert lat == 35.689722
    assert lon == 139.691667


def test_list_is_sliced_with_colon():
    test_list = [10, 20, 30, 40, 50, 60]

    assert test_list[:2] == [10, 20]
    assert test_list[3:] == [40, 50, 60]
    assert test_list[1:4] == [20, 30, 40]


def test_list_is_sliced_with_multilpe_colons():
    test_list = [10, 20, 30, 40, 50, 60, 70]

    assert test_list[::3] == [10, 40, 70]
    assert test_list[::-1] == [70, 60, 50, 40, 30, 20, 10]
    assert test_list[::-2] == [70, 50, 30, 10]
    assert test_list[2::4] == [30, 70]
    assert test_list[0:6:2] == [10, 30, 50]


def test_operations_on_slices_are_performed():
    test_list_1 = [10, 20, 30, 40, 50, 60, 70]
    test_list_2 = [10, 20, 30, 40, 50, 60, 70]

    test_list_1[0:2] = [11, 22]
    del test_list_1[5:7]

    assert test_list_1 == [11, 22, 30, 40, 50]

    test_list_2[2::4] = [33, 77]

    assert test_list_2 == [10, 20, 33, 40, 50, 60, 77]

    test_list_2[0:5] = [100]

    assert test_list_2 == [100, 60, 77]


def test_creating_list_of_lists_differs_when_using_list_multiplication():
    board_1 = [["_"] * 3 for i in range(3)]
    board_1[1][2] = "X"

    assert sum(row.count("X") for row in board_1) == 1  # Only one row is affected

    board_2 = [["_"] * 3] * 3
    board_2[1][2] = "X"

    for row in board_2:
        assert row[2] == "X"  # All lists reference to the same list!
