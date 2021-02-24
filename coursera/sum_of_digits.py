digit = int(input())
a = digit % 10
b = (digit // 10) % 10
c = digit // 100
print(a + b + c)
