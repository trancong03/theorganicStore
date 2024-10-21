from neoapp.respositories.AdminStoreRepository import AdminStoreRepository

class AdminProductService:
    def __init__(self, neo4j_driver):
        self.admin_store_repository = AdminStoreRepository(neo4j_driver)
    
    def add_store(self, id_store, name, address, email, hotline):
        return self.admin_store_repository.add_store(id_store, name, address, email, hotline)
    
    def get_all_stores(self):
        return self.admin_store_repository.get_all_stores(self)
