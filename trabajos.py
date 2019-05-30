import os
import csv

data = os.listdir('./Job Bulletins')
todosDatos, header = [], []
for i in data:
    datos = {}
    archivo = open('./Job Bulletins/{}'.format(i))
    datos = []
    while True:
        linea = str(archivo.readline())
        if len(linea) < 1:
            break
        if linea[-1] == '\n':
            linea = linea[:-1]
        while True:
            if '\t' in linea:
                linea = linea.replace('\t', '')
            else:
                break
        while True:
            if len(linea) > 0:
                if linea[-1] == ' ':
                    linea = linea[:-1]
                elif linea[0] == ' ':
                    linea = linea[1:]
                else:
                    break
            else:
                break
        if len(linea) > 1:
            datos.append(linea)
    archivo.close()

    linea = 0
    while 'CAMPUS' in datos[linea]:
        linea += 1
    datos['Puesto'] = datos[linea]
    while not 'Code' in datos[linea]:
        linea += 1
    aux, aux1 = datos[linea].split(':', 1)[1], ''
    iniciado = False
    for letra in aux:
        if iniciado:
            if letra == ' ':
                break
            else:
                aux1 += letra
        else:
            if letra != ' ':
                aux1 += letra
                iniciado = True
    datos['Clase'] = int(aux1)
    while not ('Open Date' in datos[linea] or 'Open date' in datos[linea]):
        linea += 1
    datos['Fecha Inicio'] = datos[linea].split(':')[-1].strip()
    while not 'ANNUAL SALARY' in datos[linea]:
        linea += 1
    linea += 1
    if ' to ' in datos[linea]:
        datos['Salario Minimo'] = datos[linea].split(' to ')[0].strip()
        datos['Salario Maximo'] = datos[linea].split(' to ')[-1].strip()
    elif '(flat-rated)' in datos[linea]:
        datos['Salario Minimo'] = datos[linea].split(' ')[0].strip()
        datos['Salario Maximo'] = datos[linea].split(' ')[0].strip()
    while not 'REQUIREMENT' in datos[linea]:
        linea += 1
    linea += 1
    numeros = []
    while not 'NOTE' in datos[linea]:
        if 'years' in datos[linea]:
            anios = datos[linea].split('years')[0]
            anios = anios.split(' ')[-2]
            if '.' in anios:
                anios = anios.split('.')[1]
            if len(anios) > 1:
                anios = anios[0].upper() + anios[1:]
            numeros.append((anios))
        linea += 1
    numeros.sort()
    if len(numeros) == 0:
        datos['Experiencia'] = 'No necesaria'
    elif len(numeros) == 1:
        datos['Experiencia'] = numeros[0]
    else:
        datos['Experiencia'] = str(numeros[0]) + ' to ' + str(numeros[-1])
    while not 'TO APPLY' in datos[linea]:
        linea += 1
    linea += 1
    if 'on-line' in datos[linea] or 'online' in datos[linea]:
        try:
            link = 'http' + datos[linea].split('http')[1]
        except:
            linea += 1
            link = 'http' + datos[linea].split('http')[1]
        datos['Aplicar'] = link.split(' ')[0]
    else:
        datos['Aplicar'] = 'Interview whith recruiter'
    try:
        while not 'DEADLINE' in datos[linea]:
            linea += 1
        linea += 1
        if ' by ' in datos[linea]:
            fecha = datos[linea].split('by ')[1]
            fecha = fecha.split(', ')
            datos['Fecha Termino'] = fecha[-2] + ' ' + fecha[-1][:-1]
        elif ' THROUGH ' in datos[linea]:
            fecha = datos[linea].split('THROUGH ')[1]
            fecha = fecha.split(', ')
            datos['Fecha Termino'] = fecha[-2] + ' ' + fecha[-1][:-1]
        elif 'without prior notice' in datos[linea]:
            datos['Fecha Termino'] = 'desconocida'
        elif 'the following' in datos[linea]:
            fecha = datos[linea].split(', ')
            datos['Fecha Termino'] = fecha[-2] + ' ' + fecha[-1][:-1]
        else:
            datos['Fecha Termino'] = 'indeterminada'
    except:
        datos['Fecha Termino'] = 'indeterminada'
    todosDatos.append(datos)

for item in todosDatos[0]:
    header.append(item)
try:
    with open('./trabajos.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for data in todosDatos:
            writer.writerow(data)
except IOError:
    print('Error de escritura')