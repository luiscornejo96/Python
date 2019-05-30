import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', passwd='asdf1234', db='pruebas')
cursor = db.cursor()
cursor = conn.cursor(MySQLdb.cursor.DictCursor)

cursor.execute('select count(*),edad from usuarios group by edad')

resultados = cursor.fetchall()
for registro in resultados:
   print (registro)