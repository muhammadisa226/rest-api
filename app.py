from flask import Flask, request
from flask_restx import Resource, Api
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
CORS(app)

#Inisiasi variabel kosong bertipe dictionary ,dictyonary = json
identitas ={}

#membuat class resource
class ContohResource(Resource):
    def get(self):
        # response = {"msg": "Hello world"}
        return identitas
    def post(self):
        nama = request.form['nama']
        umur = request.form['umur']
        identitas['nama'] = nama
        identitas['umur'] = umur
        response = {'msg' : 'data berhasil masuk'}
        return response

api.add_resource(ContohResource,"/api", methods=["GET","POST"])

if __name__ == '__main__':
    app.run(debug=True,port=5005)