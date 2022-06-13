import matplotlib.pyplot as plt
import numpy as np
#for y=2^x

x = [1, 2, 3, 4, 5]
y = [2, 4, 8, 16, 32]


plt.plot(x, y, 'b')
plt.xlabel('inputs')
plt.ylabel('steps')
plt.title('exponential Complexity')
plt.show()

