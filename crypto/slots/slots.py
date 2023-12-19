
import random
import time
import os

def clear():
    os.system("cls || clear")
from pynetcat import pynetcat

from mt19937predictor import MT19937Predictor

predict = MT19937Predictor()

nc = pynetcat()

nc.connect("0.cloud.chals.io",34865)

first_value = 0

def rng():
    test = str(predict.getrandbits(32))
    test = test.zfill(10)
    return test
def check(f1, f2, f3):
    if f1[0] == f1[1] == f1[2]:
        return True, f1[0] + f1[1] + f1[2]

    if f2[0] == f2[1] == f2[2]:
        return True, f2[0] + f2[1] + f2[2]

    if f3[0] == f3[1] == f3[2]:
        return True, f3[0] + f3[1] + f3[2]

    if f1[0] == f2[1] == f3[2]:
        return True, f1[0] + f2[1] + f3[2]

    if f1[2] == f2[1] == f3[0]:
        return True, f1[2] + f2[1] + f3[0]
forward = """
 Prefix to chal here      
"""

lines = nc.receive(len(forward)).decode()

stored_randoms = []

print(lines)


def getValues():
    nc.sendLine(b"0")

    values = nc.receive(41).decode()
    nc.receive(8000)
    print(values)
    
    values = values.split('\n')
    print(values)
    
    values1 = values[1][3:].split(' ')
    values2 = values[2][3:].split(' ')
    values3 = values[3][3:].split(' ')

    mult = values[4].removeprefix('MULTIPLIER=')
    string = str(values3[0]) + str(values2[0]) + str(values1[0]) + str(values3[1]) + str(values2[1]) + str(values1[1]) + str(values3[2]) + str(values2[2]) + str(values1[2]) + str(mult)
    print(string)
    return string
while len(stored_randoms) < 625:
    val = int(getValues())
    print(val)
    stored_randoms.append(val)
    print(len(stored_randoms))
    predict.setrand_int32(val)

money = b'1000'
for i in range(1, 1000):
    time.sleep(0.100)
    start = rng()
    print(f"NC   : {str()}")
    r1 = start[0:3]
    r2 = start[3:6]
    r3 = start[6:9]
    multi = start[9]
    f1 = r1[2] + r2[2] + r3[2]
    f2 = r1[1] + r2[1] + r3[1]
    f3 = r1[0] + r2[0] + r3[0]
    print(f"LOCAL: {str(start)}")
    canWin = check(f1,f2,f3)
    if canWin and multi != '0':
        nc.sendLine(money)
        print(f"Using ${money}")  
    else:
        nc.sendLine(b"0")  
    stringblock = nc.receive(8120)
    print(stringblock.decode())
    stringblock = stringblock.decode().split('\n')[7]
    print(stringblock)
    money = stringblock.split(' ')[2].encode()