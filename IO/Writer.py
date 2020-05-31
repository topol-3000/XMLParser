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
        count_of_products = len(product_list)
        print(f'{count_of_products} will be write')
        for item, product in enumerate(product_list, 1):
            self.__writeProduct(root, product)
            print(f'{product.id} has been written. '
                  f'{count_of_products - item} remain')
        tree.write(self._filename)
        self.__prettify()

    @staticmethod
    def __writeProduct(root, product):
        new_product = ET.SubElement(root, "PRODUCT")

        product_model = ET.SubElement(new_product, 'MODEL')
        product_model.text = str(product.id) + 'm'

        SEOKeyword = ET.SubElement(new_product, 'SEOKeyword')
        SEOKeyword.text = str(product.id) + 'm'

        product_name = ET.SubElement(new_product, 'ProductName')
        product_name.text = str(product.name)

        sku = ET.SubElement(new_product, 'SKU')
        sku.text = ''

        upc = ET.SubElement(new_product, 'UPC')
        upc.text = ''

        ean = ET.SubElement(new_product, 'EAN')
        ean.text = ''

        jan = ET.SubElement(new_product, 'JAN')
        jan.text = ''

        isbn = ET.SubElement(new_product, 'ISBN')
        isbn.text = ''

        mpn = ET.SubElement(new_product, 'MPN')
        mpn.text = ''

        location = ET.SubElement(new_product, 'Location')
        location.text = ''

        product_description = ET.SubElement(new_product, 'Description')
        product_description.text = str(product.description)

        metaTagDescription = ET.SubElement(new_product, 'MetaTagDescription')
        metaTagDescription.text = str(product.description)

        metaTagKeywords = ET.SubElement(new_product, 'MetaTagKeywords')
        metaTagKeywords.text = str(product.name)

        product_price = ET.SubElement(new_product, 'Price')
        product_price.text = str(product.price)

        productTags = ET.SubElement(new_product, 'ProductTags')
        productTags.text = ''

        minimumQuantity = ET.SubElement(new_product, 'MinimumQuantity')
        minimumQuantity.text = '0'

        SubtractStock = ET.SubElement(new_product, 'SubtractStock')
        SubtractStock.text = '0'

        product_quantity = ET.SubElement(new_product, 'Quantity')
        product_quantity.text = str(product.quantity)

        product_image = ET.SubElement(new_product, 'Image')
        product_image.text = str(product.image_path)

        product_date = ET.SubElement(new_product, 'DateAvailable')
        product_date.text = str(product.date_available)

        product_manufacturer = ET.SubElement(new_product, 'Manufacturer')
        product_manufacturer.text = str(product.manufacturer)

        product_category = ET.SubElement(new_product, 'Categories')
        product_category.text = str(product.category_list)

        product_store = ET.SubElement(new_product, 'Stores')
        product_store.text = str(product.store)

        product_title = ET.SubElement(new_product, 'MetaTitle')
        product_title.text = str(product.name)

        product_status = ET.SubElement(new_product, 'Status')
        product_status.text = '1'

        OutOfStockStatus = ET.SubElement(new_product, 'OutOfStockStatus')
        OutOfStockStatus.text = '5'

        RequiresShipping = ET.SubElement(new_product, 'RequiresShipping')
        RequiresShipping.text = '0'

        LengthClass = ET.SubElement(new_product, 'LengthClass')
        LengthClass.text = '0'

        Length = ET.SubElement(new_product, 'Length')
        Length.text = '0.00000000'

        Width = ET.SubElement(new_product, 'Width')
        Width.text = '0.00000000'

        height = ET.SubElement(new_product, 'height')
        height.text = '0.00000000'

        Weight = ET.SubElement(new_product, 'Weight')
        Weight.text = '0.00000000'

        WeightClass = ET.SubElement(new_product, 'WeightClass')
        WeightClass.text = '0'

        SortOrder = ET.SubElement(new_product, 'SortOrder')
        SortOrder.text = '0'

        Viewed = ET.SubElement(new_product, 'Viewed')
        Viewed.text = '0'

        RelatedProduct = ET.SubElement(new_product, 'RelatedProduct')
        OptionName = ET.SubElement(new_product, 'OptionName')
        OptionValue = ET.SubElement(new_product, 'OptionValue')
        additionalImages = ET.SubElement(new_product, 'additionalImages')
        SpeicalPrice = ET.SubElement(new_product, 'SpeicalPrice')
        TaxClass = ET.SubElement(new_product, 'TaxClass')
        FilterGroupName = ET.SubElement(new_product, 'FilterGroupName')
        FilterNames = ET.SubElement(new_product, 'FilterNames')
        Attributes = ET.SubElement(new_product, 'Attributes')
        Discount = ET.SubElement(new_product, 'Discount')
        Downloadid = ET.SubElement(new_product, 'Downloadid')
        Reviews = ET.SubElement(new_product, 'Reviews')

    def __prettify(self):
        tree = ET.parse(self._filename)
        tree.write(self._filename, pretty_print=True, encoding='utf-8', xml_declaration=True)
