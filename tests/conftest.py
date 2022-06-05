from dao.director import DirectorDAO
from dao.model.director import Director
from unittest.mock import MagicMock
import pytest
from dao.genre import GenreDAO
from dao.model.genre import Genre

from dao.movie import MovieDAO
from dao.model.movie import Movie


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


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    comedy = Genre(id=1, name='Комедия')
    family = Genre(id=2, name='Семейный')
    fantasy = Genre(id=3, name='Фэнтези')

    genre_dao.get_one = MagicMock(return_value=comedy)
    genre_dao.get_all = MagicMock(return_value=[comedy, family, fantasy])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    genre_dao.update_partial = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    film_1 = Movie(
        id=1,
        title='Омерзительная восьмерка',
        description='США после Гражданской войны. Легендарный охотник за головами Джон Рут '
                    'по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще '
                    'несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на '
                    'отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, '
                    'ковбой… И один из них - не тот, за кого себя выдает.',
        trailer='https://www.youtube.com/watch?v=lmB9VWm0okU',
        year=2015,
        rating=7.8,
        genre_id=15,
        director_id=2
    )
    film_2 = Movie(
        id=2,
        title='Омерзительная восьмерка',
        description='США после Гражданской войны. Легендарный охотник за головами Джон Рут '
                    'по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько '
                    'путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, '
                    'где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… '
                    'И один из них - не тот, за кого себя выдает.',
        trailer='https://www.youtube.com/watch?v=lmB9VWm0okU',
        year=2015,
        rating=7.8,
        genre_id=15,
        director_id=2
    )
    film_3 = Movie(
        id=3,
        title='Джанго освобожденный',
        description='Эксцентричный охотник за головами, также известный как Дантист, '
                    'промышляет отстрелом самых опасных преступников. Работенка пыльная, и без '
                    'надежного помощника ему не обойтись. Но как найти такого и желательно не очень дорогого? '
                    'Освобождённый им раб по имени Джанго – прекрасная кандидатура. Правда, у нового помощника '
                    'свои мотивы – кое с чем надо сперва разобраться.',
        trailer='https://www.youtube.com/watch?v=2Dty-zwcPv4',
        year=2012,
        rating=8.4,
        genre_id=15,
        director_id=2
    )

    movie_dao.get_one = MagicMock(return_value=film_1)
    movie_dao.get_all = MagicMock(return_value=[film_1, film_2, film_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    movie_dao.update_partial = MagicMock()

    return movie_dao
