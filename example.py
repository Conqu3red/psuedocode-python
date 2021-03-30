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