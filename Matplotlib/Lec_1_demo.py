from matplotlib import pyplot as plt
x = [5, 10, 15, 20, 25]
y = [5, 10, 15, 20, 25]

py_y = [7, 14, 21, 28, 35]

plt.xkcd()
plt.style.use('fivethirtyeight')
plt.title('Graphs')
plt.xlabel('X-axis label ')
plt.ylabel('Y-axis label ')
plt.plot(x, y, 'k--',marker='.', label='y' , linewidth='3')
plt.plot(x, py_y, color='b',marker='o', label='py_y')

plt.legend()
# plt.legend(['y','py_y'])
plt.grid(True)


plt.tight_layout() #to give some padding 
plt.show()
