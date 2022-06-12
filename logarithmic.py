import matplotlib.pyplot as plt
import numpy as np

x = [2, 4, 6, 8, 10, 12]
y = [2, 2, 2, 2, 2, 2]
x2 = [2, 4, 6, 8, 10, 12]
y2 = [12, 4, 5, 2, 8, 9]

# x3 = [2, 4, 6, 8, 10, 12]
# y3 = [2, 4, 6, 8, 10, 12]

x3 = [-3, -2, -1, 0, 1, 2, 3]
y3 = [9, 4, 1, 0, 1, 4, 9]

plt.plot(x, y, 'b')
plt.plot(x2, y2, 'c')
plt.plot(x3, y3)
plt.xlabel('inputs')
plt.ylabel('steps')
plt.title('Constant Complexity')
plt.show()

# plt.plot(x, y, 'b')
# plt.xlabel('inputs')
# plt.ylabel('steps')
# plt.title('Constant Complexity')
# plt.show()