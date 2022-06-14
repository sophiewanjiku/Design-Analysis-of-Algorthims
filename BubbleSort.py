def bubble_sort(data):
    """
    :param data:
    :return:
    """
    swapped = True
    while swapped:
        swapped = False
        for i in range (len(data)-1):
            if data[i] > data[i+i]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
if __name__ == '__main__':
    data = []
    arr1 = []
num = len(data)
num = int(input("number of elements:"))
num = int(input("numbers to be sorted"))

print("array before sorting is:", data)
print(data)
