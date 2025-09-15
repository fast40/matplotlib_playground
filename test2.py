from matplotlib import pyplot as plt
from matplotlib.markers import TICKLEFT
import numpy as np

x = np.arange(30)
y1 = x
y2 = x ** 2
y3 = x ** 3

line, = plt.scatter(x, x**2, label='linear')
# line.axes.grid()
plt.grid()
# line.set_ydata(y2)
# line.axes.relim()
# plt.autoscale()

# for thing in dir(line.axes):
#     print(thing)

# plt.plot(x, y2, label='quadratic')
# plt.plot(x+3, y1, label='linear2')
plt.legend()
plt.show()
