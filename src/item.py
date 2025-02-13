import csv


class InstantiateCSVError(Exception):
    def __init__(self, message="Файл item.csv поврежден"):
        self.message = message
        super().__init__(self.message)


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

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self._name

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
    def instantiate_from_csv(cls, csv_file_path='items.csv'):
        cls.all.clear()
        try:
            with open(csv_file_path, mode='r', encoding='cp1251') as file:
                try:
                    reader = csv.DictReader(file)
                    required_columns = {'name', 'price', 'quantity'}
                    if not required_columns.issubset(reader.fieldnames):
                        raise InstantiateCSVError("Файл items.csv поврежден: отсутствует одна из колонок данных")
                    for row in reader:
                        try:
                            name = row['name']
                            price = float(row['price'])
                            quantity = int(row['quantity'])
                            item = cls(name, price, quantity)
                        except KeyError:
                            raise InstantiateCSVError("Файл items.csv поврежден: отсутствует одна из колонок данных")
                except csv.Error:
                    raise InstantiateCSVError("Файл items.csv поврежден: ошибка чтения CSV")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(string):
        try:
            return int(float(string))
        except ValueError:
            raise ValueError("Не удалось преобразовать строку в число")

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Нельзя сложить Item с экземплярами других классов.")
