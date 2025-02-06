from main import BooksCollector

def test_add_new_book_successfully_added():
    collector = BooksCollector()
    collector.add_new_book("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_books_genre()
