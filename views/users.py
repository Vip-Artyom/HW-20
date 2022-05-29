from flask import request, jsonify
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):        
        all_users = user_service.get_all()
        res = UserSchema(many=True).dump(all_users)
        return res, 200

    def post(self):
        req_json = request.get_json()
        user_id = req_json["id"]
        user_service.create(req_json)

        responce = jsonify()
        responce.status_code = 201
        responce.headers["Location"] = f"{user_id}"
        return responce


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        u = user_service.get_one(uid)
        user = UserSchema().dump(u)
        return user, 200

    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def patch(self, uid):
        req_json = request.get_json()
        req_json["id"] = uid

        user_service.update_partial(req_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
