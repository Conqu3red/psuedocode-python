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

