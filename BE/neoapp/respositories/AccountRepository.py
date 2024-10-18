class AccountRepository:
    def __init__(self, neo4j_driver):
        self.neo4j_driver = neo4j_driver

    def get_account_by_credentials(self, username, password):
        query = """
                MATCH (a:Account {Username: $username, Password: $password})<-[:HAS_ACCOUNT]-(p:Person)
                RETURN a, p
                """
        try:
            result = self.neo4j_driver.execute_query(query, {'username': username, 'password': password})
            if not result:
                return None
            return result
        except Exception as e:
            print(f"Error in reset_password: {e}")
            return None
        
    def check_username_exists(self, username):
        query = """ MATCH (a:Account {Username: $username}) RETURN a """
        try:
            result = self.neo4j_driver.execute_query(query, {'username': username})
            return len(result) > 0  
        except Exception as e:
            return False
    
    def get_new_person_id(self):
        query = """ MATCH (p:Person) RETURN MAX(p.PersonID) AS max_person_id """
        result = self.neo4j_driver.execute_query(query)
        max_person_id = result[0]['max_person_id'] if result and result[0]['max_person_id'] is not None else 0
        return max_person_id + 1  

    def get_new_account_id(self):
        query = """ MATCH (a:Account) RETURN MAX(a.AccountID) AS max_account_id """
        result = self.neo4j_driver.execute_query(query)
        max_account_id = result[0]['max_account_id'] if result and result[0]['max_account_id'] is not None else 0
        return max_account_id + 1 

    def create_person_and_account(self, name, email, phone, username, password, admin):
        if self.check_username_exists(username):
            return {"success": False, "message": "Tên người dùng đã tồn tại."}
        person_id = self.get_new_person_id()  
        account_id = self.get_new_account_id()  
        create_person_query = """CREATE (p:Person { PersonID: $person_id, Name: $name, Phone: $phone, Email: $email,Address: null,BirthDate: null, Gender: null }) RETURN p """
        role = 'Admin' if admin else 'Customer' 
        create_account_query = """
            MATCH (p:Person {PersonID: $person_id}) 
            CREATE (a:Account {
                AccountID: $account_id,
                Username: $username,
                Password: $password,
                Role: $role  
            })
            CREATE (p)-[:HAS_ACCOUNT]->(a)  
            RETURN a
        """
        try:
            self.neo4j_driver.execute_query(create_person_query, {'person_id': person_id,'name': name,'phone': phone,'email': email})
            result = self.neo4j_driver.execute_query(create_account_query, {'username': username,'password': password,'account_id': account_id,'person_id': person_id,'role': role})
            return {"success": True, "account": result}
        except Exception as e:
            print(f"Error occurred: {e}")
            return {"success": False, "message": str(e)}
        

    def reset_password(self,username,old_password,new_password):
        account = self.get_account_by_credentials(username,old_password)
        if account:
            query = """
                MATCH (a:Account {Username: $username})
                SET a.Password = $new_password
                RETURN a
            """
            try:
                result = self.neo4j_driver.execute_query(query, {'username': username, 'new_password': new_password})
                if not result:
                    return None
                return result[0]['a']  
            except Exception as e:
                print(f"Error in reset_password: {e}")
                return None
        else:
            return None         
