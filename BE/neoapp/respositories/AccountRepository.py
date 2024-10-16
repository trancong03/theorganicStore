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
            return None
