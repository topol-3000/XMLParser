import lxml.etree as ET
from Models.Product import Product
from Models.Category import Category

TAG_CATEGORIES = 'categories'
TAG_PRODUCTS = 'offers'
TAG_PRODUCT_ID = 'id'
TAG_PRODUCT_NAME = 'name'
TAG_PRODUCT_IMAGE = 'picture'
TAG_PRODUCT_PRICE = 'price'
TAG_PRODUCT_CATEGORY = 'categoryId'
TAG_PRODUCT_MANUFACTURER = 'vendor'
TAG_PRODUCT_DESCRIPTION = 'description'
TAG_PRODUCT_QUANTITY = 'quantity'

class Reader:

    def __init__(self, xml_path):
        tree = ET.parse(xml_path)
        self.__root = tree.getroot()
        self.__product_list = self.__root.find('shop').find(TAG_PRODUCTS)

    def read(self):
        return self.__getCategoryList(), self.__getProductList()

    def __getCategoryList(self):
        category_list = []
        for category in self.__root.find('shop').find(TAG_CATEGORIES):
            parent = category.attrib['parentId'] if 'parentId' in category.attrib else None
            category = Category(id = category.attrib['id'],
                                name = category.text,
                                parent_id = parent)
            category_list.append(category)
        return category_list

    def __getProductList(self):
        product_list = []
        for product_item in self.__product_list:
            product = Product(
                id = self.__getProductId(product_item),
                name = self.__getProductName(product_item),
                category_id= self.__getProductCategoryId(product_item),
                price = self.__getProductPrice(product_item),
                image_url= self.__getProductImage(product_item),
                manufacturer = self.__getProductManufacturer(product_item),
                description = self.__getProductDescription(product_item),
                quantity = self.__getProductQuantity(product_item)
            )
            product_list.append(product)
        return product_list

    @staticmethod
    def __getProductCategoryId(product):
        category = product.find(TAG_PRODUCT_CATEGORY)
        return category.text if category is not None else None

    @staticmethod
    def __getProductImage(product):
        image_url = product.find(TAG_PRODUCT_IMAGE).text
        return image_url

    @staticmethod
    def __getProductId(product):
        if TAG_PRODUCT_ID in product.attrib:
            return product.attrib[TAG_PRODUCT_ID]
        return '-1'

    @staticmethod
    def __getProductName(product):
        name = product.find(TAG_PRODUCT_NAME)
        if name is not None:
            return name.text
        return ''

    @staticmethod
    def __getProductDescription(product):
        description = product.find(TAG_PRODUCT_DESCRIPTION)
        if description is not None:
            return description.text
        return ''

    @staticmethod
    def __getProductManufacturer(product):
        manufacturer = product.find(TAG_PRODUCT_MANUFACTURER)
        if manufacturer is not None:
            return manufacturer.text
        return ''

    @staticmethod
    def __getProductPrice(product):
        price = product.find(TAG_PRODUCT_PRICE)
        if price is not None:
            if ',' in price.text:
                # 135,1 -> 135.0
                return float(price.text.split(',')[0])
            return float(price.text)
        return 0.0

    @staticmethod
    def __getProductQuantity(product):
        quantity = product.find(TAG_PRODUCT_QUANTITY)
        if quantity is not None:
            if ',' in quantity.text:
                # 1,000 -> 1
                return int(quantity.text.split(',')[0])
            return int(quantity.text)
        return 1
