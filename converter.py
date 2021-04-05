import sys

def get_integer_part(str_number):
    return int(str_number.split('.')[0])

def get_fractionary_part(str_number):
    return int(str_number.split('.')[1])

def convert_integer_part(value, target_base):
    result = ''
    while value > 0:
        result = result + str(value % target_base)
        value = int(value / target_base)
    result = result[::-1]
    return result

def convert_fractionary_part(value, target_base):
    result = ''
    while value > 0:
        prior_len = len(str(value))
        value = value * target_base
        after_len = len(str(value))
        if prior_len == after_len:
            result = result + '0'
        else:
            result = result + str(value)[0]
        value = int(str(value)[1:])
    return result

def main():
    value_str = ''
    target_base_str = ''
    print('*** Base converter from base 10 to base 2 until 9. Enter the value to be converted, and then the target base. ***\n')
    value_str = input('Please enter the input value to be converted: ')
    target_base_str = input('Please enter the target base in which the value will be converted: ')
    target_base = int(target_base_str)
    if (target_base < 2) or (target_base > 9):
        sys.exit('Invalid target base (the base should be between 2 and 9).')
    integer_part = get_integer_part(value_str)
    if value_str.find('.') != -1:
        fractionary_part = get_fractionary_part(value_str)
        print('\nResult: ' + convert_integer_part(integer_part, target_base) + '.' + convert_fractionary_part(fractionary_part, target_base))
    else:
        print('\nResult: ' + convert_integer_part(integer_part, target_base))

if __name__ == "__main__":
    main()
