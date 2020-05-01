import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from Models.Product import Product
from XMLUtils.CategoryCatalog import CategoryCatalog
import XMLUtils.ProductFillingTools as ProductFillingTools
import  XMLUtils.ImageDownloader as ImageDownloader
from  XMLUtils.CreatorXML import CreatorXML

TAG_CATEGORY = 'catalog'
TAG_PRODUCT = 'items'

IMAGES_DIRECTORY = '\\images\\' + str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
IMAGE_PREFIX = '\\catalog\\import_images\\'
IMAGE_PREFIX_FOR_SERVER = 'catalog/import_images/'

class Reader:
    __root = None

    def __init__(self, directory, xml_path):
        self.__directory = directory
        self.__categoryCatalog = CategoryCatalog()
        self.__creatorXML = CreatorXML(directory + '\\resourses\import_for_opencart.xml')

        tree = ET.parse(directory + xml_path)
        self.root = tree.getroot()

    def start(self):
        self.fillCategoryCatalog(self.root.find(TAG_CATEGORY))
        print('Убедитесь что уже имеются категории следующей вложенности:')
        self.__categoryCatalog.show()
        ImageDownloader.createDirectory(self.__directory + IMAGES_DIRECTORY + IMAGE_PREFIX)

        product_list = self.root.find(TAG_PRODUCT)
        count_products = len(product_list)
        for index, product_item in enumerate(product_list, 1):
            product = Product(
                id = ProductFillingTools.getId(product_item),
                name = ProductFillingTools.getName(product_item),
                category = ProductFillingTools.getCategory(product_item, self.categoryCatalog),
                price = ProductFillingTools.getPrice(product_item),
                image = ProductFillingTools.getImage(product_item, IMAGES_DIRECTORY,
                                                     IMAGE_PREFIX, IMAGE_PREFIX_FOR_SERVER,
                                                     root_directory = self.__directory),
                manufacturer = ProductFillingTools.getManufacturer(product_item),
                description = ProductFillingTools.getDescription(product_item)
            )
            self.__creatorXML.writeProduct(product)
            print(f'Загружено {index} товаров из {count_products}')
        self.__creatorXML.prettify()
        sys.exit(99)

    @property
    def root_element(self):
        return self.__root

    @property
    def categoryCatalog(self):
        return self.__categoryCatalog

    def fillCategoryCatalog(self, category_list):
        """Заполняем каталог категорий всеми категориями из xml."""
        for category in category_list:
            parent = category.attrib['parentId'] if 'parentId' in category.attrib else None
            self.__categoryCatalog.addCategory(id = category.attrib['id'],
                                name = category.text,
                                parent_id = parent)

