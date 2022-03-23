#! C:\Users\Pedro\AppData\Local\Programs\Python\Python37/python.exe
print ("Content-type: text/html\n")
import cgi
form = cgi.FieldStorage()

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='asir21', #Aquí añade la contraseña de la base de datos.
    database='soundme', #Aquí añade el nombre de la base de datos.
    port="3306"
    )

if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = mydb.cursor()
        entrada = 1
        while entrada == 1:
            nombre = form.getvalue('nombre')
            apellido = form.getvalue('apellido')
            email = form.getvalue('correo')
            password = form.getvalue('password')

            entrada = 0

            sql = "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)"
            val = (nombre, apellido, email, password)
            cursor.execute(sql, val)
            mydb.commit()
            print("<h1>Usuario registrado</h1>")
            print("<a href='index.html'>Volver</a>")
else:
    print("<h1>No se pudo conectar a la base de datos</h1>")
    print("<a href='index.html'>Volver</a>")