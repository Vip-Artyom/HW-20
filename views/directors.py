from flask import request, jsonify
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        req_json = request.get_json()
        director_id = req_json["id"]
        director_service.create(req_json)

        responce = jsonify()
        responce.status_code = 201
        responce.headers["Location"] = f"{director_id}"
        return responce


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    def put(self, did):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    def patch(self, did):
        req_json = request.get_json()
        req_json["id"] = did

        director_service.update_partial(req_json)
        return "", 204

    def delete(self, did):
        director_service.delete(did)
        return "", 204
