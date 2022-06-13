import matplotlib.pyplot as plt
import numpy as np

x = [2, 4, 6, 8, 10, 12]
y = [2, 2, 2, 2, 2, 2]


plt.plot(x, y, 'b')
plt.xlabel('inputs')
plt.ylabel('steps')
plt.title('Constant Complexity')
plt.show()

