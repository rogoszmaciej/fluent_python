from copy import deepcopy
from unittest.mock import Mock
from weakref import finalize

from chapter_06.variables import HauntedBus, TwilightBus


def test_updating_list_variable_will_update_variable_that_is_holding_reference_to_it():
    var_a = [1, 2, 3]
    var_b = var_a

    var_a.append(4)

    # var_b holds the reference to var_a and will return it"s updated value
    assert var_b == [1, 2, 3, 4]


def test_creating_identical_objects_will_not_create_references_between_them():
    charles = {"name": "Charles L. Dodgson", "born": 1832}
    lewis = charles
    charles["balance"] = 950

    # identity of objects in memory is the same
    assert charles == lewis and lewis is charles

    alex = {"name": "Charles L. Dodgson", "born": 1832, "balance": 950}
    assert alex == charles
    # identity of two objects differ, even though the content is equal
    assert alex is not charles


def test_new_list_is_created_using_constructor_itself():
    list_1 = ["a", "b", "c"]
    list_2 = list(list_1)

    assert list_1 == list_2
    # list_2 creates new object and therefore new id value
    assert list_2 is not list_1


def test_shallow_copying_a_list_creates_new_list_with_references_to_objects_inside_initial_list():
    list_1 = ["a", "b", ["a", "b"]]
    list_2 = list_1[:]

    assert list_1 == list_2
    assert list_2 is not list_1

    list_1[2].append("c")
    del list_1[0]

    assert list_1 == ["b", ["a", "b", "c"]]
    # Shallow copying copies references to inner objects, hence last item of list_2 is also
    # affected by change! Note after deleting first item of list_1 it stays in list_2
    assert list_2 == ["a", "b", ["a", "b", "c"]]


def test_deepcopy_copies_objects_with_cyclic_references():
    list_1 = [10, 20]
    list_2 = [list_1, 30]

    list_3 = deepcopy(list_2)
    assert list_3 == [[10, 20], 30]
    assert list_3 is not list_2


def test_mutable_argument_as_default_parameter_value_causes_multiple_instances_modify_the_same_value():
    bus_1 = HauntedBus(["Dave", "Bill"])
    assert bus_1.passengers == ["Dave", "Bill"]

    bus_1.pick("Charlie")
    bus_1.drop("Dave")
    assert bus_1.passengers == ["Bill", "Charlie"]

    bus_2 = HauntedBus()
    bus_2.pick("Carrie")
    assert bus_2.passengers == ["Carrie"]

    bus_3 = HauntedBus()
    # Default passengers is mutable, and two instnces reference to the same object in memory
    assert bus_3.passengers == ["Carrie"]

    bus_3.pick("Dave")
    assert bus_2.passengers == ["Carrie", "Dave"]
    assert bus_2.passengers is bus_3.passengers


def test_list_is_modified_by_class_using_reference_instead_of_deepcopy():
    team = ["Sue", "Tina", "Maya", "Diana"]
    bus = TwilightBus(team)

    bus.drop("Diana")

    # List of passengers for bus is modified, as well as initial list!
    assert bus.passengers == ["Sue", "Tina", "Maya"] == team
    assert bus.passengers is team


def test_del_deletes_reference_to_object_and_callback_on_removal_is_invoked():
    s1 = {1, 2, 3}
    s2 = s1
    bye = Mock()  # We set a mock to check if it was called

    ender = finalize(s1, bye)
    assert ender.alive

    del s1
    # We are deleting reference to the set, it is referenced by s2
    assert ender.alive
    bye.assert_not_called()

    s2 = {"a", "b"}
    # s2 Changed it's reference, initial set in not referenced. Mock function should be called
    assert not ender.alive
    assert s2
    bye.assert_called_once()
