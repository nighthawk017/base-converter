import sys


def convert_real_number_str(str_value, target_base, max_fractionary_digits=10000):
    __validate_target_base(target_base)
    integer_part = __get_integer_part(str_value)
    fractionary_part = __get_fractionary_part(str_value)
    result = convert_integer_str(integer_part) + __convert_fractionary_part_str(fractionary_part)
    return result

def convert_integer(str_value, target_base):
    return int(convert_integer_str(str_value, target_base))

def convert_integer_str(str_value, target_base):
    value = int(str_value)
    __validate_target_base(target_base)
    result = ''
    while value > 0:
        result = result + str(value % target_base)
        value = int(value / target_base)
    result = result[::-1]
    return result    

def __convert_fractionary_part_str(str_value, target_base):
    result = ''
    total_value_digits = len(str_value)
    value = int(str_value)
    digits_remaining = len(str(value))
    while value > 0:
        if digits_remaining <= 0:
            break
        prior_len = len(str(value))
        value = value * target_base
        after_len = len(str(value))
        if after_len <= total_value_digits:
            result = result + '0'
        else:
            result = result + str(value)[0]
            value = int(str(value)[1:])
        digits_remaining = digits_remaining - 1
    return result

def __validate_target_base(target_base):
    if target_base < 1 or target_base > 9:
        raise ValueError('Target base should be between 2 and 9.')

def __get_integer_part(str_value):
    return str_value.split('.')[0]

def __get_fractionary_part(str_value):
    return str_value.split('.')[1]


def main():
    str_value = ''
    target_base_str = ''
    print('*** Base converter from base 10 to base 2 until 9. Enter the value to be converted, and then the target base. ***\n')
    str_value = input('Please enter the input value to be converted: ')
    target_base_str = input('Please enter the target base in which the value will be converted: ')
    target_base = int(target_base_str)
    if (target_base < 2) or (target_base > 9):
        sys.exit('Invalid target base (the base should be between 2 and 9).')
    integer_part = __get_integer_part(str_value)
    if str_value.find('.') != -1:
        fractionary_part = __get_fractionary_part(str_value)
        print('\nResult: ' + convert_integer_str(integer_part, target_base) + '.' + __convert_fractionary_part_str(fractionary_part, target_base))
    else:
        print('\nResult: ' + convert_integer_str(integer_part, target_base))

if __name__ == "__main__":
    main()
