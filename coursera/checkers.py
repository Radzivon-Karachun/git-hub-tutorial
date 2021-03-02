x = int(input())
y = int(input())
A = int(input())
B = int(input())
if B < y:
    print('NO')
elif (A % 2 == 0 and B % 2 == 0) or (A % 2 != 0 and B % 2 != 0):
    print('YES')
else:
    print('NO')
