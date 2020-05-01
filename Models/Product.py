import random
from datetime import datetime

class Product:
    def __init__(self, id, name = None, category = None, price = None, image = None,
                 manufacturer = None, description = None, quantity = None):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.image = image
        self.manufacturer = manufacturer
        self.description = description
        if quantity is None:
            self.quantity = str(random.randint(1, 15))
        else:
            self.quantity = quantity
        self.date_available = datetime.now().strftime('%Y-%m-%d')
        self.store = 'default;'
        self.meta_title = 'meta_title' + str(random.randint(-10000, 100000))

    def __str__(self):
        return f'Product(\n' \
               f'\t{self.id=};\n' \
               f'\t{self.name=};\n' \
               f'\t{self.category=};\n' \
               f'\t{self.price=};\n' \
               f'\t{self.image=};\n' \
               f'\t{self.manufacturer=};\n' \
               f'\t{self.description=};\n' \
               f'\t{self.quantity=};\n' \
               f'\t)\n'