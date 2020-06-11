def Dec2Bin(numb):
    Binary = ['0']*16
    for num in range(0, numb):
        if Binary[15] == '0':
            Binary[15] = '1'
        else:
            index = 15
            while Binary[index] == '1':
                Binary[index] = '0'
                index -= 1
            Binary[index] = '1'
    # return int(''.join(Binary))
    return Binary


def Bin2Dec(numb):
    Binary = ['0']*16
    Final_Number = 0
    Bin = 0
    while numb != Bin:
        if Binary[15] == '0':
            Binary[15] = '1'
        else:
            index = 15
            while Binary[index] == '1':
                Binary[index] = '0'
                index -= 1
            Binary[index] = '1'
        Final_Number += 1
        Bin = int(''.join(Binary))
    return Final_Number


def BinAnd(a, b):
        Bin1 = Dec2Bin(a)
        Bin2 = Dec2Bin(b)
        And = ['0'] * 16
        for number in range(0, 16):
            index = 15 - number
            if Bin1[index] == '1' and Bin2[index] == '1':
                And[index] = '1'
        return Bin2Dec(int(''.join(And)))


def BinOr(a, b):
    Bin1 = Dec2Bin(a)
    Bin2 = Dec2Bin(b)
    Or_ = ['0'] * 16
    for number in range(0, 16):
        index = 15 - number
        if Bin1[index] == '1' or Bin2[index] == '1':
            Or_[index] = '1'
    return Bin2Dec(int(''.join(Or_)))


def BinNot(a):
    Bin1 = Dec2Bin(a)
    Not = ['0'] * 16
    for number in range(0, 16):
        if Bin1[number] == '0':
            Not[number] = '1'
        else:
            Not[number] = '0'
    return Bin2Dec(int(''.join(Not)))


def BinLshift(a, amount):
    Bin1 = Dec2Bin(a)
    Lshift = ['0']*16
    for numbers in range(0, 16):
        shift_number = numbers + amount
        if shift_number <= 15:
            # shift_number -= 16
            Lshift[numbers] = Bin1[shift_number]
    return Bin2Dec(int(''.join(Lshift)))


def BinRshift(a, amount):
    Bin1 = Dec2Bin(a)
    Rshift = ['0']*16
    for numbers in range(0, 16):
        shift_number = numbers - amount
        if shift_number >= 0:
            # shift_number += 16
            Rshift[numbers] = Bin1[shift_number]
    return Bin2Dec(int(''.join(Rshift)))

