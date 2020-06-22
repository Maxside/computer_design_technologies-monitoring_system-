from __future__ import annotations
from abc import ABC, abstractmethod
from DAL.product import ProductRequest
from typing import List
from pony.orm import db_session
from DAL.database_store import Product


class INotify(ABC):
    """Інтерфейс видавця оголошує методи для управління підписками."""

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class NotifyPublisher(INotify):
    """Видавець володіє деяким важливим станом і оповіщає спостерігачів про його зміну."""
    _state: dict = None

    _observers: List[Observer] = []
    """Список підписників"""

    def attach(self, observer: Observer) -> None:
        """Метод додавання підписників"""
        print("INotify: Приєднав спостерігача.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Метод видалення підписників"""
        print("INotify: Відєднав спостерігача.")
        self._observers.remove(observer)

    def notify(self) -> None:
        """Запуск оновлення в кажному підписнику."""
        print("INotify: Повідомлення спостерігачів ...")
        for observer in self._observers:
            observer.update(self)
    
    @db_session
    def some_business_logic(self) -> None:
        """Зріз інформації по товарах, що закінчується"""
        self._state = {}
        print("\nINotify: Я роблю щось важливе.")
        for p in Product.select(lambda p: p.quantity < 25):
            self._state[p.quantity] = p.name

        print(f"INotify: Мій стан щойно змінився на: {self._state}")
        self.notify()


class Observer(ABC):
    """Спостерігач"""
    @abstractmethod
    def update(self, subject: INotify) -> None:
        pass


class aProduct(Observer):
    """Конкретний спостерігач, що слідкує за зміною кількості товарів"""
    def update(self, subject: INotify) -> None:
        if 20 in subject._state:
            print("Э товари, що закінчуються!")

class bProduct(Observer):
    """Конкретний спостерігач, що реагує на відсутність товару"""
    def update(self, subject: INotify) -> None:
        if 0 in subject._state:
            print("Э товари, що закінчились!")
        


