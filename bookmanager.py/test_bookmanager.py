import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):

    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        """Test menambahkan buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(book)
        self.assertIn(book, self.book_manager.get_all_books())

    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)
        removed = self.book_manager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertNotIn(book, self.book_manager.get_all_books())

    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        removed = self.book_manager.remove_book("Buku Tidak Ada")
        self.assertFalse(removed)

    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author"""
        book1 = Book("Pemrograman Python", "Andi", 2020)
        book2 = Book("Pemrograman Java", "Budi", 2021)
        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        result = self.book_manager.find_books_by_author("Andi")
        self.assertIn(book1, result)
        self.assertNotIn(book2, result)

    def test_get_all_books(self):
        """Test mendapatkan semua buku"""
        book1 = Book("Pemrograman Python", "Andi", 2020)
        book2 = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        books = self.book_manager.get_all_books()
        self.assertEqual(len(books), 2)
        self.assertIn(book1, books)
        self.assertIn(book2, books)

if __name__ == "_main_":
    unittest.main(verbosity=2)