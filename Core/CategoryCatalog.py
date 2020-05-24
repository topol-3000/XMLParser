import html
import Conf
from Models.Category import Category


class CategoryCatalog:
    nesting_symbol = html.unescape(Conf.get(section='Xml', prop='CategorySeparator'))

    def __init__(self):
        self.__categories = []
        self.__last_cat_tree = None

    def addCategory(self, category):
        """
        Args:
            category (Category): instance of Category.

        """
        self.__categories.append(category)

    def getCategoryById(self, category_id):
        """Returns category by id.

        Args:
            category_id (int): id of category
        Returns:
            Category: category if it exist in catalog, None otherwise.

        """
        for category in self.__categories:
            if category.id == category_id:
                return category
        print(f'Could not find category with id={category_id}')
        # TODO выбрасывать эксепшин
        return None

    def getCategoryChain(self, category):
        """Get Category chain for one category.

        Args:
            category (Category): category for which need get tree

        Returns:
            str: string with parent categories, None if category not found

        """
        if category not in self.__categories:
            print('Category does not exist in CategoryCatalog\n'
                  f'category({category})')
            return None
        self.__last_cat_tree = ''
        self.__recursiveCreatingCategoryChain(chain = category.name, category = category)
        return self.__last_cat_tree

    def __recursiveCreatingCategoryChain(self, chain, category):
        if category.parent_id is None:
            return
        next_cat = None
        for cat in self.__categories:
            if cat.id == category.parent_id:
                self.__last_cat_tree = cat.name + self.nesting_symbol + chain
                next_cat = cat
                break
        if next_cat is not None:
            self.__recursiveCreatingCategoryChain(self.__last_cat_tree, next_cat)
        else:
            return

    def show(self):
        top_categories = []
        for cat in self.__categories:
            if cat.parent_id is None:
                top_categories.append(cat)
        self.__showTree(top_categories, 0)

    def __showTree(self, categories, level):
        for category in categories:
            print('-' * level, category.name, sep='')
            if self.__isChildExist(category):
                child_categories = []
                for cat in self.__categories:
                    if cat.parent_id == category.id:
                        child_categories.append(cat)
                self.__showTree(child_categories, level + 1)

    def __isChildExist(self, category):
        for cat in self.__categories:
            if cat.parent_id == category.id:
                return True
        return False
