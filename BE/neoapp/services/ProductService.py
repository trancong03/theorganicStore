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
    
    def get_product_on_like (self,id_person=None):
        return self.product_repository.get_product_on_like(id_person)
    def add_product_to_like(self, id_product, id_person):
        return self.product_repository.add_product_to_like(id_product,id_person)
    def remove_product_from_like(self, id_product, id_person):
        return self.product_repository.remove_product_from_like(id_product,id_person) 
    def create_delivery_address(self,person_id,recipient_name,phone_number,delivery_address):
        return self.product_repository.create_delivery_address(person_id,recipient_name,phone_number,delivery_address)
    def get_delivery_address(self, id_person=None):
        return self.product_repository.get_delivery_address(id_person)