import os
from queue import Queue
import Conf
from Core.CategoryCatalog import CategoryCatalog
from Network.Downloader import Downloader


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
                product.category_list = self.__categoryCatalog.getCategorylistByChain(product.category_chain)

    def __handleImages(self):
        self.queue = Queue()

        # Запускаем потоки и очередь
        for i in range(10):
            t = Downloader(self.queue)
            t.setDaemon(True)
            t.start()
        self.__fillImageQueue()

        # Ждем завершения работы очереди
        self.queue.join()

    def onSuccessImageDownload(self, product):
        dir_separator_on_server = Conf.get(section='General', prop='ServerDirSeparator')
        image_name = os.path.basename(product.image_url)
        image_path_on_server = Conf.get(section='ImageDownloading',
                                        prop='ImagesPathOnServer')
        if image_path_on_server[0] == dir_separator_on_server:
            image_path_on_server = image_path_on_server[1:]
        if image_path_on_server[-1] == dir_separator_on_server:
            image_path_on_server = image_path_on_server[:-1]
        product.image_path = (image_path_on_server + dir_separator_on_server + image_name)
        print(f'Image {product.image_url} has been downloaded. {self.queue.qsize()} remain.')

    def __fillImageQueue(self):
        # Даем очереди нужные нам ссылки для скачивания
        gen = (product for product in self.__product_list if product.image_url is not None)
        for product_item in gen:
            dir_separator = Conf.get(section='General', prop='DirSeparator')
            image_name = os.path.basename(product_item.image_url)
            local_image_path = (self._images_dir + dir_separator + image_name)
            task = {
                'url': product_item.image_url,
                'file_path': local_image_path,
                'on_success_cb': self.onSuccessImageDownload,
                'cb_args': product_item
            }
            self.queue.put(task)
