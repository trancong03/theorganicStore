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


