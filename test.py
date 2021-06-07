import csv
import matplotlib.pyplot as plt

x = []
y = []
filepath = 'C:/Users/lucaj/PycharmProjects/Simulator/test.xy'
with open(filepath, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[2]))
data = [x, y]

plt.plot(data[0], data[1])
plt.show()
