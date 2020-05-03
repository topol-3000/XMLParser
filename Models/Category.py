class Category:
    """Model for category.

    Attributes:
        id (int): Id of product.
        name (str): Name of product.
        parent_id (int|None): Id of category.

    Args:
        id (int): id of category.
        name (str): name of category.
        parent_id (int|None): id of parent category for current category.

    """
    def __init__(self, id, name, parent_id):

        self.id = id
        self.name = name
        self.parent_id = parent_id

    def __str__(self):
        return f'Category(id={self.id}; name={self.name}; parent_id={self.parent_id})'
