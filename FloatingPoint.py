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
    assert (type(num) == int) or (type(num) == float) or (type(num) == str)
    tmp = num
    if tmp == 'zero':
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
    assert (type(num) == int) or (type(num) == float) or (type(num) == str)
    return shortZ3_to_longZ3(float_to_shortZ3(num))
 
def float_to_hexZ3(num):
    assert (type(num) == int) or (type(num) == float) or (type(num) == str)
    return shortZ3_to_hexZ3(float_to_shortZ3(num))
 
def float_to_dictZ3(num):
    assert (type(num) == int) or (type(num) == float) or (type(num) == str)
    return shortZ3_to_dictZ3(float_to_shortZ3(num))
 
def float_to_memoryInt(num):
    assert (type(num) == int) or (type(num) == float) or (type(num) == str)
    return shortZ3_to_memoryInt(float_to_shortZ3(num))

const_max_num = '0 0111110 11111111111111'

const_min_num = '0 1000001 00000000000000'

const_pi = '0 0000001 10010010001000'

const_sqrt2 = '0 0000000 01101010000010'

const_e = '0 0000001 01011011111100'

const_eul_mas = '0 1111111 00100111100010'
