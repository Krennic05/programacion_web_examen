from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        pinturas = request.form['pinturas']
        #A continuación hacemos que no se pueda llenar el formulario con valores invalidos
        if (not edad.isnumeric()) or (not pinturas.isnumeric()) or (nombre == "") or (edad == "") or (pinturas == ""):
            return render_template('ejercicio1.html', clienteInput="ERROR", totalInput="Por favor ingresar valores validos")
        cliente = f'Nombre del cliente: ${nombre}'
        #no entiendo por que en el ejemplo hay un '$' en el nombre, pero lo mantengo en mi trbajao para asi seguir el ejemplo
        edad = int(edad)
        pinturas = int(pinturas)

        if (edad >= 18) and (edad <= 30):
            t = pinturas * 9000
            d = t * 0.15
            td = t - d
            total = f'Total sin descuento: ${t}'
            descuento = f'El descuento es: ${d}'
            totaldesc = f'El total a pagar es de: ${td}'

        elif edad > 30:
            t = pinturas * 9000
            d = t * 0.25
            td = t - d
            total = f'Total sin descuento: ${t}'
            descuento = f'El descuento es: ${d}'
            totaldesc = f'El total a pagar es de: ${td}'

        else:
            t = pinturas * 9000
            d = t * 0
            td = t - d
            total = f'Total sin descuento: ${t}'
            descuento = f'El descuento es: ${d}'
            totaldesc = f'El total a pagar es de: ${td}'

        return render_template('ejercicio1.html', nombreInput=nombre, edadInput=edad, pinturasInput=pinturas,
                           clienteInput=cliente, totalInput=total, descuentoInput=descuento, totaldescInput=totaldesc)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']
        #a continuación cumplo con el requerimiento como lo entendí en las instrucciones
        #por eso solo se controla si se ingresa al administrador juan o al usuario pepe
        #sin incluir la posibilidad de crear nuevos usuarios, cambiar contraseña ni nada por el estilo.
        if (nombre == "juan") and (contraseña == "admin"):
            saludo = "Bienvenido administrador juan"
        elif (nombre == "pepe") and (contraseña == "user"):
            saludo = "Bienvenido usuario pepe"
        else:
            saludo = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', nombreInput=nombre, contraseñaInput=contraseña, saludoInput=saludo)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)