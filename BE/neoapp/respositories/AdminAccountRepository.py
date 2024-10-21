class AdminAccountRepository:
    def __init__(self, neo4j_driver):
        self.neo4j_driver = neo4j_driver

    def add_account(self, id_account, role, username, password):
        query = """
        CREATE (a:Account {
            AccountID: $id_account, 
            Role: $role, 
            Username: $username, 
            Password: $password
        })
        RETURN a;
        """
        parameters = {
            "id_account": id_account,
            "role": role,
            "username": username,
            "password": password
        }
        try:
            result = self.neo4j_driver.execute_query(query, parameters)
            if result:
                return {"success": True}  
            else:
                return {"success": False}  
        except Exception as e:
            print(f"Error in add_account: {e}")
            return {"success": False}  

    def get_all_accounts(self):
        query = """
            MATCH (a:Account)
            RETURN a AS account
        """
        try:
            result = self.neo4j_driver.execute_query(query)
            if result:
                accounts = [record['account'] for record in result]  
                return {
                    "success": True,
                    "data": {
                        "accounts": accounts,
                    }
                }
            else:
                return {"success": False, "data": {"accounts": []}}  
        except Exception as e:
            print(f"Error in get_all_accounts: {e}")
            return {"success": False, "data": {"accounts": []}}  # Returns an empty list on error
