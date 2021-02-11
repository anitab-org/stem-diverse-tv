from app.database.models.category import CategoryModel
from flask_sqlalchemy import BaseQuery
from typing import List


class CategoryDAO:
    @staticmethod
    def create_category(title: str):
        """
        Create new section if the params fields are valid and section is not created before.
        :param title: "section title",
        :return:
        """
        category = CategoryModel(title=title)
        category.save_to_db()
        return category

    @staticmethod
    def find_category_by_id(id: int) -> "CategoryModel":
        """
        Finds category by the given id (or None)
        :param id: id of the category
        :return: CategoryModel or None
        """
        return CategoryModel.query.get(id)

    @staticmethod
    def find_category_by_title(title: str) -> "CategoryModel":
        """
        Finds category by the given title
        :param title: title of the category
        :return: CategoryModel or None
        """
        return CategoryModel.query.filter_by(title=title).first()

    @staticmethod
    def create_or_find_category(title: str):
        category = CategoryDAO.find_category_by_title(title)
        if category is None:
            category = CategoryDAO.create_category(title)
        return category

    @staticmethod
    def add_category_sections(category, sections: BaseQuery) -> bool:
        non_existing_category_sections = list(
            filter(lambda section: section not in category.section, sections)
        )
        category.add_sections(non_existing_category_sections)
        return len(non_existing_category_sections) == sections.count()

    @staticmethod
    def update_category(category, title):
        category.title = title
        category.save_to_db()
        return category

    @staticmethod
    def delete_category(category):
        category.delete_from_db()
