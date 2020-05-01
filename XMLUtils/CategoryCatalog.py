import sys
from Models.Category import Category


class CategoryCatalog:
    nesting_symbol = '  >  '

    def __init__(self):
        self.__categories = []

    def addCategory(self, id, name, parent_id=None):
        '''
            Parameters:
            category (Category): instance of Category.

        '''
        category = Category(id, name, parent_id)
        self.__categories.append(category)

    def getCategoryById(self, category_id):
        for category in self.__categories:
            if category.id == category_id:
                return category
        print(f'not find {category_id=}')

    def getCategoryTree(self, category):
        if category not in self.__categories:
            print('Category does not exist in CategoryCatalog\n'
                  f'category({category})')
            sys.exit(1)
        self.__last_cat_tree = ''
        self.__recursiveCreatinCategoryTree(tree = category.name, category = category)
        return self.__last_cat_tree

    def __recursiveCreatinCategoryTree(self, tree, category):
        if category.parent_id is None:
            return
        next_cat = None
        for cat in self.__categories:
            if cat.id == category.parent_id:
                self.__last_cat_tree = cat.name + self.nesting_symbol + tree
                next_cat = cat
                break
        if next_cat is not None:
            self.__recursiveCreatinCategoryTree(self.__last_cat_tree, next_cat)
        else:
            return

    def show(self):
        top_categories = []
        for cat in self.__categories:
            if cat.parent_id is None:
                top_categories.append(cat)
        self.showTree(top_categories, 0)

    def showTree(self, categories, level):
        for category in categories:
            print('-' * level, category.name, sep='')
            if self.__isChildsExist(category):
                child_categories = []
                for cat in self.__categories:
                    if cat.parent_id == category.id:
                        child_categories.append(cat)
                self.showTree(child_categories, level + 1)

    def __isChildsExist(self, category):
        for cat in self.__categories:
            if cat.parent_id == category.id:
                return True
        return False