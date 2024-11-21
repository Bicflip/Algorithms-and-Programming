from Domain.domain import Film, Client
from Repository.film_repo import FilmRepository
from Repository.client_repo import ClientRepository


class UI:
    def __init__(self):
        self.film_repo = FilmRepository()
        self.client_repo = ClientRepository()

    def print_menu(self):
        print("\n Alegeti o optiune:")
        print("1. Adauga film")
        print("2. Afiseaza filme")
        print("3. Sterge film")
        print("4. Actualizeaza film")
        print("5. Cauta film dupa ID")
        print("6. Adauga client")
        print("7. Afiseaza clienti")
        print("8. Sterge client")
        print("9. Actualizeaza client")
        print("10. Cauta client dupa ID")
        print("0. Iesire")

    def add_film_ui(self):
        try:
            film_id = int(input("ID film: "))
            title = input("Titlu film: ")
            description = input("Descriere: ")
            genre = input("Gen: ")
            rating = float(input("Rating (0-10): "))

            film = Film(film_id, title, description, genre, rating)
            self.film_repo.add(film)
            print("Film adaugat cu succes!")
        except ValueError as ve:
            print(f"Eroare: {ve}")

    def display_films_ui(self):
        films = self.film_repo.get_all()
        if not films:
            print("Nu exista filme în repo.")
        else:
            print("\n--- Lista Filme ---")
            for film in films:
                print(film)

    def delete_film_ui(self):
        try:
            film_id = int(input("ID-ul filmului de sters: "))
            self.film_repo.remove(film_id)
            print("Film sters cu succes!")
        except ValueError as ve:
            print(f"Eroare: {ve}")

    def update_film_ui(self):
        try:
            film_id = int(input("ID film: "))
            title = input("Titlu nou: ")
            description = input("Descriere noua: ")
            genre = input("Gen nou: ")
            rating = float(input("Rating nou (0-10): "))

            updated_film = Film(film_id, title, description, genre, rating)
            self.film_repo.update(updated_film)
            print("Film actualizat cu succes!")
        except ValueError as ve:
            print(f"Eroare: {ve}")

    def find_film_ui(self):
        try:
            film_id = int(input("ID-ul filmului de cautat: "))
            film = self.repo.find_by_id(film_id)
            if film:
                print("Film gasit:")
                print(film)
            else:
                print("Film inexistent.")
        except ValueError as ve:
            print(f"Eroare: {ve}")

    def add_client_ui(self):
        """Interfață pentru adăugarea unui client."""
        try:
            client_id = int(input("ID client: "))
            name = input("Nume client: ")
            cnp = input("CNP client: ")

            client = Client()
            client.client(client_id, name, cnp)
            self.client_repo.add(client)
            print("Client adăugat cu succes!")
        except ValueError as ve:
            print(f"Eroare: {ve}")

    def display_clients_ui(self):
        """Interfață pentru afișarea clienților."""
        clients = self.client_repo.get_all()
        if not clients:
            print("Nu există clienți în repo.")
        else:
            print("\n--- Lista Clienți ---")
            for client in clients:
                print(client)

    def delete_client_ui(self):
        """Interfață pentru ștergerea unui client."""
        try:
            client_id = int(input("ID-ul clientului de șters: "))
            self.client_repo.remove(client_id)
            print("Client șters cu succes!")
        except ValueError as ve:
            print(f"Eroare: {ve}")

    def update_client_ui(self):
        """Interfață pentru actualizarea unui client."""
        try:
            client_id = int(input("ID client: "))
            name = input("Nume nou: ")
            cnp = input("CNP nou: ")

            updated_client = Client()
            updated_client.client(client_id, name, cnp)
            self.client_repo.update(updated_client)
            print("Client actualizat cu succes!")
        except ValueError as ve:
            print(f"Eroare: {ve}")

    def find_client_ui(self):
        """Interfață pentru căutarea unui client după ID."""
        try:
            client_id = int(input("ID-ul clientului de căutat: "))
            client = self.client_repo.find_by_id(client_id)
            if client:
                print("Client găsit:")
                print(client)
            else:
                print("Client inexistent.")
        except ValueError as ve:
            print(f"Eroare: {ve}")

    def start(self):

        while True:
            self.print_menu()
            try:
                option = int(input("Alege o opțiune: "))
                if option == 1:
                    self.add_film_ui()
                elif option == 2:
                    self.display_films_ui()
                elif option == 3:
                    self.delete_film_ui()
                elif option == 4:
                    self.update_film_ui()
                elif option == 5:
                    self.find_film_ui()
                elif option == 6:
                    self.add_client_ui()
                elif option == 7:
                    self.display_clients_ui()
                elif option == 8:
                    self.delete_client_ui()
                elif option == 9:
                    self.update_client_ui()
                elif option == 10:
                    self.find_client_ui()
                elif option == 0:
                    print("Programul se inchide...")
                    break
                else:
                    print("Optiune invalida.")
            except ValueError:
                print("Te rog sa introduci un numar valid.")

