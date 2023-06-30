#import json
#import time
#from flask import Flask
#import flask
#
#
#from flask_restful import Resource, reqparse
#from flask import Flask
#from werkzeug.security import safe_str_cmp
#
##from models.user import UserModel
#
#
##Toook out parser
#
#class UserRegister(Resource):
#    def post(self):#from yasoob
#        data = _user_parser.parse_args()
#
#        if UserModel.find_by_username(data['username']):
#            return {"message": "A user with that username already exists"}, 400
#
#        user = UserModel(**data)
#        user.save_to_db()
#
#        return {"message": "User created successfully."}, 201
#
#class User(Resource):
#    def post(self):
#        """
#        $ curl http://localhost:5000/api/login -X POST \
#        -d '{"username":"Yasoob","password":"strongpassword"}'
#        """
#        req = flask.request.get_json(force=True)
#        username = req.get('username', None)
#        password = req.get('password', None)
#        user = guard.authenticate(username, password)
#        ret = {'access_token': guard.encode_jwt_token(user)}
#        return ret, 200
#    def get(self):
#        return ("hello")
#    
#
#
#
#
#class Time(Resource):
#    #Can we have different functions depending on the type of request
#    def get(self):
#        print(type ({'time':time.time()}))
#        return {'time': time.time()}
## INteresting
#   
##    user = guard.authenticate(username, password)
##    ret = {'access_token': guard.encode_jwt_token(user)}
#
#class UserLogin(Resource):
#    def post(self):
#        """
#        Logs a user in by parsing a POST request containing user credentials and
#        issuing a JWT token.
#        .. example::
#        $ curl http://localhost:5000/api/login -X POST \
#        -d '{"username":"Yasoob","password":"strongpassword"}'
#        """
#        req = flask.request.get_json(force=True)
#        username = req.get('username', None)
#        password = req.get('password', None)
#        user = guard.authenticate(username, password)
#        ret = {'access_token': guard.encode_jwt_token(user)}
#        return ret, 200
#
#
#
##class UserLogin(Resource):
##    def post(self):
##        #data = _user_parser.parse_args()
##        #user = UserModel.find_by_username(data['username'])
##        #J: I modified these to just return json strings, but we might go back to returning
##        #"Responses" later one
##
##        # this is what the `authenticate()` function did in security.py
##        if user and safe_str_cmp(user.password, data['password']):
##            # identity= is what the identity() function did in security.py—now stored in the JWT
##            #J: Maybe I don't need these in here just huh?
##            req = flask.request.get_json(force=True)
##            username = req.get('username', None)
##            password = req.get('password', None)
##            user = guard.authenticate(username, password)
##            guard.authenticate(username,password)
##            access_token = guard.encode_jwt_token()
##            refresh_token = create_refresh_token(user.id)
##            return json.dumps({
##                'access_token': access_token,
##                'refresh_token': refresh_token
##            }, 200)
##
##        return json.dumps({"message": "Invalid Credentials!"}, 401)
#
#
##class UserLogout(Resource):
##    @flask_praetorian.auth_required
##    def post(self):
##        jti = guard.extract_jwt_token(token)
##        BLACKLIST.add(jti)
##        return {"message": "Successfully logged out"}, 200
#
#
##class TokenRefresh(Resource):
# #    @flask_praetorian.auth_required(refresh=True)
##    def post(self):
##        current_user = 
##        new_token = create_access_token(identity=current_user, fresh=False)
##        return {'access_token': new_token}, 200
#
