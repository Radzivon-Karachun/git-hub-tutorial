rub = int(input())
kop = int(input())
num = int(input())
KopRub = (kop * num) // 100
totalKop = kop * num - KopRub * 100
totalRub = rub * num + KopRub
print(totalRub, totalKop)
