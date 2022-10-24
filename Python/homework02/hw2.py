from keyword import iskeyword
import json


class JsonTransformer:
    def __init__(self, mapping):
        for key, item in mapping.items():
            new_key = key
            if iskeyword(key):
                new_key += '_'
            setattr(self, new_key, item)


class ColorizeMixin:
    repr_color_code = 33

    def __str__(self):
        return f'\033[1;{self.repr_color_code}m {self.title} | {self.price} ₽ \033[0m'


class Advert(ColorizeMixin, JsonTransformer):
    def __init__(self, mapping):
        super().__init__(mapping)
        if 'location' in mapping:
            self.location = JsonTransformer(mapping['location'])

    @property
    def price(self):
        try:
            return self._price
        except AttributeError:
            return 0

    @price.setter
    def price(self, price):
        assert price >= 0, 'price must be >= 0'
        self._price = price

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    corgi_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    corgi = json.loads(corgi_str)
    corgi_adv = Advert(corgi)
    print('Colorized representation:', corgi_adv)
    print('price attribute:', corgi_adv.price)
    print('class_ attribute:', corgi_adv.class_)
    print('.location.address:', corgi_adv.location.address, end='\n\n')

    # no price
    lesson_str = """{
        "title": "python",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_adv = Advert(lesson)

    # 0 when price is not specified
    print('No price in json:', lesson_adv.price, end='\n\n')

    # negative price
    iphone_str = """{
            "title": "iPhone X",
            "price": -100,
            "location": {
                "address": "город Самара, улица Мориса Тореза, 50",
                "metro_stations": ["Спортивная", "Гагаринская"]
            }
        }"""
    iphone = json.loads(iphone_str)
    iphone_adv = Advert(iphone)