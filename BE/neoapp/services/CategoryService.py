from neoapp.respositories.CategoryRepository import CategoryRepository

class CategoryService:
    def __init__(self, neo4j_driver):
        self.category_service = CategoryRepository(neo4j_driver)
    def get_all_category(self):
        return self.category_service.get_all_category()
    def get_product_category(self, id_category=None):
        return self.category_service.get_product_category(id_category)