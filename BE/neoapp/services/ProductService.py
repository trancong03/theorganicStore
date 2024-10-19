from neoapp.respositories.ProductRepository import ProductRepository

class ProductService:
    def __init__(self, neo4j_driver):
        self.product_repository = ProductRepository(neo4j_driver)
    def get_all_product(self):
        return self.product_repository.get_all_product()
    
    def get_product_on_cart (self,id_person=None):
        return self.product_repository.get_product_on_cart(id_person)
    
    
    def add_product_to_Cart(self, id_product, id_person):
        return self.product_repository.add_product_to_Cart(id_product,id_person) 
    def remove_product_from_Cart(self, id_product, id_person):
        return self.product_repository.remove_product_from_Cart(id_product,id_person) 