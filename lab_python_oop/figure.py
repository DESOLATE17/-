from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный класс «Геометрическая фигура»
    """
    @abstractmethod
    def square(self):
        """
        содержит виртуальный метод для вычисления площади фигуры.
        """
        pass

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __eq__(self, other):
        return self.square() == other.square()

    def __ne__(self, other):
        return self.square() != other.square()

    def __gt__(self, other):
        return self.square() > other.square()
    def __ge__(self, other):
        return self.square() <= other.square()