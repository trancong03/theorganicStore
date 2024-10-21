class AdminStoreRepository:
    def __init__(self, neo4j_driver):
        self.neo4j_driver = neo4j_driver

    def add_store(self, id_store, name, address, email, hotline):
        query = """
        CREATE (s:Store {
            StoreID: $id_store,
            Name: $name,
            Address: $address,
            Email: $email,
            Hotline: $hotline
        })
        RETURN s
        """
        parameters = {
            "id_store": id_store,
            "name": name,
            "address": address,
            "email": email,
            "hotline": hotline
        }
        try:
            result = self.neo4j_driver.execute_query(query, parameters)
            return {"success": bool(result)}  # Chuyển đổi kết quả sang boolean để trả về success
        except Exception as e:
            print(f"Error in add_store: {e}")
            return {"success": False, "error": str(e)}

    def get_all_stores(self):
        query = """
        MATCH (s:Store)
        RETURN s.StoreID AS id, 
               s.Name AS name, 
               s.Address AS address, 
               s.Email AS email, 
               s.Hotline AS hotline
        """
        try:
            result = self.neo4j_driver.execute_query(query)
            stores = [
                {
                    "id": record['id'],
                    "name": record['name'],
                    "address": record['address'],
                    "email": record['email'],
                    "hotline": record['hotline']
                }
                for record in result
            ]
            return {"success": True, "data": stores}
        except Exception as e:
            print(f"Error in get_all_stores: {e}")
            return {"success": False, "error": str(e)}
