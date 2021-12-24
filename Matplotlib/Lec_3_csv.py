from matplotlib import pyplot as plt
import numpy as np
import csv
x = [5, 10, 15, 20, 25]
y = [5, 10, 15, 20, 25]
py_y = [7, 14, 21, 28, 35]

x_index = np.arange(len(x))
width = 0.15

plt.style.use('fivethirtyeight')
plt.title('Graphs')

with open('csv_sample.ppm') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    row = next(csv_reader)
    print(row)

     