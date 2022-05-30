from flask import request
from flask_restx import Resource, Namespace
from implemented import auth_service
from flask import abort

auth_ns = Namespace('auths')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.get_json()

        name = req_json.get("username")
        password = req_json.get("password")

        if None in [name, password]:
            return "", 400

        tokens = auth_service.generate_tokens(name, password)

        return tokens

    def put(self):
        req_json = request.get_json()

        refresh_token = req_json.get("refresh_token")

        if not auth_service.check_token(refresh_token):
            abort(404)

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201
