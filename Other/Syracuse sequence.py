n = int(input('Enter the number: '))


def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('Program execution time: {} seconds'.format(end - start))
        print("--- %s seconds ---" % (end - start))

    return wrapper


@benchmark
def syracuse_sequence():
    global n
    x = 0
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        x += 1
        print(x, ':', n)
        if n == 1:
            break


syracuse_sequence()
