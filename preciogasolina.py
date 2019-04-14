import xmltodict

with open('./prices.xml') as fd:
    xml = xmltodict.parse(fd.read())
j, minM, minP, minD, maxM, maxP, maxD = 0, 1000.0, 1000.0, 1000.0, 0.0, 0.0, 0.0
varM, varP, varD = 0.0, 0.0, 0.0
promM, promP, promD = 0.0, 0.0, 0.0
gasolinas = {'regular':0, 'premium':0, 'diesel':0}
gasolinasTotal = {'regular':0.0, 'premium':0.0, 'diesel':0.0}
nose = 0
regular, diesel, premium = [], [], []

for item in xml['places']['place']:
    """ if j > 10:
        break """
    aux = item['gas_price']
    try:

        for k in aux:
            #print(k['@type'],float(k['#text']))
            if float(k['#text']) <= 10.0:
                break
            if k['@type'] == 'regular':
                gasolinas['regular'] += 1
                gasolinasTotal['regular'] += float(k['#text'])
                regular.append(float(k['#text']))
                if float(k['#text']) < minD:
                    minM = float(k['#text'])
                if float(k['#text']) > maxM:
                    maxM = float(k['#text'])
            elif k['@type'] == 'premium':
                gasolinas['premium'] += 1
                gasolinasTotal['premium'] += float(k['#text'])
                premium.append(float(k['#text']))
                if float(k['#text']) < minP:
                    minP = float(k['#text'])
                if float(k['#text']) > maxP:
                    maxP = float(k['#text']) 
            elif k['@type'] == 'diesel':
                gasolinas['diesel'] += 1
                gasolinasTotal['diesel'] += float(k['#text'])
                diesel.append(float(k['#text']))
                if float(k['#text']) < minD:
                    minD = float(k['#text'])
                if float(k['#text']) > maxD:
                    maxD = float(k['#text']) 
    except:
        if float(aux['#text']) <= 10.0:
            break
        #print(aux['@type'],aux['#text'])
        if aux['@type'] == 'regular':
            gasolinas['regular'] += 1
            gasolinasTotal['regular'] += float(aux['#text'])
            regular.append(float(aux['#text']))
            if float(aux['#text']) < minM:
                minM = float(aux['#text'])
            if float(aux['#text']) > maxM:
                maxM = float(aux['#text'])
        elif aux['@type'] == 'premium':
            gasolinas['premium'] += 1
            gasolinasTotal['premium'] += float(aux['#text'])
            premium.append(float(aux['#text']))
            if float(aux['#text']) < minP:
                minP = float(aux['#text'])
            if float(aux['#text']) > maxP:
                maxP = float(aux['#text']) 
        elif aux['@type'] == 'diesel':
            gasolinas['diesel'] += 1
            gasolinasTotal['diesel'] += float(aux['#text'])
            diesel.append(float(aux['#text']))
            if float(aux['#text']) < minD:
                minD = float(aux['#text'])
            if float(aux['#text']) > maxD:
                maxD = float(aux['#text'])
    j += 1

for item in regular:
    varM += (item-promM)**2
for item in premium:
    varP += (item-promP)**2
for item in diesel:
    varD += (item-promD)**2

varM = varM/gasolinas['regular']
varP = varP/gasolinas['premium']
varD = varD/gasolinas['diesel']
promM = gasolinasTotal['regular'] / gasolinas['regular']
promP = gasolinasTotal['premium'] / gasolinas['premium']
promD = gasolinasTotal['diesel'] / gasolinas['diesel']
print('Maximo Regular:', maxM, "Maximo Premium:", maxP, "Maximo Diesel:", maxD)
print('Minimo Regular:', minM, "Minimo Premium:", minP, "Minimo Diesel:", minD)
print('Promedio Regular:', promM, "Promedio Premium:", promP, "Promedio Diesel:", promD)
print('Varianza Regular:', varM, 'Varianza Premiun:', varP, 'Varianza Diesel:', varD)
print('Desv. Estandar Regular:', (varM)**.5, 'Desv. Estandar Premiun:', (varP)**.5, 'Desv. Estandar Diesel:', (varD)**.5)