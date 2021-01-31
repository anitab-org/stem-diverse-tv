from app.database.models.category import CategoryModel


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
    def find_category_by_title(title: str) -> "SectionModel":
        return CategoryModel.query.filter_by(title=title).first()

    @staticmethod
    def create_or_find_category(title: str):
        category = CategoryDAO.find_category_by_title(title)
        if category is None:
            category = CategoryDAO.create_category(title)
        return category
