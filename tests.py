from __future__ import annotations
from DAL.order import Order
from DAL.builder import OrderBuild
from datetime import datetime
from BLL.accounts import IAcc, Account, AccsessControler, client
from DAL.store_operator import StoreOperator
from DAL.administrator import Administrator
from DAL.userr import User
from DAL.product import ProductRequest
from typing import List
from pony.orm import db_session
from DAL.database_store import Product
from BLL.notify import NotifyPublisher, Observer, aProduct, bProduct
from BLL.memento import Originator, StatusMemento, Memento, Caretaker
import unittest

class TestMyPattern(unittest.TestCase):
    def setUp(self):
        #builder
        self.date_created = datetime.now().strftime("%d/%m/%Y, %H:%M")
        #proxy
        self.standart_access_user = StoreOperator("Оператор Іван", 1, "ivan@ukr.net", "000000000", 2, "pass", "ivan" )
        self.super_access_user = Administrator("Адміністратор Богдан", "bogdan@bigmir.net", "010101010", 1, "admin12344", "bogration")

    def test_builder(self):
        print("Test Builder")
        builder = OrderBuild().item()
        builder.withOrderId(1)
        builder.withDateCreated()
        builder.withDateShipped("22/06/2020, 11:17")
        builder.withOversizedCargo("Габаритний")
        builder.withStatus("Архівний")
        new_order = builder.build()
        new_order.print()

        self.assertEqual(new_order.order_id, 1)
        self.assertEqual(new_order.date_created, self.date_created)
        self.assertEqual(new_order.date_shipped, "22/06/2020, 11:17")
        self.assertEqual(new_order.oversized_cargo, "Габаритний")
        self.assertEqual(new_order.status, "Архівний")
        print("--"*15)

    def test_proxy_standart_user(self):
        print("Test Proxy - standart user")
        user = self.standart_access_user
        real_subject = Account()
        proxy = AccsessControler(real_subject, user._accsess_level)
        client(proxy, user)

        self.assertEqual(proxy.checkAccsess(), False)
        print("--"*15)

    def test_proxy_super_user(self):
        print("Test Proxy - super user")
        user = self.super_access_user
        real_subject = Account()
        proxy = AccsessControler(real_subject, user._accsess_level)
        client(proxy, user)

        self.assertEqual(proxy.checkAccsess(), True)

    def test_observer(self):
        subject = NotifyPublisher()
        observer_a = aProduct()
        observer_b = bProduct()
        subject.attach(observer_a)
        subject.attach(observer_b)
        self.assertNotEqual(subject._observers, [])
        self.assertEqual(len(subject._observers), 2)
        subject.some_business_logic()
        subject.detach(observer_a)
        self.assertEqual(len(subject._observers), 1)
        subject.some_business_logic()

    def test_memento(self):
        originator = Originator("Нове")
        caretaker = Caretaker(originator)
        self.assertEqual(originator._state, "Нове")

        caretaker.backup()
        originator.change_status("Активне")
        self.assertEqual(originator._state, "Активне")
        
        caretaker.backup()
        originator.change_status("Архівне")
        self.assertEqual(originator._state, "Архівне")
        
        print()
        caretaker.show_history()

        print("\nClient: Виконати відкат!!\n")
        caretaker.undo()
        self.assertEqual(originator._state, "Активне")

        print("\nClient: Виконати відкат!\n")
        caretaker.undo()
        self.assertEqual(originator._state, "Нове")


if __name__ == "__main__":
    unittest.main()
    