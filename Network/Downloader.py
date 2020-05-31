# -*- coding: utf-8 -*-
import os
import threading
import requests


class Downloader(threading.Thread):
    """Потоковый загрузчик файлов"""

    def __init__(self, queue):
        """Инициализация потока"""
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """Запуск потока"""
        while True:
            # Получаем url из очереди
            task = self.queue.get()
            url = task['url']
            file_path = task['file_path'] if 'file_path' in task else None
            on_success_cb = task['on_success_cb'] if 'on_success_cb' in task else None
            cb_args = task['cb_args'] if 'cb_args' in task else None

            # Скачиваем файл
            result = self.download_file(url, file_path)
            if result and on_success_cb is not None:
                # TODO if cb_args is None?
                on_success_cb(cb_args)
            else:
                print(f'Image {url} has not been downloaded.')

            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()



    def download_file(self, url, file_path):
        """Скачиваем файл"""
        file_name = file_path if file_path is not None else os.path.basename(url)
        with open(file_name, 'wb') as handle:
            response = requests.get(url, stream=True)
            if not response.ok:
                return False

            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        return True
