import pytest
from test_data import BOOKS_NAMES_AND_GENRE
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('name', ['', 'Странная история доктора Джекила и мистера Хайда'])
    def test_add_new_book_not_added_with_invalid_name(self, name, books_collector):
        books_collector.add_new_book(name)
        assert name not in books_collector.get_books_genre()

    @pytest.mark.parametrize('genre_and_expected', [['Фантастика', 'Фантастика'], ['Криминал', '']])
    def test_set_book_genre_1_set_and_1_not_set(self, books_collector, genre_and_expected):
        genre, expected_result = genre_and_expected
        name = 'Гордость и предубеждение и зомби'

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)

        genre_added = books_collector.get_book_genre(name)

        assert genre_added == expected_result

    def test_get_book_genre_return_genre_by_name(self, books_collector):
        name = 'Гордость и предубеждение и зомби'
        books_collector.add_new_book(name)

        assert books_collector.get_book_genre(name) == ''

    def test_get_books_with_specific_genre_returned_5(self, books_collector):
        genre = 'Фантастика'

        # ✅ Добавляем 5 книг
        books = ['Гарри Поттер', 'Властелин Колец', 'Дюна', 'Фантастические твари', 'Звёздные войны']
        for book in books:
            books_collector.add_new_book(book)
            books_collector.set_book_genre(book, genre)

        returned_books_list = books_collector.get_books_with_specific_genre('Фантастика')

        assert len(returned_books_list) == 5

    def test_get_books_genre_dict_books_genre_returned(self, books_collector):
        books_collector.add_new_book('Гарри Поттер')
        books_collector.set_book_genre('Гарри Поттер', 'Фантастика')

        expected_books_genre_dict = {'Гарри Поттер': 'Фантастика'}
        returned_books_genre_dict = books_collector.get_books_genre()

        assert returned_books_genre_dict == expected_books_genre_dict

    def test_get_books_for_children_return_non_rating_books(self, books_collector):
        books_genre_data = {
            'Гарри Поттер и философский камень': 'Фантастика',
            'Винни-Пух': 'Мультфильмы',
            'Автостопом по галактике': 'Фантастика'
        }

        # ✅ Добавляем книги и устанавливаем жанры
        for book, genre in books_genre_data.items():
            books_collector.add_new_book(book)
            books_collector.set_book_genre(book, genre)

        expected_books = ['Гарри Поттер и философский камень', 'Винни-Пух', 'Автостопом по галактике']
        returned_books = books_collector.get_books_for_children()

        assert returned_books == expected_books

    def test_add_book_in_favorites_not_added_book(self, books_collector):
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        list_books = books_collector.get_list_of_favorites_books()

        assert len(list_books) == 0

    def test_add_book_in_favorites_not_added_in_favorites_if_name_is_name(self, books_collector):
        books_collector.add_new_book('Убийство в Восточном экспрессе')

        books_collector.add_book_in_favorites('Убийство в Восточном экспрессе')
        books_collector.add_book_in_favorites('Убийство в Восточном экспрессе')

        list_books = books_collector.get_list_of_favorites_books()

        assert len(list_books) == 1

    def test_delete_book_from_favorites_not_deleted_book_with_invalid_name(self, books_collector):
        books_collector.add_new_book('Гордость и предубеждение и зомби')

        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        books_collector.delete_book_from_favorites('Автостопом по галактике')

        list_books = books_collector.get_list_of_favorites_books()

        assert len(list_books) == 1

    def test_delete_book_from_favorites_book_deleted(self, books_collector):
        books_collector.add_new_book('Гордость и предубеждение и зомби')

        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        books_collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        list_books = books_collector.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' not in list_books

    def test_get_list_of_favorites_books_list_returned(self, books_collector):
        for book in ['Гарри Поттер', 'Властелин Колец']:
            books_collector.add_new_book(book)
            books_collector.add_book_in_favorites(book)

        returned_list = books_collector.get_list_of_favorites_books()
        expected_list = ['Гарри Поттер', 'Властелин Колец']

        assert returned_list == expected_list
