class PersonRepository:
    def __init__(self, neo4j_driver):
        self.neo4j_driver = neo4j_driver

    def get_new_userid(self):
        query = """
            MATCH (p:Person)
            RETURN MAX(p.PersonID) AS max_id
        """
        try:
            result = self.neo4j_driver.execute_query(query)
            max_id = result[0]['max_id'] if result and result[0]['max_id'] is not None else 0
            return max_id + 1  # Tạo userid mới bằng max_id + 1
        except Exception as e:
            return None  # Trả về None nếu có lỗi
   
    def update_person(self, person_id, name=None, email=None, phone=None, address=None, birth_date=None, gender=None):
        query = """
            MATCH (p:Person {PersonID: $person_id})
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
            print(f"Result from Neo4j: {result}")
            if not result:
                return None
            return result[0]['p']
        except Exception as e:
            print(f"Error in update_person: {e}")
            return None

    def update_avatar_person(self, person_id, avatar=None):
        query = """
            MATCH (p:Person {PersonID: $person_id})
            SET p.Avatar = COALESCE($avatar, p.Avatar)
            RETURN p
        """       
        try:
            parameters = {
                'person_id': person_id,
                'avatar': avatar
            }
            result = self.neo4j_driver.execute_query(query, parameters)
            if not result:
                return None
            return result[0]['p']
        except Exception as e:
            print(f"Error in update_avatar_person: {e}")
            return None
