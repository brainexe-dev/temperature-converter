from temperature_converter import c_to_f, f_to_c, c_to_k, f_to_k

def test_c_to_f():
    assert c_to_f(0) == 32

def test_f_to_c():
    assert f_to_c(32) == 0

def test_c_to_k():
    assert c_to_k(0) == 273.15

def test_f_to_k():
    assert f_to_k(32) == 273.15

def test_c_to_f_100():
    assert c_to_f(100) == 212
