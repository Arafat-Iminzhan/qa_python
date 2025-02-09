import pytest
from main import BooksCollector
from test_data import BOOKS_NAMES_AND_GENRE


@pytest.fixture
def books_collector():
    """Создает новый объект BooksCollector для каждого теста"""
    return BooksCollector()


@pytest.fixture
def add_books(books_collector):
    books = ['Гарри Поттер', 'Властелин Колец', 'Дюна', 'Фантастические твари', 'Звёздные войны']
    for book in books:
        books_collector.add_new_book(book)
    return books


@pytest.fixture
def set_genre(books_collector, add_books):
    genre = "Фантастика"
    for book in add_books:
        books_collector.set_book_genre(book, genre)
