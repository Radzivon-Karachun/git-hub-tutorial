x = int(input())
y = int(input())
A = int(input())
B = int(input())
if A == x + 1 and B == y + 1:
    print('YES')
elif A == x + 1 and B == y:
    print('YES')
elif A == x + 1 and B == y - 1:
    print('YES')
elif A == x and B == y - 1:
    print('YES')
elif A == x - 1 and B == y - 1:
    print('YES')
elif A == x - 1 and B == y:
    print('YES')
elif A == x - 1 and B == y + 1:
    print('YES')
elif A == x and B == y + 1:
    print('YES')
else:
    print('NO')
