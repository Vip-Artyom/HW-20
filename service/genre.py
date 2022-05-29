from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, genre_d):
        return self.dao.create(genre_d)

    def update(self, genre_d):
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
    
    def update_partial(self, data):
        gid = data.get("id")
        genre = self.get_one(gid)

        if "id" in data:
            genre.id = data["id"]
        if "name" in data:
            genre.name = data["name"]

        self.dao.update_partial(genre)
