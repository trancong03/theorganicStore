class ProductRepository:
    def __init__(self, neo4j_driver):
        self.neo4j_driver = neo4j_driver

    def get_all_product(self):
        query = """ MATCH(N:Product) RETURN N   """
        try:
            result = self.neo4j_driver.execute_query(query)
            if not result:
                return None
            return [record['N'] for record in result]
        except Exception as e:
            print(f"Error in reset_password: {e}")
            return None
    