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
    
    def get_product_on_cart(self, id_person=None):
        query = """ MATCH (p:Person{PersonID:$id_person})-[:ADDED_TO_CART]->(prod:Product)
                    RETURN prod """
        try:
            result = self.neo4j_driver.execute_query(query,  {'id_person': id_person})
            if not result:
                return [] 
            return [record['prod'] for record in result]
        except Exception as e:
            print(f"Error retrieving products from cart: {e}")
            return []      
        
    def add_product_to_Cart(self, id_product, id_person):
        query = """
        MATCH (p:Person {PersonID: $id_person}), (prod:Product {ProductID: $id_product})
        MERGE (p)-[:ADDED_TO_CART]->(prod)
        RETURN p, prod
        """
        parameters = {"id_person": id_person, "id_product": id_product}
        try:
            result = self.neo4j_driver.execute_query(query, parameters)
            if result:
                return {"success": True}  
            else:
                return {"success": False}  
        except Exception as e:
            print(f"Error in add_product_to_Cart: {e}")
            return {"success": False}  
    def remove_product_from_Cart(self, id_product, id_person):
        query = """
        MATCH (p:Person {PersonID: $id_person})-[r:ADDED_TO_CART]->(prod:Product {ProductID: $id_product})
        DELETE r
        RETURN p, prod

        """
        parameters = {"id_person": id_person, "id_product": id_product}
        try:
            result = self.neo4j_driver.execute_query(query, parameters)
            if result:
                return {"success": True}  
            else:
                return {"success": False}  
        except Exception as e:
            print(f"Error in add_product_to_Cart: {e}")
            return {"success": False}  
    # Thêm sản phẩm yêu thích

    def add_product_to_like(self, id_product, id_person):
        query = """
        MATCH (p:Person {PersonID: $id_person}), (prod:Product {ProductID: $id_product})
        MERGE (p)-[:LIKES]->(prod)
        RETURN p, prod
        """
        parameters = {"id_person": id_person, "id_product": id_product}
        try:
            result = self.neo4j_driver.execute_query(query, parameters)
            if result:
                return {"success": True}  
            else:
                return {"success": False}  
        except Exception as e:
            print(f"Error in add_product_to_like: {e}")
            return {"success": False}  
    def get_product_on_like(self, id_person=None):
        query = """ MATCH (p:Person{PersonID:$id_person})-[:LIKES]->(prod:Product)
                    RETURN prod """
        try:
            result = self.neo4j_driver.execute_query(query,  {'id_person': id_person})
            if not result:
                return [] 
            return [record['prod'] for record in result]
        except Exception as e:
            print(f"Error retrieving products from cart: {e}")
            return []      
    def remove_product_from_like(self, id_product, id_person):
        query = """
        MATCH (p:Person {PersonID: $id_person})-[r:LIKES]->(prod:Product {ProductID: $id_product})
        DELETE r
        RETURN p, prod

        """
        parameters = {"id_person": id_person, "id_product": id_product}
        try:
            result = self.neo4j_driver.execute_query(query, parameters)
            if result:
                return {"success": True}  
            else:
                return {"success": False}  
        except Exception as e:
            print(f"Error in add_product_to_Cart: {e}")
            return {"success": False}  
      