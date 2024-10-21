from neoapp.respositories.AdminAccountRepository import AdminAccountRepository

class AdminAccountService:
    def __init__(self, neo4j_driver):
        self.admin_account = AdminAccountRepository(neo4j_driver)
    
    def add_account(self, id_account, role, username, password):
        return self.admin_account.add_account(id_account, role, username, password)
    
    def get_all_accounts(self):
        return self.admin_account.get_all_accounts()
