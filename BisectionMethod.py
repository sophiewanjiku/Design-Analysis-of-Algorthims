def bisection(func, a, b, error_accept):
    """
    this function solves for an unknown root for a non-linear function, the initial root boundaries and  an acceptable level of error
    parameters

    :param func:
    :param a:
    :param b:
    :param error_accept:
    :return:
    """
    def f(x):
        f = eval(func)
        return f
    error = abs(b - a)
    while error > error_accept:
        c = (b+a)/2

        if f(a) * f(b) >= 0:
            print("no root or multiple roots present, therefore, the bisection method will not work")
            quit()
        elif f(c) * f(a) < 0:
            b = c
            error = abs(b - a)
        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)

        else:
            print("something went wrong")
            quit()
    print(f"the error is{error}")
    print(f"the lower boundary, a, is {a} and the upper boundary, b, is {b}")
# calling our functions descriptions
# print(bisection. doc)

func = input("Enter func: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
error_accept = float(input("Enter error_accept: "))

# "(4*x  ** 3) + 3*x-3", 0, 1, 0.05
print(bisection(func, a, b, error_accept))
