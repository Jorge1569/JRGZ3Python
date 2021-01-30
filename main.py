speed = False

def assert_shortZ3(text):
    if not(speed):
        assert type(text) == str
        assert len(text) == 22
        for idx in range(22):
            assert (text[idx] == '0') or (text[idx] == '1')

def assert_longZ3(text):
    if not(speed):
        assert type(text) == str
        assert len(text) == 24
        assert (text[0] == '0') or (text[0] == '1')
        for idx in range(2,9):
            assert (text[idx] == '0') or (text[idx] == '1')
        for idx in range(10,24):
            assert (text[idx] == '0') or (text[idx] == '1')
        assert text[1] == ' '
        assert text[9] == ' '

def assert_hexZ3(text):
    if not(speed):
        assert type(text) == str
        assert len(text) == 6
        for idx in range(1,6):
            assert (ord(text[idx]) >= ord('0')) and (ord(text[idx]) <= ord('f'))
            assert (ord(text[idx]) <= ord('9')) or (ord(text[idx]) >= ord('a'))
        assert (ord(text[0]) >= ord('0')) and (ord(text[0]) <= ord('3'))

def assert_dictZ3(my_dict):
    if not(speed):
        assert type(my_dict) == dict
        assert len(my_dict) == 22
        for idx in range(22):
            assert type(my_dict[idx]) == bool

def assert_memoryInt(num):
    if not(speed):
        assert type(num) == int
        assert num >= 0
        assert num <= (2 ** 22) - 1

def assert_floatZ3(num):
    if not(speed):
        assert (type(num) == int) or (type(num) == float) or (type(num) == str)
        if type(num) == str:
            assert (num == 'zero') or (num == 'infinity')

def shortZ3_to_longZ3(text):
    assert_shortZ3(text)
    return text[0] + ' ' + text[1:8] + ' ' + text[8:22]

def shortZ3_to_hexZ3(text):
    assert_shortZ3(text)
    return '{:06x}'.format(int(text,2))

def shortZ3_to_dictZ3(text):
    assert_shortZ3(text)
    my_dict = {}
    for idx in range(22):
        my_dict[idx] = (text[idx] == '1')
    return my_dict

def shortZ3_to_memoryInt(text):
    assert_shortZ3(text)
    return int(text,2)

def longZ3_to_shortZ3(text):
    assert_longZ3(text)
    return text.replace(' ','')

def longZ3_to_hexZ3(text):
    assert_longZ3(text)
    return shortZ3_to_hexZ3(longZ3_to_shortZ3(text))

def longZ3_to_dictZ3(text):
    assert_longZ3(text)
    return shortZ3_to_dictZ3(longZ3_to_shortZ3(text))

def longZ3_to_memoryInt(text):
    assert_longZ3(text)
    return shortZ3_to_memoryInt(longZ3_to_shortZ3(text))

def hexZ3_to_shortZ3(text):
    assert_hexZ3(text)
    return '{:022b}'.format(int(text,16))

def hexZ3_to_longZ3(text):
    assert_hexZ3(text)
    return shortZ3_to_longZ3(hexZ3_to_shortZ3(text))

def hexZ3_to_dictZ3(text):
    assert_hexZ3(text)
    return shortZ3_to_dictZ3(hexZ3_to_shortZ3(text))

def hexZ3_to_memoryInt(text):
    assert_hexZ3(text)
    return shortZ3_to_memoryInt(hexZ3_to_shortZ3(text))

def dictZ3_to_shortZ3(my_dict):
    assert_dictZ3(my_dict)
    text = ''
    for idx in range(22):
        if my_dict[idx]:
            text = text + '1'
        else:
            text = text + '0'
    return text

def dictZ3_to_longZ3(my_dict):
    assert_dictZ3(my_dict)
    return shortZ3_to_longZ3(dictZ3_to_shortZ3(my_dict))

def dictZ3_to_hexZ3(my_dict):
    assert_dictZ3(my_dict)
    return shortZ3_to_hexZ3(dictZ3_to_shortZ3(my_dict))

def dictZ3_to_memoryInt(my_dict):
    assert_dictZ3(my_dict)
    return shortZ3_to_memoryInt(dictZ3_to_shortZ3(my_dict))

