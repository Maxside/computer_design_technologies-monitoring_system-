from DAL.userr import User

class StoreOperator(User):
    def __init__(self, name, store_id, email, phone, user_id, password, login):
        super().__init__()
        self.name = name
        self.store_id = store_id
        self.email = email
        self.phone = phone
        self.user_id = user_id
        self.password = password
        self.login = login
        
        

