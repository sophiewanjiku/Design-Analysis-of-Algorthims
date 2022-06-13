import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]


plt.plot(x, y, 'b')
plt.xlabel('inputs')
plt.ylabel('steps')
plt.title('quadratic Complexity')
plt.show()