def memoryInt_to_shortZ3(num):
    assert_memoryInt(num)
    return (('0' * (22 - len(bin(num)[2:]))) + bin(num)[2:])

def memoryInt_to_longZ3(num):
    assert_memoryInt(num)
    return shortZ3_to_longZ3(memoryInt_to_shortZ3(num))

def memoryInt_to_hexZ3(num):
    assert_memoryInt(num)
    return shortZ3_to_hexZ3(memoryInt_to_shortZ3(num))

def memoryInt_to_dictZ3(num):
    assert_memoryInt(num)
    return shortZ3_to_dictZ3(memoryInt_to_shortZ3(num))

def decbin(num,digits):
    if not(speed):
        assert type(digits) == int
        assert digits >= 1
        assert type(num) == int
        assert num >= 0 and num <= ((2 ** digits) - 1)
    return (('0' * (digits - len(bin(num)[2:]))) + bin(num)[2:])

def bindec(text):
    if not(speed):
        assert type(text) == str
    return int(text,2)

def shortZ3_to_float(text):
    assert_shortZ3(text)
    sign = bindec(text[0])
    sign = (-1) ** sign
    exponent = bindec(text[1:8])
    if exponent >= 64:
        exponent = exponent - 128
    mantissa = float(bindec(text[8:22]) / (2 ** 14)) + 1
    if exponent == -64:
        return 'zero'
    elif exponent == 63:
        return 'infinity'
    else:
        return sign * mantissa * (2 ** exponent)

def longZ3_to_float(text):
    assert_longZ3(text)
    return shortZ3_to_float(longZ3_to_shortZ3(text))
 
def hexZ3_to_float(text):
    assert_hexZ3(text)
    return shortZ3_to_float(hexZ3_to_shortZ3(text))
 
def dictZ3_to_float(my_dict):
    assert_dictZ3(my_dict)
    return shortZ3_to_float(dictZ3_to_shortZ3(my_dict))
 
def memoryInt_to_float(num):
    assert_memoryInt(num)
    return shortZ3_to_float(memoryInt_to_shortZ3(num))
 
def float_to_shortZ3(num):
    assert_floatZ3(num)
    tmp = num
    if tmp == 'zero' or tmp == 0:
        return '0100000000000000000000'
    if tmp == 'infinity':
        return '0011111100000000000000'
    from math import log,floor
    exp = floor(log(tmp,2))
    if exp >= 63:
        return '0011111100000000000000'
    sign = (tmp < 0)
    tmp = abs(tmp)
    mant = (tmp / (2 ** exp)) - 1
    if exp < 0:
        exp = exp + 128
    mant = int(mant * (2 ** 14))
    min = (2 ** exp) * (mant / (2 ** 14) + 1)
    max = (2 ** exp) * ((mant + 1) / (2 ** 14) + 1)
    if (max - tmp) < (tmp - min):
        mant = mant + 1
    tb = ''
    if sign:
        tb = tb + '1'
    else:
        tb = tb + '0'
    tb = tb + decbin(exp,7)
    tb = tb + decbin(mant,14)
    return tb
 
def float_to_longZ3(num):
    assert_floatZ3(num)
    return shortZ3_to_longZ3(float_to_shortZ3(num))
 
def float_to_hexZ3(num):
    assert_floatZ3(num)
    return shortZ3_to_hexZ3(float_to_shortZ3(num))
 
def float_to_dictZ3(num):
    assert_floatZ3(num)
    return shortZ3_to_dictZ3(float_to_shortZ3(num))
 
def float_to_memoryInt(num):
    assert_floatZ3(num)
    return shortZ3_to_memoryInt(float_to_shortZ3(num))

const_max_num = '0 0111110 11111111111111'

const_min_num = '0 1000001 00000000000000'

const_pi = '0 0000001 10010010001000'

const_sqrt2 = '0 0000000 01101010000010'

const_e = '0 0000001 01011011111100'

const_eul_mas = '0 1111111 00100111100010'

def roundZ3(num):
    assert_floatZ3(num)
    return dictZ3_to_float(float_to_dictZ3(a))

def isZ3representable(num):
    assert_floatZ3(num)
    if num == 0:
        return True
    return num == roundZ3(num)
