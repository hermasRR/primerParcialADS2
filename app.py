from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/enviarForm', methods=['POST'])
def enviarForm():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    edad = request.form.get("edad")
    fecha_nacimiento = request.form.get("fecha_nacimiento")
    
    #return render_template("received.html", nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, edad=edad)
    return redirect(f'/datosRecibidos?nombre={nombre}&apellido={apellido}&fecha_nacimiento={fecha_nacimiento}&edad={edad}')

@app.route('/datosRecibidos')
def datosRecibidos():
    nombre = request.args.get("nombre")
    apellido = request.args.get("apellido")
    edad = request.args.get("edad")
    fecha_nacimiento = request.args.get("fecha_nacimiento")
    return render_template("received.html", nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, edad=edad)

if __name__ == "__main__":
    app.run()