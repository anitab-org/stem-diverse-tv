from app.database.models.section import SectionModel


class SectionDAO:
    @staticmethod
    def create_section(title: str) -> 'SectionModel':
        """
        Create new section if the params fields are valid and section is not created before.
        :param title: "section title",
        :return:
        """
        section = SectionModel(title=title)
        section.save_to_db()
        return section

    @staticmethod
    def find_section_by_title(title: str) -> 'SectionModel':
        """
        Find section that has the given title (if any).
        :param title: title of the section
        :return: SectionModel object (or None)
        """
        return SectionModel.query.filter_by(title=title).first()
