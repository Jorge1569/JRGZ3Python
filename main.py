speed = False

const_max_num = '0 0111110 11111111111111'

const_min_num = '0 1000001 00000000000000'

const_pi = '0 0000001 10010010001000'

const_sqrt2 = '0 0000000 01101010000010'

const_e = '0 0000001 01011011111100'

const_euler_mascheroni = '0 1111111 00100111100010'

def decbin(num,digits):
    if not(speed):
        assert type(digits) == int, 'type(arg[1]) = {}'.format(type(digits))
        assert digits >= 1, 'arg[1] = {}'.format(digits)
        assert type(num) == int, 'type(arg[0]) = {}'.format(type(num))
        assert num >= 0 and num <= ((2 ** digits) - 1), 'arg[0] = {}'.format(num)
    return (('0' * (digits - len(bin(num)[2:]))) + bin(num)[2:])

def bindec(text):
    if not(speed):
        assert type(text) == str,'type(arg[0]) = {}'.format(type(text))
        for idx in range(len(text)):
            assert (text[idx] == '0') or (text[idx] == '1'), 'arg[0][{}] = {}'.format(idx, text[idx])
    return int(text,2)

def assert_shortZ3(text):
    if not(speed):
        assert type(text) == str, 'type(arg[0]) = {}'.format(type(text))
        assert len(text) == 22, 'len(arg[0]) == {}'.format(len(text))
        for idx in range(22):
            assert (text[idx] == '0') or (text[idx] == '1'), 'arg[0][{}] = {}'.format(idx, text[idx])

def assert_longZ3(text):
    if not(speed):
        assert type(text) == str, 'type(arg[0]) = {}'.format(type(text))
        assert len(text) == 24, 'len(arg[0]) == {}'.format(len(text))
        assert (text[0] == '0') or (text[0] == '1'), 'arg[0][0] = {}'.format(text[0])
        for idx in range(2,9):
            assert (text[idx] == '0') or (text[idx] == '1'), 'arg[0][{}] = {}'.format(idx, text[idx])
        for idx in range(10,24):
            assert (text[idx] == '0') or (text[idx] == '1'), 'arg[0][{}] = {}'.format(idx, text[idx])
        assert text[1] == ' ', 'arg[0][1] = {}'.format(text[1])
        assert text[9] == ' ', 'arg[0][9] = {}'.format(text[9])

def assert_hexZ3(text):
    if not(speed):
        assert type(text) == str, 'type(arg[0]) = {}'.format(type(text))
        assert len(text) == 6, 'len(arg[0]) == {}'.format(len(text))
        for idx in range(1,6):
            assert (ord(text[idx]) >= ord('0')) and (ord(text[idx]) <= ord('f')), 'arg[0][{}] = {}'.format(idx, text[idx])
            assert (ord(text[idx]) <= ord('9')) or (ord(text[idx]) >= ord('a')), 'arg[0][{}] = {}'.format(idx, text[idx])
        assert (ord(text[0]) >= ord('0')) and (ord(text[0]) <= ord('3')), 'arg[0][0] = {}'.format(text[0])

def assert_dictZ3(my_dict):
    if not(speed):
        assert type(my_dict) == dict, 'type(arg[0]) = {}'.format(type(my_dict))
        assert len(my_dict) == 22, 'len(arg[0]) == {}'.format(len(my_dict))
        for idx in range(22):
            assert type(my_dict[idx]) == bool, 'type(arg[0][{}]) = {}'.format(idx, type(my_dict[idx]))

def assert_memoryInt(num):
    if not(speed):
        assert type(num) == int,  'type(arg[0]) = {}'.format(type(num))
        assert num >= 0 and num <= (2 ** 22) - 1, 'arg[0] = {}'.format(num)

def assert_floatZ3(num):
    if not(speed):
        assert (type(num) == int) or (type(num) == float) or (type(num) == str), 'type(arg[0]) = {}'.format(type(num))
        if type(num) == str:
            assert (num == 'zero') or (num == 'infinity'), 'arg[0] = {}'.format(num)

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

def longZ3_to_float(text):
    assert_longZ3(text)
    return shortZ3_to_float(longZ3_to_shortZ3(text))

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

def hexZ3_to_float(text):
    assert_hexZ3(text)
    return shortZ3_to_float(hexZ3_to_shortZ3(text))

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

def dictZ3_to_float(my_dict):
    assert_dictZ3(my_dict)
    return shortZ3_to_float(dictZ3_to_shortZ3(my_dict))

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

def memoryInt_to_float(num):
    assert_memoryInt(num)
    return shortZ3_to_float(memoryInt_to_shortZ3(num))

