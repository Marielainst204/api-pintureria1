import os, time
# Instalar con pip install flask
from flask import Flask, jsonify, request
# Instalar con pip install flask-cors
from flask_cors import CORS

"""
Para trabajar con archivos asegurar que un nombre de archivo 
proporcionado por el usuario sea seguro para guardarlo en el sistema de archivos.
"""
# Si es necesario, pip install Werkzeug 
from werkzeug.utils import secure_filename

from app.models.product import Producto
from app.database import init_app, init_db

"""
Crear las dependencias
pip freeze > requirements.txt

Instalar todas las dependencias
pip install -r requirements.txt

"""
d = os.path.dirname(__file__)
os.chdir(d)

ruta_destino ='static/img/'


app = Flask(__name__)
CORS(app)

# Inicializar la base de datos con la aplicación Flask
init_app(app)

@app.route('/init-db')
def init_db_route():
    init_db()
    return "Base de datos inicializada correctamente."



@app.route('/producto', methods=['POST'])
def create_producto():
    print("HOLA")
    # data = request.json
    data = request.form
    print("que hay en data ", data)
    archivo=request.files['imagen']
    print(archivo)
    # Trabajamos con la imagen
    # Utilizamos la función `secure_filename` para obtener un nombre de archivo seguro para la imagen cargada. 
    # Esta función elimina caracteres especiales que podrían causar problemas de seguridad.
    nombre_imagen = secure_filename(archivo.filename)

    print(">>>>>>>>>", nombre_imagen)

    # Separamos el nombre base del archivo y su extensión utilizando `os.path.splitext`.
    # Esto nos permite trabajar con el nombre y la extensión por separado.
    nombre_base, extension = os.path.splitext(nombre_imagen)

    # Generamos un nuevo nombre para el archivo utilizando el nombre base original y 
    # agregando un timestamp para asegurarnos de que el nombre del archivo sea único.
    # Concatenamos el nombre base, un guion bajo, el timestamp actual y la extensión.
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"

    # Guardamos el archivo en la ruta de destino utilizando el nuevo nombre generado.
    # `os.path.join` se asegura de que la ruta sea correcta, sin importar el sistema operativo.
    archivo.save(os.path.join(ruta_destino, nombre_imagen))



    new_producto = Producto(nombre=data['nombre'], precio=data['precio'],  poster_url=nombre_imagen)
    new_producto.save()
    return jsonify({'message': 'Producto creado correctamente 😎'}), 201


@app.route('/producto', methods=['GET'])
def get_all_producto(): #FIJARSE SI ESTA BIEN
    producto = Producto.get_all()
    producto_json=[]
    for p in producto:
         producto_json.append(p.serialize())
    return  producto_json
    # Manera resumida:
    # return jsonify([movie.serialize() for movie in movies])


@app.route('/producto/<int:id>', methods=['GET'])
def get_by_id_producto(id):
    producto = Producto.get_by_id(id)
    if producto:
        return jsonify(producto.serialize())
    else:
        return jsonify({'message': 'Producto no encontrado'}), 404

@app.route('/producto/<int:id>', methods=['DELETE'])
def delete_producto(id):
    producto = Producto.get_by_id(id)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    producto.delete()
    return jsonify({'message': 'El producto fue borrado'})

@app.route('/producto/<int:id>', methods=['PUT'])
def update_producto(id):
    producto = Producto.get_by_id(id)
    if not producto:
        return jsonify({'message': 'Producto no encontrado'}), 404
    data = request.form
    producto.nombre = data.get('nombre', producto.nombre)
    producto.precio = data.get('precio', producto.precio)
   
    # producto.poster_url = data.get('poster_url', producto.poster_url)
    producto.save()
    return jsonify({'message': 'Producto actualizado correctamente 😋'})


if __name__ == '__main__':
     app.run(debug=True)
     #app.run(host='0.0.0.0', port=5000) #ver el puerto