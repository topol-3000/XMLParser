import os
import traceback
from datetime import datetime
import Conf
from IO.Reader import Reader
from IO.Writer import Writer
from Core.Handler import Handler


def __createDirectory(dir_path):
    os.makedirs(dir_path)


def main():
    current_dir = os.getcwd()
    images_dir = (current_dir +
                  Conf.get(section='ImageDownloading', prop='ImagesDir') +
                  Conf.get(section='General', prop='DirSeparator') +
                  str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) +
                  Conf.get(section='ImageDownloading', prop='ImagesPath'))
    __createDirectory(images_dir)

    xml_path = (current_dir +
                Conf.get(section='General', prop='DirSeparator') +
                Conf.get(section='General', prop='InputXML'))
    reader = Reader(xml_path=xml_path)
    category_list, product_list = reader.read()

    product_handler = Handler(images_dir=images_dir)
    category_list, product_list = product_handler.handle(category_list, product_list)

    writer = Writer(filename=Conf.get(section='General', prop='OutputXML'))
    writer.write(product_list)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())
    input('Нажмите любую клавишу чтобы выйти')


# TODO print -> logger
# TODO GUI  с кнопкой загрузить xml, окно с логом, кнопка начать
# TODO add progress bar с процентами