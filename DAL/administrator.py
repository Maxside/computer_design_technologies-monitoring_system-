from DAL.userr import User

class Administrator(User):
    def __init__(self, name, email, phone, user_id, password, login):
        super().__init__()
        self.name = name
        self.email = email
        self.phone = phone
        self.user_id = user_id
        self.password = password
        self.login = login
        self._accsess_level = 1


 