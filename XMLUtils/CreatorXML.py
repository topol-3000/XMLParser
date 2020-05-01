import lxml.etree as ET

class CreatorXML:
    __filename = None
    def __init__(self, filename):
        self.__filename = filename
        self.__initialSettings()

    def __initialSettings(self):
        root = ET.Element("PRODUCTS")
        tree = ET.ElementTree(root)
        tree.write( self.__filename)

    def writeProduct(self, product):
        tree = ET.parse(self.__filename)
        root = tree.getroot()

        new_product = ET.SubElement(root, "PRODUCT")

        product_model = ET.SubElement(new_product, 'MODEL')
        product_model.text = product.id + 'm'

        product_name = ET.SubElement(new_product, 'ProductName')
        product_name.text = product.name

        product_description = ET.SubElement(new_product, 'Description')
        product_description.text = product.description

        product_price = ET.SubElement(new_product, 'Price')
        product_price.text = product.price

        product_quantity = ET.SubElement(new_product, 'Quantity')
        product_quantity.text = product.quantity

        product_image = ET.SubElement(new_product, 'Image')
        product_image.text = product.image

        product_date = ET.SubElement(new_product, 'DateAvailable')
        product_date.text = product.date_available

        product_manufacturer = ET.SubElement(new_product, 'Manufacturer')
        product_manufacturer.text = product.manufacturer

        product_category = ET.SubElement(new_product, 'Categories')
        product_category.text = product.category

        product_store = ET.SubElement(new_product, 'Stores')
        product_store.text = product.store

        product_title = ET.SubElement(new_product, 'MetaTitle')
        product_title.text = product.meta_title

        product_status = ET.SubElement(new_product, 'Status')
        product_status.text = '1'

        tree.write(self.__filename)

    def prettify(self):
        tree = ET.parse(self.__filename)
        tree.write(self.__filename, pretty_print=True, encoding='utf-8', xml_declaration=True)
