x = int(input())
y = int(input())
A = int(input())
B = int(input())
if x % 2 == 0 and y % 2 == 0 and A % 2 == 0 and B % 2 == 0:
    print('YES')
elif x % 2 != 0 and y % 2 != 0 and A % 2 != 0 and B % 2 != 0:
    print('YES')
elif x % 2 == 0 and y % 2 != 0 and A % 2 == 0 and B % 2 != 0:
    print('YES')
elif x % 2 != 0 and y % 2 == 0 and A % 2 == 0 and B % 2 != 0:
    print('YES')
elif x % 2 == 0 and y % 2 != 0 and A % 2 != 0 and B % 2 == 0:
    print('YES')
elif x % 2 != 0 and y % 2 == 0 and A % 2 != 0 and B % 2 == 0:
    print('YES')
elif x % 2 != 0 and y % 2 != 0 and A % 2 == 0 and B % 2 == 0:
    print('YES')
elif x % 2 == 0 and y % 2 == 0 and A % 2 != 0 and B % 2 != 0:
    print('YES')
else:
    print('NO')
