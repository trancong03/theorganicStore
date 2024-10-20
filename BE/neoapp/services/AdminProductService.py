from neoapp.respositories.AdminProductRepository import AdminProductRepository

class AdminProductService:
    def __init__(self, neo4j_driver):
        self.AdminProduct = AdminProductRepository(neo4j_driver)
    def add_product(self, id_product, id_person, image_ids, name, price, unit, origin, expiration_date):
        return self.AdminProduct.add_product(id_product, id_person, image_ids, name, price, unit, origin, expiration_date)
    def get_product_store(self, id_store):
        return self.AdminProduct.get_product_store(id_store)