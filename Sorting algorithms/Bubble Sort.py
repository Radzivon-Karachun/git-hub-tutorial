def bubble_sort(array):
    # Array length
    length = len(array)
    # Outer loop, number of passes N-1
    for i in range(length):
        # Inner loop, N-i-1 passes
        for j in range(0, length - i - 1):
            # Change the elements in places
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


# example implementation
a = [34, 4, 1, 67, 5, 7, 9, 0, 3, 12, 23, 6]
bubble_sort(a)
print(a)
