# importar la función que devolverá una instancia de una conexión
from config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('users').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de users
        users = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def newuser(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users').query_db( query, data )        

    @classmethod
    def get_one(cls,id):
        print(type(id), id)
        query = "SELECT * FROM users WHERE id = %(id)s;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('users').query_db(query, {"id": id})
        if results:
            user = cls(results[0])  # Crear una instancia de User con el primer resultado
            return user
        else:
            return None
        
    @classmethod
    def edituser(cls, data ):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users').query_db( query, data)        

    @classmethod
    def delete_one_user(cls, id ):
        query = "DELETE FROM users WHERE id = %(id)s;"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users').query_db( query, {"id": id})    