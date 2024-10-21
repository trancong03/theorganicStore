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
    # Giỏ Hàng
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
        query = """ 
        MATCH (p:Person {PersonID: $id_person})-[:LIKES]->(prod:Product)
        RETURN prod
        """
        try:
            # Thực hiện truy vấn
            result = self.neo4j_driver.execute_query(query, {'id_person': id_person})
            
            if not result or len(result) == 0:
                return []
            return [record['prod'] for record in result]
        
        except Exception as e:
            print(f"Error retrieving liked products: {e}")
            return []  # Trả về mảng rỗng nếu có lỗi

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
            

    def update_delivery_address(self, person_id, old_delivery_address, new_delivery_address, new_recipient_name=None, new_phone_number=None):
        update_delivery_address_query = """
            MATCH (p:Person {PersonID: $person_id})-[:DELIVERED_AT]->(a:Address {DeliveryAddress: $old_delivery_address})
            SET a.DeliveryAddress = $new_delivery_address,
                a.RecipientName = COALESCE($new_recipient_name, a.RecipientName),
                a.PhoneNumber = COALESCE($new_phone_number, a.PhoneNumber)
            RETURN a
        """
        try:
            result = self.neo4j_driver.execute_query(update_delivery_address_query, {
                'person_id': person_id,
                'old_delivery_address': old_delivery_address,
                'new_delivery_address': new_delivery_address,
                'new_recipient_name': new_recipient_name,
                'new_phone_number': new_phone_number
            })
            if not result:
                return {"success": False, "message": "No address found to update."}

            return {"success": True, "updated_address": result}
        except Exception as e:
            print(f"Error occurred: {e}")
            return {"success": False, "message": str(e)}

    def delete_delivery_address(self, person_id, delivery_address):
        try:
            # Xóa tất cả các mối quan hệ liên quan đến địa chỉ
            delete_relationships_query = """
                MATCH (p:Person {PersonID: $person_id})-[r:DELIVERED_AT]->(a:Address {DeliveryAddress: $delivery_address})
                DELETE r
            """
            self.neo4j_driver.execute_query(delete_relationships_query, {
                'person_id': person_id,
                'delivery_address': delivery_address
            })

            delete_address_query = """
                MATCH (a:Address {DeliveryAddress: $delivery_address})
                DELETE a
            """
            self.neo4j_driver.execute_query(delete_address_query, {
                'delivery_address': delivery_address
            })

            return {"success": True, "message": "Delivery address deleted successfully."}
        except Exception as e:
            print(f"Error occurred: {e}")
            return {"success": False, "message": str(e)}
        # 
