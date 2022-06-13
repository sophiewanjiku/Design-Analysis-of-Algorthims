#constant time
def fact (n):
    """

    :param n:
    :return:
    """
    product = 1
    for i in range(n):
        product = product * (i+1)
        return product
print(fact(10))

    
















