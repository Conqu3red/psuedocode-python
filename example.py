# -- BEGIN HELPER FUNCTIONS -- #
import random
def LEN(l):
    return len(l)

def POSITION(v, char):
    try:
        return v.index(char)
    except:
        return -1

def SUBSTRING(p1, p2, string):
    return string[p1:p2+1]

def STRING_TO_INT(v): return int(v)
def STRING_TO_REAL(v): return float(v)
def INT_TO_STRING(v): return str(v)
def REAL_TO_STRING(v): return str(v)
def CHAR_TO_CODE(v): return ord(v)
def CODE_TO_CHAR(v): return chr(v)

def RANDOM_INT(f, c):
    return random.randint(f, c+1)
# -- END HELPER FUNCTIONS -- #

def TotalOut(a, b):
    c = a + b
    while a < c:
        a = a + 1
        b = b - a

    return b



a = 1
while True:
    print( a)
    a = a + 1
    if ( a == 4): break

a = 1
if (a % 2) == 0:

    print( 'even')
else:
    print( 'odd')


for a in range(1,3+1):
    print( a)