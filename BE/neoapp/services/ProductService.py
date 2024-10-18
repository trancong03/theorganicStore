from neoapp.respositories.ProductRepository import ProductRepository

class ProductService:
    def __init__(self, neo4j_driver):
        self.product_repository = ProductRepository(neo4j_driver)
    def get_all_product(self):
        return self.product_repository.get_all_product(); 