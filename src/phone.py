from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim  # Используем сеттер для установки значения

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._number_of_sim = value

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise ValueError("Нельзя сложить Phone с экземплярами других классов.")

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
