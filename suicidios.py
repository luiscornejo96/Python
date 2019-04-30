import matplotlib.pyplot as plt

csv = open('./suicides.csv','r')
header = str(csv.readline())
estados = {}
print(header)
j , anio, muertes = 0, [], []

while True:
    linea = str(csv.readline())
    if len(linea) <= 0:
        break
    if j > 10000:
        break
    j += 1
    if linea[-1] == '\n':
        linea = linea[:-1]
    linea = linea.split('"')
    aux = linea[0].split(',')
    aux =  aux[:-1]
    aux2 = linea[1]
    aux3 = linea[2].split(',')
    aux3 = aux3[1:]
    linea = []
    for i in aux:
        linea.append(i)
    linea.append(aux2)
    for i in aux3:
        linea.append(i)
    if linea[-1] == 'Generation X':
        if linea[2] == 'male':
            try:
                try:
                    estados[linea[0]]['anio'].append(int(linea[1]))
                    #anio.append(int(linea[1]))
                    try:
                        estados[linea[0]]['muertes'].append(int(linea[4]))
                        #muertes.append(int(linea[4]))
                    except :
                        estados[linea[0]]['muertes'].append(0)
                        #muertes.append(0)
                except:
                    #anio.append(0)
                    #muertes.append(0)
                    estados[linea[0]]['anio'].append(0)
                    try:
                        estados[linea[0]]['muertes'].append(int(linea[4]))
                        #muertes.append(int(linea[4]))
                    except :
                        estados[linea[0]]['muertes'].append(0)
                        #muertes.append(0)
            except :
                estados[linea[0]] = {'anio': [], 'muertes': []}

fig, ax = plt.subplots()
for item in estados:
    #print(estados[item])
    ax.plot(estados[item]['anio'], estados[item]['muertes'], label = item)
    if item == 'Brazil':
        print(estados[item])
print(len(estados))
ax.legend()
plt.title('Generation X, male')
plt.show()