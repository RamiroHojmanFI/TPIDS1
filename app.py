from flask import Flask, render_template, request, redirect, flash


app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_DEFAULT_SENDER'] = ''


@app.route("/")
def home():
    info_evento = { 
            1: {   
                "nombre": "Rally MTB 2025",  
                "organizador": "Club Social y Deportivo Unidos por el Deporte", 
                "slogan":"La carrera de tu vida",
                "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km ...", 
                "fecha": "24 de Octubre de 2025", 
                "horario": "8am", 
                "lugar": "Tandil, Buenos Aires", 
                "tipo_carrera": "MTB rural", 
                "modalidad_costo": {1: {"nombre": "Corta" ,"valor": "100"}, 
            2: {"nombre": "Larga" ,"valor": "200"}}, 
            3:{    
                "Ausp1":"texto",
                "Ausp2":"texto2",
                "Ausp3":"texto3"         
            } }}
    return render_template('index.html', mensaje='lolazo', envio =info_evento) #esto es lo del jinja !!
@app.route("/contacto")

def contacto():
    datos={ 
        'Ramiro Hojman':'245692',
        'Carlos perez':'245692'

    }
    return render_template('contacto.html',datosenvio=datos)

@app.route("/registro")
def registro():
    #aca deberia tomar los datos del participante con el metodo post y mandarlo, lo borre pq no funca lo de correos
    info_evento = { 
            1: {   
                "nombre": "Rally MTB 2025",  
                "organizador": "Club Social y Deportivo Unidos por el Deporte", 
                "slogan":"La carrera de tu vida",
                "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km ...", 
                "fecha": "24 de Octubre de 2025", 
                "horario": "8am", 
                "lugar": "Tandil, Buenos Aires", 
                "tipo_carrera": "MTB rural", 
                "modalidad_costo": {1: {"nombre": "Corta" ,"valor": "100"}, 
            2: {"nombre": "Larga" ,"valor": "200"}}, 
            3:{    
                "Ausp1":"texto",
                "Ausp2":"texto2",
                "Ausp3":"texto3"         
            } }}
    return render_template('registro.html', mensaje='lolazo', envio =info_evento)


if __name__ == "__main__":
    app.run("localhost", port=5002, debug=True)