def float_to_shortZ3(num, round_mode = 'closer'):
    assert_floatZ3(num)
    assert (round_mode == 'closer') or (round_mode == 'floor'), 'arg[1] = {}'.format(round_mode)
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
    if (max - tmp) < (tmp - min) and round_mode == 'closer':
        mant = mant + 1
    elif round_mode == 'floor':
        mant = mant
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

def roundZ3(num):
    assert_floatZ3(num)
    return dictZ3_to_float(float_to_dictZ3(a))

def isZ3representable(num):
    assert_floatZ3(num)
    if num == 0:
        return True
    return num == roundZ3(num)

def explore_shortZ3(text):
    assert_shortZ3(text)
    print('shortZ3\t\t= {}'.format(text))
    print('longZ3\t\t= {}'.format(shortZ3_to_longZ3(text)))
    print('hexZ3\t\t= {}'.format(shortZ3_to_hexZ3(text)))
    print('memoryInt\t= {}'.format(shortZ3_to_memoryInt(text)))
    print('float\t\t= {}'.format(shortZ3_to_float(text)))

def explore_longZ3(text):
    assert_longZ3(text)
    print('shortZ3\t\t= {}'.format(longZ3_to_shortZ3(text)))
    print('longZ3\t\t= {}'.format(text))
    print('hexZ3\t\t= {}'.format(longZ3_to_hexZ3(text)))
    print('memoryInt\t= {}'.format(longZ3_to_memoryInt(text)))
    print('float\t\t= {}'.format(longZ3_to_float(text)))

def explore_hexZ3(text):
    assert_hexZ3(text)
    print('shortZ3\t\t= {}'.format(hexZ3_to_shortZ3(text)))
    print('longZ3\t\t= {}'.format(hexZ3_to_longZ3(text)))
    print('hexZ3\t\t= {}'.format(text))
    print('memoryInt\t= {}'.format(hexZ3_to_memoryInt(text)))
    print('float\t\t= {}'.format(hexZ3_to_float(text)))

def explore_dictZ3(my_dict):
    assert_dictZ3(my_dict)
    print('shortZ3\t\t= {}'.format(dictZ3_to_shortZ3(my_dict)))
    print('longZ3\t\t= {}'.format(dictZ3_to_longZ3(my_dict)))
    print('hexZ3\t\t= {}'.format(dictZ3_to_hexZ3(my_dict)))
    print('memoryInt\t= {}'.format(dictZ3_to_memoryInt(my_dict)))
    print('float\t\t= {}'.format(dictZ3_to_float(my_dict)))

def explore_memoryInt(num):
    assert_memoryInt(num)
    print('shortZ3\t\t= {}'.format(memoryInt_to_shortZ3(num)))
    print('longZ3\t\t= {}'.format(memoryInt_to_longZ3(num)))
    print('hexZ3\t\t= {}'.format(memoryInt_to_hexZ3(num)))
    print('memoryInt\t= {}'.format(num))
    print('float\t\t= {}'.format(memoryInt_to_float(num)))

def explore_float(num):
    assert_floatZ3(num)
    print('shortZ3\t\t= {}'.format(float_to_shortZ3(num)))
    print('longZ3\t\t= {}'.format(float_to_longZ3(num)))
    print('hexZ3\t\t= {}'.format(float_to_hexZ3(num)))
    print('memoryInt\t= {}'.format(float_to_memoryInt(num)))
    print('float\t\t= {}'.format(roundZ3(num)))
    if isZ3representable(num):
        print('Exact')
    else:
        print('Approximate')

def bit_shortZ3(text,bit):
    assert_shortZ3(text)
    if not(speed):
        assert type(bit) == int, 'type(arg[1]) = {}'.format(type(bit))
        assert bit >= 0, 'arg[1] = {}'.format(bit)
    return text[bit] == '1'

def bit_longZ3(text,bit):
    assert_longZ3(text)
    if not(speed):
        assert type(bit) == int, 'type(arg[1]) = {}'.format(type(bit))
        assert bit >= 0, 'arg[1] = {}'.format(bit)
    return longZ3_to_shortZ3(text)[bit] == '1'

def bit_hexZ3(text,bit):
    assert_hexZ3(text)
    if not(speed):
        assert type(bit) == int, 'type(arg[1]) = {}'.format(type(bit))
        assert bit >= 0, 'arg[1] = {}'.format(bit)
    return hexZ3_to_shortZ3(text)[bit] == '1'

