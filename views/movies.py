from flask import request, jsonify
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_service.get_all()
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200

    def post(self):
        req_json = request.get_json()
        movie_id = req_json["id"]
        movie_service.create(req_json)

        responce = jsonify()
        responce.status_code = 201
        responce.headers["Location"] = f"{movie_id}"
        return responce


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        b = movie_service.get_one(mid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    def put(self, mid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = mid
        movie_service.update(req_json)
        return "", 204

    def patch(self, mid):
        req_json = request.get_json()
        req_json["id"] = mid

        movie_service.update_partial(req_json)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204
