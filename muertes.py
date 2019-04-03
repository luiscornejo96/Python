archivo = open('./defunciones.csv')
head =  archivo.readline();
print(head)
j = 0

while True:
    linea =  str(archivo.readline())
    if len(linea) <= 0:
        break
    if linea[-1] == '\n':
        linea = linea[:-1]
    if j > 10:
        break
    j += 1
    linea =  linea.split(',')
    linea =  linea[10]
    print(linea)
