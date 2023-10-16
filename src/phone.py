from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise ValueError("Нельзя сложить Phone с экземплярами других классов.")

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
