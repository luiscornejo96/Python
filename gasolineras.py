import xmltodict
import matplotlib.pyplot as plt

with open('./places.xml') as fd:
    doc = xmltodict.parse(fd.read())

j = 0
for item in doc['places']['place']:
    X = float(item['location']['x'])
    Y = float(item['location']['y'])
    if X < -80 and Y > 0:
        plt.scatter(X, Y, c='B')
    j += 1
    if j > 9000:
        break
plt.title('Gasolineras en Mexico')
plt.show()