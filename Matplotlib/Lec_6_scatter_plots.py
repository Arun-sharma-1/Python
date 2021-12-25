from matplotlib import pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')

plt.title('MY Scatter plot ')
x = [20, 11, 48, 23, 45]
y = [5, 10, 15, 20, 25]
x = np.arange(0,14 , 0.2)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
# plt.scatter(x, y,s=100,marker='X')
# plt.plot(x,y_sin)
# plt.plot(x,y_cos)
plt.plot(x,y_tan)
plt.tight_layout()  # give some padding
plt.show()
