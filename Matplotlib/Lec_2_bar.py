from matplotlib import pyplot as plt
import numpy as np
x = [5, 10, 15, 20, 25]
y = [5, 10, 15, 20, 25]
py_y = [7, 14, 21, 28, 35]

x_index = np.arange(len(x))
width = 0.15

plt.style.use('fivethirtyeight')
plt.title('Graphs')


plt.bar(x_index+width, py_y, color='lightgreen',width=width)
# plt.plot(x+width, py_y, color='b', marker='o', label='py_y')


plt.bar(x_index-width, y, label='y', color='red',width=width)
# plt.plot(x, y, 'k--', marker='.', label='y', linewidth='3')

plt.xticks(ticks = x_index ,labels=x) #use to remove indices from x-axis after using arange
plt.legend()

plt.tight_layout()  # to avoid padding when u give linewidth
plt.show()
