import matplotlib.pyplot as plt
import numpy as np

x = [0.11, 0.33, 1, 3, 9, 27, 81]
y = [-2, -1, 0, 1, 2, 3, 4]


plt.plot(x, y, 'b')
plt.xlabel('inputs')
plt.ylabel('steps')
plt.title('logarithmic time complexity')
plt.show()

