def test_deque_can_be_rotated(dq):
    dq_1 = dq.copy()
    dq_2 = dq.copy()

    dq_1.rotate(3)
    dq_2.rotate(-4)

    assert list(dq_1) == [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
    assert list(dq_2) == [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]


def test_items_are_appended_and_extended_to_deque(dq):
    dq_1 = dq.copy()

    dq.appendleft(-1)
    assert list(dq) == [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

    dq.append(10)
    assert list(dq) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]

    dq_1.extendleft([-1, -2])
    assert list(dq_1) == [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]

    dq_1.extend([10, 11])
    assert list(dq_1) == [0, 1, 2, 3, 4, 5, 6, 7, 10, 11]
