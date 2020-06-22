from abc import ABC, abstractmethod

class IAcc(ABC):
    """Інтерфейс акаунту(cуб'єкт)"""
    @abstractmethod
    def changeContactInfo(self):
        pass
    
    @abstractmethod
    def changeLogin(self, obj):
        pass

  
class Account(IAcc):
    """Акаунт(реальний суб'єкт)"""
    def changeContactInfo(self, obj):
        self.obj = obj
        new_phone = input("Введіть ваш новий телефон:")
        self.obj.setPhone(new_phone)
        new_email = input("Введіть вашу нову електонну адресу:")
        self.obj.setEmail(new_email)
        
    def changeLogin(self, obj):
        self.obj = obj
        new_login = input("Введіть ваш новий логін:")
        self.obj.setLogin(new_login)
  

class AccsessControler(IAcc):
    """Замісник(proxy) для контролю доступу до певних привілегійованих функцій"""
    def __init__(self, real_subject: Account, chek) -> None:
        self._real_subject = real_subject
        self.chek = chek

    def changeContactInfo(self, obj):
        self._real_subject.changeContactInfo(obj)
            
    def changeLogin(self, obj):
        if self.checkAccsess():
            self._real_subject.changeLogin(obj)

    def checkAccsess(self):
        if self.chek == 1:
            print("Proxy:Доступ підтверджено!")
            return True
        print("Proxy:У вас немає прав доступу для цієї операції!")
        return False


def client(subject: IAcc, obj):
    
    subject.changeLogin(obj)
    subject.changeContactInfo(obj)


