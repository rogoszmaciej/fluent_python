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


def test_list_is_deep_copied_using_constructor_itself():
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
