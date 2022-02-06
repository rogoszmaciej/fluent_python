def test_string_and_bytes_length_differ():
    s = "café"
    b = s.encode("utf-8")

    assert len(s) == 4
    assert len(b) == 5
    assert len(b.decode("utf-8")) == 4
