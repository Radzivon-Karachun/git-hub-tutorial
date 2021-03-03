def bubble_sort(array):
    # Set "switch" to "True" to run the loop at least once
    switch = True
    while switch:
        switch = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # Changing the elements
                array[i], array[i + 1] = array[i + 1], array[i]
                # Set "switch" to "True" for the next iteration
                switch = True


# Example implementation
a = [34, 4, 1, 67, 5, 7, 9, 0, 3, 12, 23, 6]
bubble_sort(a)
print(a)
