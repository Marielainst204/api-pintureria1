from app.database import get_db
#from app.models.review import Review

class Producto:
    # Constructor de la clase Producto
    def __init__(self, id_producto=None, nombre=None, precio=None, poster_url=None, reviews=[]):
        self.id_producto = id_producto  # ID del producto, se asigna automáticamente para nuevas películas
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.poster_url = poster_url  # URL del póster del producto
        self.reviews = reviews

        # self.reviews = reviews if reviews is not None else []  # Lista de reseñas asociadas a la película

    # Método para guardar o actualizar un producto en la base de datos
    def save(self):
        db = get_db()  # Obtener la conexión a la base de datos
        cursor = db.cursor()
        if self.id_producto:
            # Si el producto ya tiene un ID, se actualiza su registro en la base de datos
            cursor.execute("""
                UPDATE productos SET nombre = %s, precio = %s, poster_url = %s
                WHERE id_producto = %s
            """, (self.nombre,self.precio, self.poster_url, self.id_producto))
        else:
            # Si el producto no tiene un ID, se inserta un nuevo registro en la base de datos
            cursor.execute("""
                INSERT INTO productos (nombre, precio, poster_url) VALUES (%s, %s, %s)
            """, (self.nombre,self.precio,self.poster_url))
            self.id_producto = cursor.lastrowid  # Obtener el ID asignado por la base de datos
        db.commit()  # Confirmar la transacción
        cursor.close()

    # Método estático para obtener todas los productos con sus reseñas de la base de datos
    @staticmethod
    def get_all():
        """
        Retorna un listado de OBJETOS Producto, cada uno con sus reseñas.
        """
        db = get_db()  # Obtener la conexión a la base de datos
        cursor = db.cursor()
        cursor.execute("""
            SELECT 
                p.id_producto, p.nombre, p.precio, m.poster_url,
               # r.id_review, r.reviewer_name, r.comment, 
            FROM 
               Productos p
            LEFT JOIN 
                reviews r ON p.id_producto = r.id_producto
        """)  # Ejecutar la consulta para obtener todaslos productos con sus reseñas
        rows = cursor.fetchall()  # Obtener todos los resultados
        
        productos_dict = {}
        
        for row in rows:
            id_producto = row[0]
            if id_producto not in productos_dict:
                productos_dict[id_producto] = Producto(
                    id_producto=row[0], nombre=row[1], precio=row[2], poster_url=row[3],  reviews=[]
                )
            #  if row[5] is not None:
            #      review = Review(
            #         id_review=row[5], id_product=row[0], reviewer_name=row[6], comment=row[7], #DUDA SI VA ESO
            #     )
                # productos_dict[id_producto].reviews.append(review)

        cursor.close()
        return list(productos_dict.values())  # Devolver la lista de PRODUCTOS con sus reseñas

    @staticmethod
    def get_by_id(producto_id):
        db = get_db()
        cursor = db.cursor()

        # Ejecutar la consulta con JOIN para obtenerel producto y sus reseñas
        #CREO QUE NO ES NECESARIO
        cursor.execute("""
            SELECT   
                p.id_producto, p.nombre, p.precio, p.poster_url,
                r.id_review, r.reviewer_name, r.comment, r.rating
            FROM 
               productos p
            LEFT JOIN 
                reviews r ON m.id_producto = r.id_producto
            WHERE 
                p.id_producto = %s
        """, (producto_id,))
        
        rows = cursor.fetchall()
        cursor.close()

        if rows:
            # Utilizamos un diccionario para mapear los productos por su ID para evitar duplicados
            producto_map = {}
            for row in rows:
                if row[0] not in producto_map:
                    # Si el producto aún no está en el mapeo, la añadimos con sus datos básicos
                    producto_map[row[0]] = Producto(id_producto=row[0],nombre=row[1],precio=row[2], poster_url=row[3],reviews=[])

                # Añadir la reseña si existe (puede ser None si no hay reseñas asociadas)
                #NO LO VEO NECESARIO
                #if row[5] is not None:
                    #review = Review(id_review=row[5], id_movie=row[0], reviewer_name=row[6], comment=row[7], rating=row[8])
                    #movie_map[row[0]].reviews.append(review)

            # Devolver EL PRODUCTO encontrada por su ID
            return producto_map[producto_id]

        return None  # Si no se encontró el producto, devolver None
    # Método para eliminar un producto de la base de datos
    def delete(self):
        db = get_db()  # Obtener la conexión a la base de datos
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (self.id_producto,))  # Ejecutar la consulta para eliminar el producto
        db.commit()  # Confirmar la transacción
        cursor.close()

    # Método para serializar un objeto Product a un diccionario
    def serialize(self):
        return {
            'id_producto': self.id_producto,  # ID del producto
            'nombre': self.nombre,  # Nombre del producto
            'precio': self.precio,  # Precio del producto
            'poster_url': self.poster_url,  # URL del póster del producto
            #'reviews': [review.serialize() for review in self.reviews]  # Lista de reseñas serializadas
        }

    def __str__(self):
        return f"PRODUCTO: {self.id_producto} - {self.nombre} - {self.precio}"
