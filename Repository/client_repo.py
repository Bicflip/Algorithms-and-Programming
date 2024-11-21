
class ClientRepository:
    def __init__(self):
        self.clients = []

    def add(self, client):
        if client in self.clients:
            raise ValueError("Entitatea exista deja.")
        self.clients.append(client)

    def remove(self, client_id):
        for entity in self.clients:
            if entity.client_id == client_id:
                self.clients.remove(entity)
                return
        raise ValueError("Entitatea cu ID-ul specificat nu exista.")

    def update(self, updated_entity):
        for index, entity in enumerate(self.clients):
            if entity.client_id == updated_entity.client_id:
                self.clients[index] = updated_entity
                return
        raise ValueError("Entitatea cu ID-ul specificat nu exista.")

    def get_all(self):
        return self.clients

    def find_by_id(self, entity_id):
        for entity in self.clients:
            if entity.client_id == entity_id:
                return entity
        return None
