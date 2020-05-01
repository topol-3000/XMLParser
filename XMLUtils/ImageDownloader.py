import os
import requests

def createDirectory(directory):
    os.makedirs(directory)

def downloadImageByUrl(url, filename):
    with open(filename, 'wb') as handle:
        response = requests.get(url, stream = True)
        if not response.ok:
            return False

        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
    return True