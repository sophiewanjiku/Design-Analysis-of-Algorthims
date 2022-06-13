#factorial time
#recurssion technique
def fact2(n):
    """

    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        return n * fact2(n-1)


print(fact2(10))

