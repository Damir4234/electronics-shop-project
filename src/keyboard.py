from src.item import Item


class LanguageMixin:
    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)
        self._name = name

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
            self._name = new_name[:10]
        else:
            self._name = new_name
