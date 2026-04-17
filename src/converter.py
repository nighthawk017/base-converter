import sys


def _get_integer_part(str_number: str) -> int:
    return int(str_number.split('.')[0])


def _get_fractionary_part(str_number: str) -> str:
    return str_number.split('.')[1]


def convert_integer_part(value: int, target_base: int) -> str:
    """Converts a base-10 integer to target_base (2–9).

    Args:
        value: Non-negative integer in base 10.
        target_base: Target base, 2–9.
    Returns:
        String representation of value in target_base.
    """
    if value == 0:
        return '0'
    result = ''
    while value > 0:
        result = str(value % target_base) + result
        value //= target_base
    return result


def convert_fractionary_part(value_str: str, target_base: int) -> str:
    """Converts a base-10 fractional part (as string) to target_base (2–9).

    Args:
        value_str: Digits after the decimal point, e.g. '14' for 0.14.
        target_base: Target base, 2–9.
    Returns:
        String of fractional digits in target_base.
    """
    result = ''
    length = len(value_str)
    value = int(value_str)

    for _ in range(length):
        if value == 0:
            break
        value = value * target_base
        after_len = len(str(value))
        if after_len <= length:
            result += '0'
        else:
            result += str(value)[0]
            value = int(str(value)[1:])
    return result


def convert_number(value_str: str, target_base: int) -> str:
    """Converts a base-10 number string to target_base (2–9).

    Args:
        value_str: Base-10 number as string, e.g. '3.14' or '42'.
        target_base: Target base, 2–9.
    Returns:
        String representation of the number in target_base.
    Raises:
        ValueError: If target_base is outside 2–9 or value_str is not a valid number.
    """
    if (target_base < 2) or (target_base > 9):
        raise ValueError('Target base must be between 2 and 9.')
    if not value_str.replace(".", "", 1).isdigit():
        raise ValueError('Value is not a number. It should only contain numbers of the form ^[0-9\\.]*$')
    integer_part = _get_integer_part(value_str)
    if value_str.find('.') != -1:
        fractionary_part = _get_fractionary_part(value_str)
        return convert_integer_part(integer_part, target_base) + '.' + convert_fractionary_part(fractionary_part, target_base)
    return convert_integer_part(integer_part, target_base)


def main():
    print('*** Base converter from base 10 to bases 2–9. ***\n')
    value_str = input('Enter the value to convert: ')
    target_base_str = input('Enter the target base (2–9): ')
    target_base = int(target_base_str)
    if (target_base < 2) or (target_base > 9):
        sys.exit('Invalid target base (must be between 2 and 9).')
    print('\nResult: ' + convert_number(value_str, target_base))


if __name__ == "__main__":
    main()
