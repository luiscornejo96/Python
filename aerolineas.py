csv = open('./airports.csv','r')
#head = csv.readline()
j = 0
NoAeropuertos = {}
#print(head)
while True:
    linea = str(csv.readline())
    if len(linea) <= 0:
        break
    if linea[-1] == '\n':
        linea = linea[:-1]
    linea =  linea.split(',')
#    if j > 10:
#        break
    try:
        NoAeropuertos[linea[3]] += 1
    except:
        NoAeropuertos[linea[3]] = 1
    j += 1

for item in NoAeropuertos:
    print(item,':',NoAeropuertos[item])
csv.close()
csv =  open('./flights.csv')
head, j, ArrivosEnTiempo, ArrivosFueratiempo, SinTiempo = csv.readline(), 0, 0, 0, 0
NoAereolinas, aereolin , TiempoAerolineas= {}, '', {}
print(head)
while True:
    linea = str(csv.readline())
    if len(linea) <= 0:
        break
    if linea[-1] == '\n':
        linea = linea[:-1]
    """ if j >= 10:
        break """
    linea = linea.split(',')
    aereolin = linea[4]
    try:
        NoAereolinas[aereolin] += 1
    except :
        NoAereolinas[aereolin] = 1
    try:
        TiempoAerolineas[aereolin] = TiempoAerolineas[aereolin]
    except :
        TiempoAerolineas[aereolin] = 0
    try:
        linea = int(linea[22])
        if linea > 0:
            ArrivosFueratiempo += 1
        else:
            ArrivosEnTiempo += 1
        TiempoAerolineas[aereolin] += linea 
    except:
        SinTiempo += 1
        TiempoAerolineas[aereolin] += 0
    #j += 1
print('Arrivos en tiempo:',ArrivosEnTiempo,'\nArrivos Fuera de tiempo:',ArrivosFueratiempo,'\nSin Tiempo:',SinTiempo)
for item in NoAereolinas:
    total = TiempoAerolineas[item] / NoAereolinas[item]
    total =  round(total,3)
    print('Promedio total por la Aerolinea',item,':',total,'min.')