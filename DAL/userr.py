class User():
    def __init__(self):
        self.user_id = 0
        self.password = ""
        self.login = ""
        self._accsess_level = 0
        # self.phone = None
        # self.email = None


    def verifyLogin(self, login):
        if self.getLogin() == login:
            return True
        return False
    
    def setLogin(self, login):
        self.login = login

    def getLogin(self):
        return self.login

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password
    
    def setPhone(self, phone):
        self.phone = phone

    def getPhone(self):
        return self.phone

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

if __name__ == "__main__":
    pass