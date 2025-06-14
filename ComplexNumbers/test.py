import pytest
from math import isclose, sqrt
from complex_nums import *

def default_num() :
    return ComplexNum(3, 5)


def test_inverse() :
    z = default_num()
    expected = ComplexNum(0.088235294117647, -0.147058823529411)
    res = z.inverse()
    assert isclose(expected.re, res.re) and isclose(expected.im, res.im)

def test_sum() :
    z = default_num()
    zero = ComplexNum(0, 0)
    expected = z
    res = z + zero
    assert expected.re == res.re and expected.im == res.im

    second = ComplexNum(1, 2)
    res = z + second
    expected = ComplexNum(z.re + second.re, z.im + second.im)
    assert res.re == expected.re and res.im == expected.im

def test_minus() :
    z = default_num()
    second = ComplexNum(1, 2)
    res = z - second
    expected = ComplexNum(z.re - second.re, z.im - second.im)
    assert res.re == expected.re and res.im == expected.im

def test_mult() :
    z = default_num()
    second = ComplexNum(9, 2)
    expected = ComplexNum(17, 51)
    res = z * second
    assert res.re == expected.re and res.im == expected.im

def test_int_power() :
    z = default_num()
    power = 0
    expected = ComplexNum(1, 0)
    res = z.int_power(power)
    assert res.re == expected.re and res.im == expected.im

    power = 14
    expected = ComplexNum(-14923949056, 50358495360)
    res = z.int_power(power)
    assert res.re == expected.re and res.im == expected.im

    power = -5
    expected =  ComplexNum(0.000063122553890, 0.000134256477941)
    res = z.int_power(power)
    assert isclose(expected.re, res.re) and isclose(expected.im, res.im)

def test_div() :
    z = default_num()
    second = ComplexNum(9, 2)
    expected = ComplexNum(0.435294117647058, 0.458823529411764)
    res = z / second
    assert isclose(expected.re, res.re) and isclose(expected.im, res.im)

    zero = ComplexNum(0, 0)
    expected = None
    res = z / zero
    assert res is None

def test_to_polar() :
    z = default_num()
    result = z.to_polar()
    expected = (5.830951894845301, 1.030376826524312)
    assert isclose(result[0], expected[0]) and isclose(result[1], expected[1])

def test_c_abs() :
    z = default_num()
    expected = sqrt(z.re**2 + z.im**2)
    res = abs(z)
    assert isclose(expected, res)

def test_conjugate() :
    z = default_num()
    expected = ComplexNum(z.re, -z.im)
    res = z.conjugate()
    assert res.re == expected.re and res.im == expected.im