from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask import session, flash
import os
from dotenv import load_dotenv
from flask_mail import Mail, Message
app = Flask(__name__)  
app.config['SECRET_KEY'] = 'darwin'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'carlospalechor211@gmail.com' 
app.config['MAIL_PASSWORD'] = 'ymsnngdgmhctqudk '    
app.config['MAIL_DEFAULT_SENDER'] = 'carlospalechor211@gmail.com'

mail = Mail(app)


CORS(app)
app.config["UPLOAD_FOLDER"] = "./static/img"
# app.config["MONGODB_SETTINGS"] = [{
#     "db": "GestionPeliculas",
#     "host": "mongodb+srv://dstevengmz1293:<db_password>@cluster0.6jt6j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
#     "port": 27017
# }]
app.config["MONGODB_SETTINGS"] = [{
    "db": "GestionPeliculas",
    "host": os.getenv("//carlospalechor211:Ff7RNy6IPeDHZeGP@cluster0.mcui333.mongodb.net/GestionPeliculas?"),
    "port": 27017
}]

db = MongoEngine(app)

from routers.genero import *
from routers.pelicula import * 
from routers.login import * 
from routers.usuario import * 
from routers.recuperar import * 

if __name__ == "__main__":
    app.run(port=6510, host="0.0.0.0", debug=True)
