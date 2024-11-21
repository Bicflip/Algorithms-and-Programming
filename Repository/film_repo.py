
class FilmRepository:
    def __init__(self):
        self.films = []

    def add(self, film):
        if film in self.films:
            raise ValueError("Entitatea exista deja.")
        self.films.append(film)

    def remove(self, film_id):
        for entity in self.films:
            if entity.film_id == film_id:
                self.films.remove(entity)
                return
        raise ValueError("Entitatea cu ID-ul specificat nu exista.")

    def update(self, updated_entity):
        for index, entity in enumerate(self.films):
            if entity.film_id == updated_entity.film_id:
                self.films[index] = updated_entity
                return
        raise ValueError("Entitatea cu ID-ul specificat nu exista.")

    def get_all(self):
        return self.films

    def find_by_id(self, entity_id):
        for entity in self.films:
            if entity.film_id == entity_id:
                return entity
        return None
