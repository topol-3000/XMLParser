class Category:
    def __init__(self, id: str, name: str, parent_id: int = None):
        self.id = id
        self.name = name
        self.parent_id = parent_id

    def __str__(self):
        return f'Category(id={self.id}; name={self.name})'