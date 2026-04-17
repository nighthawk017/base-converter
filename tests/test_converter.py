import pytest
from base_converter import converter


# --- convert_integer_part ---

def test_convert_integer_part_base2():
    assert converter.convert_integer_part(0, 2) == '0'
    assert converter.convert_integer_part(1, 2) == '1'
    assert converter.convert_integer_part(10, 2) == '1010'
    assert converter.convert_integer_part(255, 2) == '11111111'


def test_convert_integer_part_base8():
    assert converter.convert_integer_part(0, 8) == '0'
    assert converter.convert_integer_part(8, 8) == '10'
    assert converter.convert_integer_part(64, 8) == '100'
    assert converter.convert_integer_part(511, 8) == '777'


def test_convert_integer_part_all_bases():
    # 9 in base N is always representable
    assert converter.convert_integer_part(9, 2) == '1001'
    assert converter.convert_integer_part(9, 3) == '100'
    assert converter.convert_integer_part(9, 4) == '21'
    assert converter.convert_integer_part(9, 5) == '14'
    assert converter.convert_integer_part(9, 6) == '13'
    assert converter.convert_integer_part(9, 7) == '12'
    assert converter.convert_integer_part(9, 8) == '11'
    assert converter.convert_integer_part(9, 9) == '10'


# --- convert_fractionary_part ---

def test_convert_fractionary_part_half():
    # 0.5 in base 2 = 0.1
    assert converter.convert_fractionary_part('5', 2) == '1'


def test_convert_fractionary_part_quarter():
    # 0.25 in base 2 = 0.01
    assert converter.convert_fractionary_part('25', 2) == '01'


def test_convert_fractionary_part_base8():
    # 0.5 in base 8 = 0.4
    assert converter.convert_fractionary_part('5', 8) == '4'


def test_convert_fractionary_part_zero():
    assert converter.convert_fractionary_part('0', 2) == ''


# --- convert_number (integration) ---

def test_integer_only():
    assert converter.convert_number('10', 2) == '1010'
    assert converter.convert_number('8', 8) == '10'
    assert converter.convert_number('0', 2) == '0'
    assert converter.convert_number('1', 2) == '1'


def test_fractional():
    assert converter.convert_number('0.5', 2) == '0.1'
    assert converter.convert_number('0.25', 2) == '0.01'
    assert converter.convert_number('3.5', 8) == '3.4'


def test_fractional_result_has_dot():
    result = converter.convert_number('3.14', 8)
    assert '.' in result
    assert result.startswith('3.')


def test_large_integer():
    # 1024 = 2^10
    assert converter.convert_number('1024', 2) == '10000000000'


def test_invalid_base_too_low():
    with pytest.raises(ValueError):
        converter.convert_number('10', 1)


def test_invalid_base_too_high():
    with pytest.raises(ValueError):
        converter.convert_number('10', 10)


def test_invalid_base_zero():
    with pytest.raises(ValueError):
        converter.convert_number('10', 0)


def test_invalid_value_letters():
    with pytest.raises(ValueError):
        converter.convert_number('abc', 2)


def test_invalid_value_negative():
    # negative sign not supported
    with pytest.raises(ValueError):
        converter.convert_number('-5', 2)


def test_invalid_value_multiple_dots():
    with pytest.raises(ValueError):
        converter.convert_number('1.2.3', 2)


def test_boundary_bases():
    # min and max valid bases
    assert converter.convert_number('1', 2) == '1'
    assert converter.convert_number('1', 9) == '1'
