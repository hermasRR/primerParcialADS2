from flask import Flask, render_template, request, render_template
import mysql.connector

app = Flask(__name__)

datos = []

db = mysql.connector.connect(
    host="172.17.0.2",
    user="usrTesting",
    password="dbtesting",
    database="DBtesting"
)

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/procesarForm', methods=['GET','POST'])
def procesarForm():
    codigo = request.form.get("codigo")
    nombre = request.form.get("nombre")
    carrera = request.form.get("carrera")
    datos.append({"codigo": codigo, "nombre": nombre, "carrera": carrera})

    cursor = db.cursor()

    query = "INSERT INTO cursos (codigo, nombre, carrera) VALUES (%s, %s, %s)"
    values = (codigo, nombre, carrera)
    cursor.execute(query, values)
    
    db.commit()

    #db.close()

    #return "¡Gracias por enviar el formulario!"
    return render_template("index.html", codigo=codigo, nombre=nombre, carrera=carrera, datos=datos)

if __name__ == "__main__":
    app.run(debug=True)
