import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "id": 3,
            "title": 'Джанго освобожденный',
            "description": 'Эксцентричный охотник за головами, также известный как Дантист, '
                           'промышляет отстрелом самых опасных преступников. Работенка пыльная, '
                           'и без надежного помощника ему не обойтись. Но как найти такого и желательно '
                           'не очень дорогого? Освобождённый им раб по имени Джанго – прекрасная кандидатура. '
                           'Правда, у нового помощника свои мотивы – кое с чем надо сперва разобраться.',
            "trailer": 'https://www.youtube.com/watch?v=2Dty-zwcPv4',
            "year": 2012,
            "rating": 8.4,
            "genre_id": 15,
            "director_id": 2
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": 'Джанго освобожденный',
            "description": 'Эксцентричный охотник за головами, также известный как Дантист, '
                           'промышляет отстрелом самых опасных преступников. Работенка пыльная, '
                           'и без надежного помощника ему не обойтись. Но как найти такого и желательно '
                           'не очень дорогого? Освобождённый им раб по имени Джанго – прекрасная кандидатура. '
                           'Правда, у нового помощника свои мотивы – кое с чем надо сперва разобраться.',
            "trailer": 'https://www.youtube.com/watch?v=2Dty-zwcPv4',
            "year": 2012,
            "rating": 8.4,
            "genre_id": 15,
            "director_id": 2
        }
        self.movie_service.update(movie_d)

    def test_update_partial(self):
        movie_d = {
            "title": "Джанго освобожденный"
        }
        self.movie_service.update_partial(movie_d)
