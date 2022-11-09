from flask import Flask, request
from flask_restx import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os 
app = Flask(__name__)
api = Api(app)
CORS(app)
#INISIALISAI object sqlachemy
db = SQLAlchemy(app)
#konfigurasi database
basedir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///" + os.path.join(basedir,"db.sqlite")
app.config["SQLALCHEMY_DATABASE_URI"] = database

#buat model database
class Mahasiswa(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nim = db.Column(db.Integer,unique=True)
    nama = db.Column(db.String(100))
    umur = db.Column(db.Integer)
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

#mencreate database
db.create_all()

#membuat class resource
class CreateRead(Resource):
    def get(self):
        query = Mahasiswa.query.all()
        mahasiswa = [{
            'id':data.id,
            'nim':data.nim,
            'nama':data.nama,
            'umur':data.umur
        }
        for data in query
    ]
        return mahasiswa;
        
    def post(self):
        datanim = request.form['nim']
        datanama = request.form['nama']
        dataumur = request.form['umur']
        model = Mahasiswa(nim=datanim, nama=datanama, umur=dataumur)
        model.save()
        response = {'msg' : 'data berhasil masuk'}
        return response
    def delete(self):
        query = Mahasiswa.query.all()
        for data in query:
            db.session.delete(data)
            db.session.commit()
        response ={
            'msg':'Semua Data Berhasil Dihapus'
        }
        return response
class UpdateDelete(Resource):
    def put(self,id):
        query = Mahasiswa.query.get(id)
        editNim = request.form['nim']
        editNama = request.form['nama']
        editUmur = request.form['umur']
        query.nim = editNim
        query.nama = editNama
        query.umur = editUmur
        db.session.commit()
        response = {
            'msg':'edit data berhasil',
            'code': 200
        }
        return response
    def delete(self,id):
         querydata = Mahasiswa.query.get(id)
         db.session.delete(querydata)
         db.session.commit()
         
         response = {
             'msg':'hapus data berhasil'
         }
         return response
api.add_resource(CreateRead,"/api", methods=["GET","POST","DELETE"])
api.add_resource(UpdateDelete,"/api/<id>", methods=["PUT","DELETE"])

if __name__ == '__main__':
    app.run(debug=True)