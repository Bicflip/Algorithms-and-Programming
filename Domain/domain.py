class Film:
    def __init__(self, film_id=0, title='', description='', genre='', rating=0.0):
        self.film_id = film_id
        self.title = title
        self.description = description
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"ID: {self.film_id}, Title: {self.title}, Description: {self.description},\nGen: {self.genre}, Rating: {self.rating}"

    def __eq__(self, other):
        return self.film_id == other.film_id

    def film_create(self):
        self.film_id = 0
        self.title = ''
        self.description = ''
        self.genre = ''
        self.rating = 0

    def film_copy(self, other):
        self.film_id = other.film_id
        self.title = other.title
        self.description = other.description
        self.genre = other.genre
        self.rating = other.rating


class Client:
    def __init__(self):
        self.client_id = 0
        self.name = ''
        self.cnp = ''

    def client(self, client_id, name, cnp):
        self.client_id = client_id
        self.name = name
        self.cnp = cnp

    def copy_client(self, other):
        self.client_id = other.client_id
        self.name = other.name
        self.cnp = other.cnp

    def __str__(self):
        return f"ID: {self.client_id}, Nume: {self.name}, CNP: {self.cnp}"

    def __eq__(self, other):
        return self.client_id == other.client_id


class Rental:
    def __init__(self):
        self.rental_id = 0
        self.film_id = 0
        self.client_id = 0
        self.rented_date = ''
        self.due_date = ''
        self.returned_date = ''

    def rental(self, rental_id, film_id, client_id, rented_date, due_date, returned_date):
        self.rental_id = rental_id
        self.film_id = film_id
        self.client_id = client_id
        self.rented_date = rented_date
        self.due_date = due_date
        self.returned_date = returned_date

    def __str__(self):
        return (f"ID: {self.rental_id}, Film ID: {self.film_id}, Client ID: {self.client_id},\nRented: {self.rented_date},"
                f" Due: {self.due_date}, Returned: {self.returned_date}")

    def __eq__(self, other):
        return self.rental_id == other.rental_id

