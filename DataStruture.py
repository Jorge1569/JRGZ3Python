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
