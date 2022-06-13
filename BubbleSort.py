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
if '_name_' == '_main_':
    data = []
    arr1 = []
num = len(data)
num = int(input("number of elements:"))
print("enter elements:")
for i in range(0, num):
    i = int(input())
    data.append(1)
print("array before sorting is:", data)
print(data)
