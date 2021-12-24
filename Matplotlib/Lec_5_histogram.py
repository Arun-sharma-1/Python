from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

plt.title('MY Pie Chart ')
age=[20,11,48,23,45,29,30,92,71,46,44,94,23,91,93,94,95,96,97]
bins=[10,20,30,40,50,60,70,80,90,100]
plt.hist(age ,edgecolor='black' ,bins=bins)
plt.tight_layout() #give some padding
plt.show()