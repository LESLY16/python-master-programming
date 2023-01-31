import math_func

def test_add():
    assert math_func.add(6, 3) == 9
    assert math_func.add(7) == 12
    assert math_func.add(3) == 8

def test_product():
    assert math_func.product(8) == 24
    assert math_func.product(9, 5) == 45
    assert math_func.product(6) == 18

def test_add_strings():
    result =  math_func.add("Hello", " World")
    assert result == "Hello World"
    assert type(result) == str
    assert "Hedlo" not in result

def test_product_strings():
    assert math_func.product("Hello ", 3) == "Hello Hello Hello "
    result = math_func.product("Hello ")
    assert result == "Hello Hello Hello "
    assert type(result) == str
    assert "Hello" in result

#commands used
#pip install pytest
#pytest -v
#pytest test_math_func.py
#py.test -v
#pytest -v -k "add or string"