from neoapp.respositories.AdminUserRepository import AdminUserRepository

class AdminUserService:
    def __init__(self, neo4j_driver):
        self.admin_user_repository = AdminUserRepository(neo4j_driver)
    
    def add_user(self, id_person, name, address, phone, birth, gender):
        return self.admin_user_repository.add_user(id_person, name, address, phone, birth, gender)
    
    def get_all_users(self):
        return self.admin_user_repository.get_all_user()
