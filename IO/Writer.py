import lxml.etree as ET


class Writer:

    _filename = None

    def __init__(self, filename = None):
        self._filename = 'outfile.xml' if filename is None else filename
        self.__createIdleXML()

    def __createIdleXML(self):
        root = ET.Element("PRODUCTS")
        tree = ET.ElementTree(root)
        tree.write(self._filename)

    def write(self, product_list):
        tree = ET.parse(self._filename)
        root = tree.getroot()
        for product in product_list:
            self.__writeProduct(root, product)
        tree.write(self._filename)
        self.__prettify()

    @staticmethod
    def __writeProduct(root, product):
        new_product = ET.SubElement(root, "PRODUCT")

        product_model = ET.SubElement(new_product, 'MODEL')
        product_model.text = str(product.id) + 'm'

        product_name = ET.SubElement(new_product, 'ProductName')
        product_name.text = product.name

        product_description = ET.SubElement(new_product, 'Description')
        product_description.text = product.description

        product_price = ET.SubElement(new_product, 'Price')
        product_price.text = str(product.price)

        product_quantity = ET.SubElement(new_product, 'Quantity')
        product_quantity.text = str(product.quantity)

        product_image = ET.SubElement(new_product, 'Image')
        product_image.text = product.image_path

        product_date = ET.SubElement(new_product, 'DateAvailable')
        product_date.text = product.date_available

        product_manufacturer = ET.SubElement(new_product, 'Manufacturer')
        product_manufacturer.text = product.manufacturer

        product_category = ET.SubElement(new_product, 'Categories')
        product_category.text = product.category_chain

        product_store = ET.SubElement(new_product, 'Stores')
        product_store.text = product.store

        product_title = ET.SubElement(new_product, 'MetaTitle')
        product_title.text = product.meta_title

        product_status = ET.SubElement(new_product, 'Status')
        product_status.text = '1'

    def __prettify(self):
        tree = ET.parse(self._filename)
        tree.write(self._filename, pretty_print=True, encoding='utf-8', xml_declaration=True)
        self.rep()

    def rep(self):
        # with open(self._filename) as f:
        #     for i in f.readlines():
        #         i = i.replace('&gt;', '->-')
        #         print(i)
        pass
