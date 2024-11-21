import unittest
from Domain.domain import Film, Client, Rental
from Repository.film_repo import FilmRepository
from Repository.client_repo import ClientRepository


class TestFilmRepository(unittest.TestCase):
    def setUp(self):
        self.repo = FilmRepository()
        self.film = Film(1, "Inception", "A mind-bending thriller", "Sci-Fi", 9.0)

    def test_add(self):
        self.repo.add(self.film)
        self.assertIn(self.film, self.repo.get_all())

    def test_add_existing_film(self):
        self.repo.add(self.film)
        with self.assertRaises(ValueError):
            self.repo.add(self.film)

    def test_remove(self):
        self.repo.add(self.film)
        self.repo.remove(1)
        self.assertNotIn(self.film, self.repo.get_all())

    def test_remove_nonexistent_film(self):
        with self.assertRaises(ValueError):
            self.repo.remove(999)

    def test_update(self):
        self.repo.add(self.film)
        updated_film = Film(1, "Interstellar", "A space epic", "Sci-Fi", 8.5)
        self.repo.update(updated_film)
        self.assertEqual(self.repo.find_by_id(1).title, "Interstellar")

    def test_update_nonexistent_film(self):
        with self.assertRaises(ValueError):
            self.repo.update(Film(999, "Nonexistent", "N/A", "N/A", 0))

    def test_find_by_id(self):
        self.repo.add(self.film)
        self.assertEqual(self.repo.find_by_id(1), self.film)

    def test_find_by_id_nonexistent(self):
        self.assertIsNone(self.repo.find_by_id(999))


class TestClientRepository(unittest.TestCase):
    def setUp(self):
        self.repo = ClientRepository()
        self.client = Client()
        self.client.client(1, "John Doe", "1234567890123")

    def test_add(self):
        self.repo.add(self.client)
        self.assertIn(self.client, self.repo.get_all())

    def test_add_existing_client(self):
        self.repo.add(self.client)
        with self.assertRaises(ValueError):
            self.repo.add(self.client)

    def test_remove(self):
        self.repo.add(self.client)
        self.repo.remove(1)
        self.assertNotIn(self.client, self.repo.get_all())

    def test_remove_nonexistent_client(self):
        with self.assertRaises(ValueError):
            self.repo.remove(999)

    def test_update(self):
        self.repo.add(self.client)
        updated_client = Client()
        updated_client.client(1, "Jane Doe", "9876543210987")
        self.repo.update(updated_client)
        self.assertEqual(self.repo.find_by_id(1).name, "Jane Doe")

    def test_update_nonexistent_client(self):
        with self.assertRaises(ValueError):
            updated_client = Client()
            updated_client.client(999, "Nonexistent", "0000000000000")
            self.repo.update(updated_client)

    def test_find_by_id(self):
        self.repo.add(self.client)
        self.assertEqual(self.repo.find_by_id(1), self.client)

    def test_find_by_id_nonexistent(self):
        self.assertIsNone(self.repo.find_by_id(999))


class TestRental(unittest.TestCase):
    def test_rental_creation(self):
        rental = Rental()
        rental.rental(1, 1, 1, "2024-01-01", "2024-01-10", "")
        self.assertEqual(rental.rental_id, 1)
        self.assertEqual(rental.film_id, 1)
        self.assertEqual(rental.client_id, 1)
        self.assertEqual(rental.rented_date, "2024-01-01")
        self.assertEqual(rental.due_date, "2024-01-10")
        self.assertEqual(rental.returned_date, "")

    def test_rental_equality(self):
        rental1 = Rental()
        rental1.rental(1, 1, 1, "2024-01-01", "2024-01-10", "")
        rental2 = Rental()
        rental2.rental(1, 1, 1, "2024-01-01", "2024-01-10", "")
        self.assertEqual(rental1, rental2)



