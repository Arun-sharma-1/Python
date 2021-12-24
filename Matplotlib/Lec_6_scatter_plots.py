from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

plt.title('MY Scatter plot ')
x = [20, 11, 48, 23, 45]
y = [5, 10, 15, 20, 25]
plt.scatter(x, y,s=100,marker='X')
plt.tight_layout()  # give some padding
plt.show()
