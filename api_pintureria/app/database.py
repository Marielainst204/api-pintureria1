import os 
# pip install mysql-connector-python
import mysql.connector # Importa el conector MySQL para conectar con la base de datos
from flask import g  # Importa g de Flask para almacenar datos durante la petición
# pip install python-dotenv
from dotenv import load_dotenv  

d = os.path.dirname(__file__)
os.chdir(d)

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos usando variables de entorno
DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),  
    'password': os.getenv('DB_PASSWORD'),  
    'host': os.getenv('DB_HOST'),  
    'database': os.getenv('DB_NAME'),  
    'port': os.getenv('DB_PORT', 3306) ,
     # Puerto del servidor de la base de datos, por defecto es 3306 si no se especifica
}


# Función para obtener la conexión de la base de datos
def get_db():
   if 'db' not in g:
    g.db = mysql.connector.connect(**DATABASE_CONFIG)
  
    return g.db
    

# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    # Intenta obtener la conexión de la base de datos desde g
    db = g.pop('db', None)
    # Si hay una conexión, la cerramos
    if db is not None:
        print("···· Cerrando conexion a DB ····")
        db.close()
# Función para inicializar la base de datos
def init_db():
    db = get_db()
    cursor = db.cursor()

    # Crear tablas si no existen con todas las claves e índices incluidos
    sql_commands = [

       """ CREATE TABLE IF NOT EXISTS`products` (
         `id_producto` int NOT NULL AUTO_INCREMENT,
         `nombre` varchar(100) NOT NULL,
         `precio` float NOT NULL,
        PRIMARY KEY (`id_producto`)
        ) ;"""

      
    ]

    for command in sql_commands:
        cursor.execute(command)

    db.commit()

   
    cursor.close()

# Función para inicializar la aplicación con el cierre automático de la conexión a la base de datos
def init_app(app):
    # Registrar la función close_db para que se llame automáticamente
    # cuando el contexto de la aplicación se destruye
    app.teardown_appcontext(close_db)
