class AdminProductRepository:
    def __init__(self, neo4j_driver):
        self.neo4j_driver = neo4j_driver
    def add_product(self, id_product, id_person, image_ids, name, price, unit, origin, expiration_date):
        query = """
        CREATE (p:Product {
            ProductID: $id_product, 
            ImageID: $image_ids, 
            Name: $name, 
            Price: $price, 
            Unit: $unit,
            Origin: $origin, 
            ExpirationDate: $expiration_date
        })
        RETURN p;
        """
        parameters = {
            "id_product": id_product,
            "id_person": id_person,
            "image_ids": image_ids,
            "name": name,
            "price": price,
            "unit": unit,
            "origin": origin,
            "expiration_date": expiration_date
        }
        try:
            result = self.neo4j_driver.execute_query(query, parameters)
            if result:
                return {"success": True}  
            else:
                return {"success": False}  
        except Exception as e:
            print(f"Error in add_product: {e}")
            return {"success": False}  
    
    def get_product_store(self, id_store):
        query = """
            MATCH (p:Product)-[r:AVAILABLE_AT]->(s:Store {StoreID: $id_store})
            RETURN p AS product, r.stock AS stock
        """
        parameters = {
            "id_store": id_store,
        }
        try:
            result = self.neo4j_driver.execute_query(query, parameters)
            if result:
                products = [record['product'] for record in result]  
                stocks = [record['stock'] for record in result]      
                return {
                    "success": True,
                    "data": {
                        "products": products,
                        "stocks": stocks,
                    }
                }
            else:
                return {"success": False, "data": {"products": [], "stocks": []}}  
        except Exception as e:
            print(f"Error in get_product_store: {e}")
            return {"success": False, "data": {"products": [], "stocks": []}}  # Trả về danh sách rỗng khi gặp lỗi
