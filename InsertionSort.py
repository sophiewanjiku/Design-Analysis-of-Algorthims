def insertion_sort(list):
    """
    :param alist:
    :return:
    """
    for i in range(1, len(list)):
        temp = list[i]
        x = i - 1
        while (x >= 0 and temp < list[x]):
            list[x + 1] = list[x]
            x = x - 1
        list[x + 1] = temp


list = input('Enter the list of numbers: ').split()
list = [int(n) for n in list]
insertion_sort(list)
print('Sorted list: ', end='')
print(list)