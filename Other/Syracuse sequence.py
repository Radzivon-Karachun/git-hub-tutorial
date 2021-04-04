import time

n = int(input('Enter the number: '))
x = 0
start_time = time.time()
while True:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3) + 1
    x += 1
    print(x,':', n)
    if n == 1:
        break
print("--- %s seconds ---" % (time.time()-start_time))




