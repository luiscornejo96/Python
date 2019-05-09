import matplotlib.pyplot as plt
import numpy as np


csv = open('./accidents_2017.csv','r')
head = csv.readline()
print(head)
j, horas, horasCambio = 0, {}, {}

while True:
    linea = str(csv.readline())
    if len(linea) <= 0:
        break
    if linea[-1] == '\n':
        linea = linea[:-1]
    """ if j > 100:
        break
    j += 1 """
    linea =  linea.split(',')
    try:
        horas[int(linea[7])] +=1
    except:
        horas[int(linea[7])] = 1

for item in range(24):
    print(horas[item])
    horasCambio[item] = horas[item]
yerr = []
for i in range(24):
    yerr.append(1)

fig, ax = plt.subplots()
ind = np.arange(24)
ax.bar(horasCambio.keys(), horasCambio.values(), .8, color='SkyBlue', yerr=yerr)
ax.set_xticks(ind)
ax.set_xticklabels(range(24))
plt.title('Accidentes en las horas del dia')
plt.show()