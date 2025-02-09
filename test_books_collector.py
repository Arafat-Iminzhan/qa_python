import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_successfully_added(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_books_genre()

    def test_add_new_book_not_added_with_invalid_name(self):
        collector = BooksCollector()
        collector.add_new_book("")
        assert "" not in collector.get_books_genre()

    def test_set_book_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_set_book_genre_not_set_with_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Неизвестный жанр")
        assert collector.get_book_genre("Гарри Поттер") == ""

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Властелин Колец")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.set_book_genre("Властелин Колец", "Фантастика")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert len(books) == 2

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert "Гарри Поттер" in favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 0
