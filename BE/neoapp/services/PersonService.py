from neoapp.respositories.PersonRepository import PersonRepository

class PersonService:
    def __init__(self, neo4j_driver):
        self.person_repository = PersonRepository(neo4j_driver)

    def update_person(self, person_id, name=None, email=None, phone=None, address=None, birth_date=None, gender=None):
        return self.person_repository.update_person(person_id, name, email, phone, address, birth_date, gender)

    def get_person(self, person_id):
        return self.person_repository.get_person_by_id(person_id)