def bit_dictZ3(text,bit):
    assert_dictZ3(text)
    if not(speed):
        assert type(bit) == int, 'type(arg[1]) = {}'.format(type(bit))
        assert bit >= 0, 'arg[1] = {}'.format(bit)
    return dictZ3_to_shortZ3(text)[bit] == '1'

def bit_memoryInt(text,bit):
    assert_memoryInt(text)
    if not(speed):
        assert type(bit) == int, 'type(arg[1]) = {}'.format(type(bit))
        assert bit >= 0, 'arg[1] = {}'.format(bit)
    return memoryInt_to_shortZ3(text)[bit] == '1'

def startZ3():
    global stdin
    global stdout
    global cmd
    global R1
    global R2
    global mem
    stdin = '0'*22
    stdout = '0'*22
    cmd = False
    R1 = '0'*22
    R2 = '0'*22
    mem = {}
    for idx in range(64):
        mem[idx] = '0'*22

def showRegister():
    assert_shortZ3(R1)
    assert_shortZ3(R2)
    print('R1 shortZ3\t= {}'.format(R1))
    print('R1 longZ3\t= {}'.format(shortZ3_to_longZ3(R1)))
    print('R1 hexZ3\t= {}'.format(shortZ3_to_hexZ3(R1)))
    print('R1 memoryInt\t= {}'.format(shortZ3_to_memoryInt(R1)))
    print('R1 float\t= {}\n'.format(shortZ3_to_float(R1)))
    print('R2 shortZ3\t= {}'.format(R2))
    print('R2 longZ3\t= {}'.format(shortZ3_to_longZ3(R2)))
    print('R2 hexZ3\t= {}'.format(shortZ3_to_hexZ3(R2)))
    print('R2 memoryInt\t= {}'.format(shortZ3_to_memoryInt(R2)))
    print('R2 float\t= {}\n'.format(shortZ3_to_float(R2)))
    if cmd:
        print("R1 is NOT clear")
    else:
        print("R1 is clear")

def lu():
    global stdin
    global R1
    global R2
    global cmd
    tmp = input('Insert a number in stdin:\t')
    if tmp == 'zero' or tmp == 'infinity':
        stdin = float_to_shortZ3(tmp)
    else:
        stdin = float_to_shortZ3(float(tmp))
        R1 = stdin
        R2 = '0'*22
        cmd = True

def ld():
    global stdout
    global R1
    global R2
    global cmd
    stdout = R1
    R1 = '0'*22
    R2 = '0'*22
    cmd = False
    print("Z3 returns {}".format(stdout))

def pr(idx):
    global R1
    global R2
    global cmd
    global mem
    if not(cmd):
        R1 = mem[idx]
        cmd = True
    else:
        R2 = mem[idx]

def ps(idx):
    global R1
    global cmd
    global mem
    mem[idx] = R1
    R1 = '0'*22
    cmd = False

def lm():
    global R1
    global R2
    R1 = float_to_shortZ3(shortZ3_to_float(R1) * shortZ3_to_float(R2), 'floor')

def lm():
    global R1
    global R2
    R1 = float_to_shortZ3(shortZ3_to_float(R1) * shortZ3_to_float(R2), 'floor')

def li():
    global R1
    global R2
    if shortZ3_to_float(R2) == 'zero':
        assert shortZ3_to_float(R1) != 'zero', '0/0'
        assert shortZ3_to_float(R2) != 'zero', 'num/0'
    R1 = float_to_shortZ3(shortZ3_to_float(R1) / shortZ3_to_float(R2), 'floor')
    R2 = '0'*22

def lw():
    global R1
    from math import sqrt
    R1 = float_to_shortZ3(sqrt(shortZ3_to_float(R1)), 'floor')

def ls1():
    global R1
    global R2
    R1 = float_to_shortZ3(shortZ3_to_float(R1) + shortZ3_to_float(R2), 'floor')

def ls2():
    global R1
    global R2
    R1 = float_to_shortZ3(shortZ3_to_float(R1) - shortZ3_to_float(R2), 'floor')

def clearAll():
    ps(0)
    ps(0)
    pr(0)
    pr(0)
    for idx in range(64):
        ps(idx)

def clearSaveR2():
    ps(0)
    for idx in range(64):
        ps(idx)

def clear_from_to(start,end):
    ps(start)
    ps(start)
    pr(start)
    pr(start)
    for idx in range(start,end+1):
        ps(idx)

def division_0_0():
    clearAll()
    ls2()
    ps(0)
    pr(0)
    pr(0)
    li()

def division_1_0():
    clearAll()
    ls2()
    ps(0)
    pr(0)
    pr(0)
    ps(0)
    li()
