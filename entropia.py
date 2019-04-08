import math
archivo = open('./airports.csv')
j ,numeroAeropuertos, entropia = 0.0, 0, 0.0
aeropuertos = {}
while True:
    linea = str(archivo.readline())
    if len(linea) <= 0:
        break
    if linea[-1] == '\n':
        linea =  linea[:-1]
    linea =  linea.split(',')
    linea = linea[3]
    """ if j > 5:
        break∫
    j += 1 """
    try:
        aeropuertos[linea] += 1
        numeroAeropuertos += 1
    except:
        aeropuertos[linea] = 1
        numeroAeropuertos += 1

for item in aeropuertos:
    px = aeropuertos[item] / numeroAeropuertos
    entropia += px * math.log2(px)
entropia = entropia * -1
print('Entropia:', entropia)