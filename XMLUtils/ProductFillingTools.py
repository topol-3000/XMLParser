import XMLUtils.ImageDownloader as ImageDownloader

TAG_PRODUCT_ID = 'id'
TAG_PRODUCT_NAME = 'name'
TAG_PRODUCT_IMAGE = 'image'
TAG_PRODUCT_PRICE = 'price_trade'
TAG_PRODUCT_MANUFACTURER = 'vendor'
TAG_PRODUCT_DESCRIPTION = 'description'


def getCategory(product, categoryCatalog):
    category = categoryCatalog.getCategoryById(product.find('categoryId').text)
    categoryTree = categoryCatalog.getCategoryTree(category)
    return categoryTree


def getImage(product, images_directory, image_prefix, image_prefix_for_server, root_directory):
    image_url = product.find(TAG_PRODUCT_IMAGE).text
    image_name = makeFilenameFromURL(image_url)
    if ImageDownloader.downloadImageByUrl(image_url, root_directory + images_directory + image_prefix + image_name):
        return image_prefix_for_server + image_name
    else:
        print(f'image was not downloaded by {image_url=}')

def getId(product):
    id = product.attrib[TAG_PRODUCT_ID]
    return id

def getName(product):
    name = product.find(TAG_PRODUCT_NAME)
    return name.text

def getDescription(product):
    description = product.find(TAG_PRODUCT_DESCRIPTION)
    return description.text

def getManufacturer(product):
    manufacturer = product.find(TAG_PRODUCT_MANUFACTURER)
    return manufacturer.text

def getPrice(product):
    price = product.find(TAG_PRODUCT_PRICE)
    return price.text

def makeFilenameFromURL(url):
    filename = url.split('/')[-1]
    return filename