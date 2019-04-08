import xmltodict

with open('./prueba.xml') as fd:
    doc = xmltodict.parse(fd.read())
print(doc['mydocument']['@has'])
print(doc['mydocument']['and']['many'][0])
print(doc['mydocument']['plus']['@a'])
print(doc['mydocument']['plus']['#text'])