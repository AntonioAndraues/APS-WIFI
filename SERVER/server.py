from flask import Flask, request,g,render_template
from flask_restful import Resource, Api
import datetime
import os

app = Flask(__name__,template_folder='template')
api = Api(app)

todos = {}
Is_on=0
Analog=0
ID=""
class On(Resource):
    def get(self):
        global ID, Is_on, Analog
        currentDT = datetime.datetime.now()
        ID =request.args.get('id')
        Is_on =request.args.get('digital') 
        Analog=request.args.get('analogico')

        print("ID   : {0}\n".format(ID))
        print("BOTAO  : {0}\n".format(Is_on))
        print("Analogico  : {0}\n".format(Analog))
        print (str(currentDT))
        return {'ID':ID,'Device': Is_on,'Analogico: ': Analog,'TempoLocal':str(currentDT)}

class view(Resource):
    def get(self):
        return render_template('hello.html', name = "teste")
#class TodoSimple(Resource):
#    def get(self, todo_id):
#        return {todo_id: todos[todo_id]}
#
#    def put(self, todo_id):
#        todos[todo_id] = request.form['data']
#        return {todo_id: todos[todo_id]}

#api.add_resource(TodoSimple, '/<string:todo_id>')
#for i in Id_ativados:
#    print(i)
api.add_resource(On, '/')
api.add_resource(view,'/view/')



@app.route('/index/')
def hello_name():
    dicionario={'digital':Is_on,'analogico':Analog,'id':ID}
    return render_template('index.html',dicionario=dicionario)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',debug=True,port=port)
    #app.run(debug=True)

