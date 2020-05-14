import random
from datetime import datetime


class Product:
    """Model for product.

    Attributes:
        id (str): Id of product.
        name (str): Name of product.
        category_id (str): Id of category.
        price (float): Price of product.
        image_url (str): url to image.
        manufacturer (str): manufacturer of product.
        description (str): description of product.
        quantity (int): quantity of product.
        date_available (str): creation date of product.
        store (str): Name of store, field for opencart.
        image_path (str): path to image on server.
        category_chain (str): Category chain e.g. "Moto > Geon".
        meta_title (str): meta string for product.

    Args:
        id (str): Id of product.
        name (str): Name of product.
        category_id (str): Id of category.
        price (float): Price of product.
        image_url (str): url to image.
        manufacturer (str): manufacturer of product.
        description (str): description of product.
        quantity (int): quantity of product.

    """

    def __init__(self, id, name, category_id, price,
                 image_url, manufacturer, description, quantity):
        self.id = id
        self.name = name
        self.category_id = category_id
        self.price = price
        self.image_url = image_url
        self.manufacturer = manufacturer
        self.description = description
        self.quantity = quantity
        self.date_available = datetime.now().strftime('%Y-%m-%d')
        self.store = 'default;'
        self.meta_title = 'meta_title_' + str(random.randint(0, 100000))
        self.category_chain = None
        self.image_path = None

    def getImageNameFromUrl(self):
        if self.image_url is not None:
            return self.image_url.split('/')[-1]

    def __str__(self):
        return f'Product(\n' \
               f'\t{self.id=};\n' \
               f'\t{self.name=};\n' \
               f'\t{self.category_id=};\n' \
               f'\t{self.category_chain=};\n' \
               f'\t{self.price=};\n' \
               f'\t{self.image_url=};\n' \
               f'\t{self.manufacturer=};\n' \
               f'\t{self.description=};\n' \
               f'\t{self.quantity=};\n' \
               f'\t{self.date_available=};\n' \
               f'\t{self.store=};\n' \
               f'\t{self.meta_title=};\n' \
               f'\t{self.image_path=};\n' \
               f'\t)\n'
