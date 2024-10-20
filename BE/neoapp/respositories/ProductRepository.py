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
        #Địa chỉ nhận hàng
    def create_delivery_address(self,person_id,recipient_name,phone_number,delivery_address):
        create_delivery_address_query = """
            MATCH (p:Person {PersonID: $person_id})
            MERGE (a:Address {DeliveryAddress: $delivery_address})
            ON CREATE SET a.RecipientName = $recipient_name, a.PhoneNumber = $phone_number
            ON MATCH SET a.RecipientName = $recipient_name, a.PhoneNumber = $phone_number
            MERGE (p)-[:DELIVERED_AT]->(a)
            RETURN a
        """
        try:
            result = self.neo4j_driver.execute_query(create_delivery_address_query, {'person_id': person_id,'recipient_name': recipient_name,'phone_number': phone_number,'delivery_address': delivery_address})
            return {"success": True, "delivery_address": result}
        except Exception as e:
            print(f"Error occurred: {e}")
            return {"success": False, "message": str(e)}
        
    def get_delivery_address(self, id_person=None):
            query = """ MATCH (p:Person {PersonID: $person_id})-[:DELIVERED_AT]->(a:Address)
                    RETURN a
                    """
            try:
                result = self.neo4j_driver.execute_query(query,  {'person_id': id_person})
                if not result:
                    return [] 
                return [record['a'] for record in result]
            except Exception as e:
                print(f"Error retrieving products from cart: {e}")
                return []      
            

      