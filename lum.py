import matplotlib.pyplot as plt

csv = open('./caracteristics.csv','r')
head =  csv.readline()
print(head)
lum, etiquetas = {}, {1: 'Full day', 2:'Twiling or dawn', 3: 'Night without public lighting', 4: 'Night with public lighting not lit', 5:'Night with public lighting on'}
j = 0
while True:
    linea = str(csv.readline())
    if len(linea) <= 0:
        break
    if linea[-1] == '\n':
        linea = linea[:-1]
    """ if j > 10:
        break
    j += 1 """
    linea = linea.split(',')
    try:
        lum[linea[5]] += 1
    except:
        lum[linea[5]] = 1
    #print(linea)
for item in etiquetas:
    print(item,',',etiquetas[item])
for item in lum:
    plt.bar( etiquetas[int(item)], lum[item])
print(lum)
plt.title('Lighting : lighting conditions in which the accident occurred')
plt.show()