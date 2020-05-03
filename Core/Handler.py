import os
import Conf
from Core import ImageDownloader
from Core.CategoryCatalog import CategoryCatalog


class Handler:
    """Product & category handler."""

    def __init__(self, images_dir = None):
        #: str: Path to directory, where will be store images
        self._images_dir = os.getcwd() if images_dir is None else images_dir
        #: Core.CategoryCatalog: Object for convenient work with categories. Category store.
        self.__categoryCatalog = CategoryCatalog()
        #: list: List of Model.Category.Category
        self.__category_list = None
        #: list: List of Model.Product.Product
        self.__product_list = None

    def handle(self, category_list, product_list):
        self.__category_list = category_list
        self.__product_list = product_list
        self.__fillCategoryCatalog()
        self.__updateProductCategories()
        self.__handleImages()
        return self.__category_list, self.__product_list

    def __fillCategoryCatalog(self):
        for category in self.__category_list:
            self.__categoryCatalog.addCategory(category)

    def __updateProductCategories(self):
        for product in self.__product_list:
            # TODO обернуть в трай ексепшн
            category = self.__categoryCatalog.getCategoryById(product.category_id)
            if category is None:
                print(f'Сategory from {product} doesn\'t found in category list')
                continue
            else:
                product.category_chain = self.__categoryCatalog.getCategoryChain(category)

    def __handleImages(self):
        dir_separator = Conf.get(section='General', prop='DirSeparator')
        dir_separator_on_server = Conf.get(section='General', prop='ServerDirSeparator')
        for product in self.__product_list:
            image_name = product.getImageNameFromUrl()
            local_image_path = (self._images_dir + dir_separator + image_name)

            result = ImageDownloader.downloadImageByUrl(url=product.image_url,
                                                        file_path=local_image_path)
            if result:
                image_path_on_server = Conf.get(section='ImageDownloading',
                                                prop='ImagesPathOnServer')
                if image_path_on_server[0] == dir_separator_on_server:
                    image_path_on_server = image_path_on_server[1:]
                if image_path_on_server[-1] == dir_separator_on_server:
                    image_path_on_server = image_path_on_server[:-1]

                product.image_path = (image_path_on_server + dir_separator_on_server + image_name)
                continue
            print(f'Image {product.image_url} was not downloaded.\n{product}')