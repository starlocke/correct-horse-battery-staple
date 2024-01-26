import pytest
from is_overlap import Program

def test_touching_edges():
    p = Program()
    assert not p.is_overlap((1, 2), (2, 3))

def test_disconnected_lines():
    p = Program()
    assert not p.is_overlap((5.5, 6.5), (9.5, 10.5))

def test_wholy_embedded_lines():
    p = Program()
    assert p.is_overlap((5, 10), (6, 7))

def test_wholy_embedded_lines_swapped():
    p = Program()
    assert p.is_overlap((6, 7), (5, 10))

def test_leading_edge_embedding():
    p = Program()
    assert p.is_overlap((5, 10), (5, 6))

def test_trailing_edge_embedding():
    p = Program()
    assert p.is_overlap((5, 10), (7, 10))

def test_negatives():
    p = Program()
    assert p.is_overlap((-10, -5), (-7, -6))

def test_embedded_point():
    p = Program()
    assert p.is_overlap((5, 5), (1, 10))

def test_disjoint_point():
    p = Program()
    assert not p.is_overlap((12, 12), (1, 10))

def test_disjoint_points():
    p = Program()
    assert not p.is_overlap((12, 12), (1, 1))

def test_reversed_lines():
    p = Program()
    # expected to fail because input hasn't been properly normalized
    assert not p.is_overlap((10, 5), (6, 4))

def test_reversed_lines_properly_handled():
    p = Program()
    assert p.is_overlap(p.get_line("10,5"), p.get_line("6,4"))

def test_bad_input_brackets():
    p = Program()
    with pytest.raises(ValueError):
        p.get_line("[128,256]")

def test_bad_input_incomplete():
    p = Program()
    with pytest.raises(ValueError):
        p.get_line("123")

def test_bad_input_str():
    p = Program()
    with pytest.raises(ValueError):
        p.get_line("0xFF,0xFA")

def test_bad_input_missing_second():
    p = Program()
    with pytest.raises(ValueError):
        p.get_line("(128,)")

def test_bad_input_missing_first():
    p = Program()
    with pytest.raises(ValueError):
        p.get_line("(,128)")

def test_ok_odd_input_missing_head():
    p = Program()
    assert p.get_line("123,456)") == (123, 456)

def test_ok_odd_input_missing_tail():
    p = Program()
    assert p.get_line("(123,456") == (123, 456)

def test_ok_input():
    p = Program()
    assert p.get_line("123,456") ==  (123, 456)

def test_ok_input_bracketed():
    p = Program()
    assert p.get_line("(123,456)") == (123, 456)

def test_ok_input_reversed():
    p = Program()
    assert p.get_line("(456,123)") == (123, 456)

def test_ok_input_negatives():
    p = Program()
    assert p.get_line("(-1,-5)") == (-5, -1)

def test_ok_input_floats():
    p = Program()
    assert p.get_line("(1.5,2.5)") == (1.5, 2.5)

def test_ok_input_spaces():
    p = Program()
    assert p.get_line("(   1,    5   )") == (1, 5)
