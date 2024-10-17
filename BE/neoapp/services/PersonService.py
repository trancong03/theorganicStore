from neoapp.respositories.PersonRepository import PersonRepository

class PersonService:
    def __init__(self, neo4j_driver):
        self.person_repository = PersonRepository(neo4j_driver)

    def update_person(self, person_id, name=None, email=None, phone=None, address=None, birth_date=None, gender=None):
        updated_person = self.person_repository.update_person(person_id, name, email, phone, address, birth_date, gender)
        if updated_person:
            return{
                'message': 'Person updated successfully',
                'person': {
                    'iduser': person_id,
                    'name': updated_person.get('Name'),
                    'email': updated_person.get('Email'),
                    'phone': updated_person.get('Phone'),
                    'address': updated_person.get('Address'),
                    'birth_date': updated_person.get('BirthDate'),
                    'gender': updated_person.get('Gender'),
                }
            }
        return None

    def get_person(self, person_id):
        return self.person_repository.get_person_by_id(person_id)
    
    def update_avatar_person(self, person_id, avatar=None):
       return self.person_repository.update_avatar_person(person_id,avatar)
        
        