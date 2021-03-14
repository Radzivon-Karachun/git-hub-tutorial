a = int(input())
b = int(input())
c = int(input())
if a + b <= c or a + c <= b or b + c <= a or a + b + c <= 0:
    print('impossible')
elif a == b and a == c:
    print('acute')
elif a**2 == (b**2 + c**2) or b**2 == (a**2 + c**2) or c**2 == (a**2 + b**2):
        print('rectangular')
elif a >= b and a >= c:
    if a**2 > (b**2 + c**2):
        print('obtuse')
    elif a**2 < (b**2 + c**2):
        print('acute')
elif b >= c and b >= a:
    if b**2 > (a**2 + c**2):
        print('obtuse')
    elif b**2 < (a**2 + c**2):
        print('acute')
elif c >= b and c >= a:
    if c**2 > (a**2 + b**2):
        print('obtuse')
    elif c**2 < (a**2 + b**2):
        print('acute')
