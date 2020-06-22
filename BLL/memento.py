from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime

class Originator():
    """Оригінатор містить деякий важливий стан, який може змінюватися з часом. Він також
    визначає метод збереження стану всередині пам’яті та метод відновлення попередньго стану """

    _state = None
   
    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: Мій початковий стан '{self._state}'")

    def change_status(self, new_state) -> None:
        print("Originator: Зміна стану ...")
        self._state = new_state
        print(f"Originator: Новий стан '{self._state}'")
        
    def save(self) -> Memento:
        """Збереження поточного стану в знімок."""
        return StatusMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """Відновлення попереднього стану із знімку"""
        self._state = memento.get_state()
        print(f"Originator: Новий стан: '{self._state}'")


class Memento(ABC):
    """Інтерфейс знімку, з абстрактини методами отримання назви знімку та дати"""
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class StatusMemento(Memento):
    """Знімок статусу"""
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())

    def get_state(self) -> str:
        """Знімок використовує цей метод для відновлення стану"""
        return self._state

    def get_name(self) -> str:
        """Викристовується для відображення метаданих"""
        return f"{self._date} / ({self._state}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker():
    """Клас доглядача за даними, який використовує інтерфейс доступу для відновлення стану,
    проте не має прямого доступу до нього """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Створення бекапу стану...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Відновлення стану до: '{memento.get_name()}'")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Історія змін стану:")
        for memento in self._mementos:
            print(memento.get_name())

