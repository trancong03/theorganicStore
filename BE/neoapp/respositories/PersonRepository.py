class PersonRepository:
    def __init__(self, neo4j_driver):
        self.neo4j_driver = neo4j_driver

    def get_person_by_id(self, person_id):
        query = """
            MATCH (p:Person {PersonID: $person_id})
            RETURN p
        """
        try:
            result = self.neo4j_driver.execute_query(query, {'person_id': person_id})
            if not result:
                return None
            return result[0]['p']  # Trả về đối tượng Person
        except Exception as e:
            print(f"Error in get_person_by_id: {e}")
            return None

    def update_person(self, person_id, name=None, email=None, phone=None, address=None, birth_date=None, gender=None):
        query = """
            MATCH (p:Person{PersonID: $person_id})
            SET p.Name = COALESCE($name, p.Name),
                p.Email = COALESCE($email, p.Email),
                p.Phone = COALESCE($phone, p.Phone),
                p.Address = COALESCE($address, p.Address),
                p.BirthDate = COALESCE($birth_date, p.BirthDate),
                p.Gender = COALESCE($gender, p.Gender)
            RETURN p
        """
        try:
            parameters = {
                'person_id': person_id,
                'name': name,
                'email': email,
                'phone': phone,
                'address': address,
                'birth_date': birth_date,
                'gender': gender,
            }
            result = self.neo4j_driver.execute_query(query, parameters)
            if not result:
                return None
            return result[0]['p']
        except Exception as e:
            print(f"Error in update_person: {e}")
            return None
