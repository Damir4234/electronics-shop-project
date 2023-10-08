import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name  # Сделаем атрибут name приватным (начинается с "_")
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self._name = new_name[:10]  # Обрезаем строку, если она больше 10 символов
        else:
            self._name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, csv_file_path):
        cls.all.clear()
        with open(csv_file_path, mode='r', encoding='cp1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        try:
            return int(float(string))
        except ValueError:
            raise ValueError("Не удалось преобразовать строку в число")


