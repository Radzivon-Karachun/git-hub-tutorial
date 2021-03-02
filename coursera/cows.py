n = int(input())
if n == 0 or n == 5 or n == 6 or n == 7 or n == 8 or n == 9:
    print(n, 'korov')
elif n >= 10 and n <= 20:
    print(n, 'korov')
elif n % 10 == 0:
    print(n, 'korov')
elif n % 10 == 5:
    print(n, 'korov')
elif n % 10 == 6:
    print(n, 'korov')
elif n % 10 == 7:
    print(n, 'korov')
elif n % 10 == 8:
    print(n, 'korov')
elif n % 10 == 9:
    print(n, 'korov')
elif n == 1 or n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
