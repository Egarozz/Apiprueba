from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# HelloWorld Hereda a Resource y este Resource puede handlear un get request, delete, etc.
class HelloWorld(Resource):
    def get(self): # Cuando un get request se retornara un diccionario "Hello World"
        return {"data":"Hello World"}
    
# Registrar HelloWord como resource, añadelo a la API y determinamos la ruta, 
# en este caso es /helloworld
api.add_resource(HelloWorld, "/helloworld")
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)