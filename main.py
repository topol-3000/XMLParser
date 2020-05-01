from XMLUtils.Reader import Reader
import os

XML_FILE_PATH = r'\resourses\import.xml'

if __name__ == "__main__":
    reader = Reader(os.getcwd(),  XML_FILE_PATH)
    reader.start()
    input('Нажмите любую клавиши для выхода из программы')
