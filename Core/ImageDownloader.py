import requests


def downloadImageByUrl(url, file_path):
    with open(file_path, 'wb') as handle:
        response = requests.get(url, stream = True)
        if not response.ok:
            return False

        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
    return True
