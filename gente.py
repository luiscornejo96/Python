import matplotlib.pyplot as plt

archivo = open('./population.csv')
pais = {}
paises = {}
a2015 = {}

str(archivo.readline())
str(archivo.readline())
str(archivo.readline())
str(archivo.readline())
header = str(archivo.readline())[:-2].split(',')
aux = []
ijk = 0
for item in header:
    item = item.replace('"', '')
    aux.append(item)
header = aux
aux = [header[0]]
for item in header[5:]:
    aux.append(int(item))
header = aux
print(header[:-1], '\n')
while True:
    item = str(archivo.readline())
    if len(item) < 1:
        break
    item = item[:-2].split(',')
    try:
        paises[item[0]] += int(item[5])
    except:
        if item[5] == '"SP.POP.TOTL"':
            item[6] = item[6].replace('"','')
            item[59] = item[59].replace('"','')
            if item[6] == '':
                pass
            else:
                paises[item[0]] = int(item[6])
                a2015[item[0]] = int(item[59])
        else:
            item[5] = item[5].replace('"','')
            item[56] = item[56].replace('"','')
            if item[5] == '':
                pass
            else:
                paises[item[0]] = int(item[5])
                a2015[item[0]] = int(item[56])
    aux = []
    for row in item:
        row = row.replace('"', '')
        aux.append(row)
    item = aux
    aux = [item[0]]
    if item[4] == '"SP.POP.TOTL"':
        for row in item[5:]:
            if len(row) > 0:
                aux.append(int(row))
    else:
        for row in item[6:]:
            if len(row) > 0:
                aux.append(int(row))
    pais[aux[0]] = aux[1:]

for item in paises:
    crecimiento = (a2015[item] * 100) / paises[item]
    print('crecimiento de', item.replace('"',''), 'es del', crecimiento, '%')

""" for elem in pais:
    print(elem, ':', len(pais[elem]))
    if len(pais[elem]) == 55:
        plt.plot(header[1:-1], pais[elem], label=elem)
    else:
        plt.plot(header[1:], pais[elem], label=elem)
plt.legend()
plt.show() """