class CategoryRepository:
    def __init__(self, neo4j_driver):
        self.neo4j_driver = neo4j_driver
    def get_all_category(self):
        query = """ MATCH(N:Category) RETURN N   """
        try:
            result = self.neo4j_driver.execute_query(query)
            if not result:
                return None
            return [record['N'] for record in result]
        except Exception as e:
            print(f"Error in reset_password: {e}")
            return None  
    def get_product_category(self, id_category=None):
        query = """ MATCH(N:Category{CategoryID:$id_category})<-[:BELONGS_TO]-(p:Product) RETURN p """
        print(f"Fetching products for category ID: {id_category}")

        try:
            result = self.neo4j_driver.execute_query(query,  {'id_category': id_category})
            if not result:
                return [] 
            return [record['p'] for record in result]
        except Exception as e:
            print(f"Error retrieving products from cart: {e}")
            return []      
    def get_product_search(self, product_name=None):
        query = """ MATCH (p:Product)
                    WHERE p.Name CONTAINS $product_name
                    RETURN p """
        print(f"Fetching products for category ID: {product_name}")
        try:
            result = self.neo4j_driver.execute_query(query,  {'product_name': product_name})
            if not result:
                return [] 
            return [record['p'] for record in result]
        except Exception as e:
            print(f"Error retrieving products from cart: {e}")
            return []      