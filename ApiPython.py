from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from win10toast_click import ToastNotifier 
import pyperclip

#https://pypi.org/project/win10toast-click/


app = Flask(__name__)
api = Api(app)

codigo_args = reqparse.RequestParser()
codigo_args.add_argument("Codigo", type=str, help="Name of video", required=True) #Help ayuda al sender si envio mal
codigo_args.add_argument("Monto", type=str, help="Views of video", required=True)
codigo_args.add_argument("Date", type=str, help="Likes of video", required=True)

def copyToClipboard(codigo):
    pyperclip.copy(codigo)

class Codigo(Resource):
    def put(self):
        args = codigo_args.parse_args()
        print(args)
        toaster = ToastNotifier()
        toaster.show_toast(
            args["Codigo"], # title
            "Monto: {}\nClick para copiar".format(args["Monto"]), # message 
            icon_path=None, # 'icon_path' 
            duration=10, # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
            callback_on_click=copyToClipboard(args["Codigo"]) # click notification to run function 
        )
    
# Registrar HelloWord como resource, añadelo a la API y determinamos la ruta, en este caso es /helloworld
api.add_resource(Codigo, "/codigo") #Obliga al usuario a escribir un string despues
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
