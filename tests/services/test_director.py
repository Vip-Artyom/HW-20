from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    dexter = Director(id=4, name='Декстер Флетчер')
    steve = Director(id=5, name='Стив Энтин')
    rob = Director(id=6, name='Роб Маршалл')

    director_dao.get_one = MagicMock(return_value=dexter)
    director_dao.get_all = MagicMock(return_value=[dexter, steve, rob])
    director_dao.create = MagicMock(return_value=Director(id=6))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    director_dao.update_partial = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "name": "Ivan",
            "id": 39
        }
        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "Ivan"
        }
        self.director_service.update(director_d)

    def test_update_partial(self):
        director_d = {
            "name": "Ivan"
        }
        self.director_service.update_partial(director_d)
