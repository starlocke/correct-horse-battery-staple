from ver_cmp import Program

def test_parsing_simple():
    p = Program()
    assert p.get_ver("1") == ['1']

def test_parsing_simple_semver():
    p = Program()
    assert p.get_ver("3.4.5") == ['3', '4', '5']

def test_parsing_simple_word():
    p = Program()
    assert p.get_ver("foo") == ['foo']

def test_parsing_compound_semver():
    p = Program()
    assert p.get_ver("v1.234") == ['v1', '234']

def test_parsing_compound_trailing_semver():
    p = Program()
    assert p.get_ver("v1.0-alpha") == ['v1', '0-alpha']

def test_parsing_compound_alphanum():
    p = Program()
    assert p.get_ver("v2-alpha") == ['v2-alpha']

def test_parsing_compound_alphanum_2():
    p = Program()
    assert p.get_ver("v2.0-alpha") == ['v2', '0-alpha']

def test_simple_less_cmp():
    p = Program()
    assert p.compare_versions(['1'], ['2']) == -1

def test_simple_greater_cmp():
    p = Program()
    assert p.compare_versions(['3'], ['2']) == 1

def test_simple_equal_cmp():
    p = Program()
    assert p.compare_versions(['4'], ['4']) == 0

def test_numerical_less():
    p = Program()
    assert p.compare_versions(['1'], ['11']) == -1

def test_numerical_more():
    p = Program()
    assert p.compare_versions(['11'], ['1']) == 1

def test_alpha_less():
    p = Program()
    assert p.compare_versions(['alice'], ['bob']) == -1

def test_alpha_more():
    p = Program()
    assert p.compare_versions(['bob'], ['alice']) == 1

def test_alpha_same():
    p = Program()
    assert p.compare_versions(['carole'], ['carole']) == 0

def test_alphanum_less():
    p = Program()
    assert p.compare_versions(['v1'], ['v2']) == -1

def test_alphanum_more():
    p = Program()
    assert p.compare_versions(['v2'], ['v1']) == 1

def test_alphanum_same():
    p = Program()
    assert p.compare_versions(['v3'], ['v3']) == 0

def test_alphanum_less_2():
    p = Program()
    assert p.compare_versions(['v1'], ['v11']) == -1

def test_alphanum_more_2():
    p = Program()
    assert p.compare_versions(['v2'], ['v11']) == 1

def test_alphanum_diff_lengths():
    p = Program()
    assert p.compare_versions(['v2-alpha'], ['v2', '0-alpha']) == 1
