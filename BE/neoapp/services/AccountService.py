from neoapp.respositories.AccountRepository import AccountRepository

class AccountService:
    def __init__(self, neo4j_driver):
        self.account_repository = AccountRepository(neo4j_driver)

    def login(self, username, password):
        try:
            records = self.account_repository.get_account_by_credentials(username, password)
            if records:  # Kiểm tra xem records có rỗng hay không
                record = records[0]
                account = record.get('a', {}) 
                person = record.get('p', {})   
                return {
                    'iduser':person.get('PersonID'),
                    'name': person.get('Name'),  
                    'email': person.get('Email'),
                    'phone': person.get('Phone'),
                    'address': person.get('Address'),
                    'birth_date': person.get('BirthDate'),
                    'gender': person.get('Gender'),
                    'avatar': person.get('Avatar'),
                    'role': account.get('Role'),
                    'username':account.get('Username'),   
                }
            return None
        except Exception as e:
            print(f"Error in login: {e}")  # Ghi lại lỗi
            return None
        
    def reset_password(self,username,old_password,new_password):
        return self.account_repository.reset_password(username,old_password,new_password)
    
    def create_person_and_account(self, name, email, phone, username, password, admin):
        return self.account_repository.create_person_and_account(name,email,phone,username,password,admin)
        