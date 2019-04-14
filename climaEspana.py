import matplotlib.pyplot as plt
from datetime import datetime

csv = open('./2010-2012_weather-data-spain.csv','r')
head = csv.readline()
print (head)
j, estaciones, fechas, estacionesFechas = 0, {}, [], {}

while True:
    if j > 100:
        break
    linea = str(csv.readline())
    if len(linea) <= 0:
        break
    if linea[-1] == '\n':
        linea = linea[:-1]
    linea = linea.split(',')
    try:
        auxFecha = str(linea[9] + '/'+ linea[10] + '/' + linea[11])
        auxFecha = datetime.strptime(auxFecha,'%Y/%m/%d')
        fechas.append(auxFecha)
    except :
        pass
    linea[0] = linea[0].replace('"','')
    linea[12] = linea[12].replace('"','')
    try:
        if auxFecha != "":
            estaciones[linea[0]].append(float(linea[12]))
            estacionesFechas[linea[0]].append(auxFecha)
    except:
        if linea[12] != "":
            if auxFecha != "":
                estaciones[linea[0]] = [float(linea[12])]
                try:
                    estacionesFechas[linea[0]].append(auxFecha)
                except:
                    estacionesFechas[linea[0]] = [auxFecha]
    j += 1


""" for item in estaciones:
    estacionesFechas[item] = sorted(estacionesFechas[item])
    print(item,':',estaciones[item], len(estaciones[item]),' ',estacionesFechas[item], len(estaciones[item]))
    print('------------------------------') """
fig, ax = plt.subplots()
fechas = sorted(fechas)
for item in estaciones:
    estacionesFechas[item] = sorted(estacionesFechas[item])
    ax.plot(estacionesFechas[item], estaciones[item], label=item)
    
ax.set_xlabel('Años')
ax.set_ylabel('Temperaturas')
plt.show()