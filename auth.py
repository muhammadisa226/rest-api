from flask import Flask, request, make_response, jsonify
from flask_restx import Resource, Api
import jwt
import datetime
from functools import wraps
app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = "kode" 

class LoginUser(Resource):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username and password == '12345':
            token = jwt.encode({
                "username":username,
                "exp":datetime.datetime.utcnow() + datetime.timedelta()
                },app.config['SECRET_KEY'],algorithm="HS256"
                               )
            return jsonify({
                "token":token,
                "msg":"anda Berhasil login"
            })
        return jsonify({"msg":"Silakan login !"})
        
api.add_resource(LoginUser,"/api/login", methods=["POST"])

if __name__ == '__main__':
    app.run(debug=True)