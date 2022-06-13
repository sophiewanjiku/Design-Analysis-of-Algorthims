def selection_sort(array, size):
    for s in range(size):
        minimum_index = s
        for i in range(s +1, size):

            if array[i] < array[minimum_index]:
                minimum_index = i
                (array[s], array[minimum_index]) = (array[minimum_index], array[s])
data = input("enter data")
size = len(data)
selection_sort(data, size)
print("sorted array in ascending order is:")
print(data)
