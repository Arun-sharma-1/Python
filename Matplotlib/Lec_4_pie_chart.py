from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

plt.title('MY Pie Chart ')
label = ['forty ','sixty','fifty','Twenty']
slice = [40,60,50,20]
expload = [0,0,0.1,0]
colors = ['blue','yellow','red','green']
plt.pie(slice,labels=label,wedgeprops={'edgecolor':'black'} , colors=colors ,explode=expload ,autopct='%1.1f%%')

plt.tight_layout() #give some padding
plt.show()