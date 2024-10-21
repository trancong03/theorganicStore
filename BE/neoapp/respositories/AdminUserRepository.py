class AdminUserRepository:
    def __init__(self, neo4j_driver):
        self.neo4j_driver = neo4j_driver
    
    def add_user(self, id_person, name, address, phone, birth, gender):
        query = """
        CREATE (u:User {
            PersonID: $id_person, 
            Name: $name, 
            Address: $address, 
            Phone: $phone, 
            Birth: $birth,
            Gender: $gender
        })
        RETURN u;
        """
        parameters = {
            "id_person": id_person,
            "name": name,
            "address": address,
            "phone": phone,
            "birth": birth,
            "gender": gender
        }
        try:
            result = self.neo4j_driver.execute_query(query, parameters)
            if result:
                return {"success": True}  
            else:
                return {"success": False}  
        except Exception as e:
            print(f"Error in add_user: {e}")
            return {"success": False}  
    
    def get_all_users(self):
        query = """
            MATCH (u:User)
            RETURN u AS user
        """
        try:
            result = self.neo4j_driver.execute_query(query)
            if result:
                users = [record['user'] for record in result]  
                return {
                    "success": True,
                    "data": {
                        "users": users,
                    }
                }
            else:
                return {"success": False, "data": {"users": []}}  
        except Exception as e:
            print(f"Error in get_all_user: {e}")
            return {"success": False, "data": {"users": []}}  
