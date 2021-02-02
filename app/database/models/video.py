from datetime import datetime
from typing import Dict, List

from app.database.sqlalchemy_extension import db


class VideoModel(db.Model):
    # Specifying table
    __tablename__ = "videos"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    url = db.Column(db.Text(), unique=True)
    preview_url = db.Column(db.Text())
    title = db.Column(db.String(200))
    date_published = db.Column(db.Date)
    source = db.Column(db.String(50), default="Youtube")
    channel = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    archived = db.Column(db.Boolean)
    free_to_reuse = db.Column(db.Boolean)
    authorized_to_reuse = db.Column(db.Boolean)

    def json(self):
        """Returns VideoModel object in json format."""
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "preview_url": self.preview_url,
            "title": self.title,
            "date_published": datetime.strftime(self.date_published, "%Y-%m-%d"),
            "source": self.source,
            "channel": self.channel,
            "duration": self.duration,
            "archived": self.archived,
            "free_to_reuse": self.free_to_reuse,
            "authorized_to_reuse": self.authorized_to_reuse,
        }

    def find_by_id(cls, _id: int) -> "VideoModel":
        """Returns a particular video of given id."""
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        """Add video to database"""
        db.session.add(self)
        db.session.commit()

    def update(self, new_data: Dict[str, object]) -> None:
        """Update existing video with new data"""
        for field in new_data:
            if hasattr(self, field):
                setattr(self, field, new_data[field])
        db.session.commit()

    def delete_from_db(self) -> None:
        """Deletes video from the database."""
        db.session.delete(self)
        db.session.commit()

    # authors association
    def add_authors(self, authors: List["AuthorModel"]) -> None:
        """
        Add video authors entities to associated m2m model.
        :param authors: list of authors to add
        :return: None
        """
        self.authors.extend(authors)
        db.session.commit()

    def update_authors(self, authors: List["AuthorModel"]) -> None:
        """
        Replace authors of video -> m2m records
        :param authors: list of new authors
        :return: None
        """
        self.authors = authors
        db.session.commit()

    def remove_all_authors(self):
        """
        Remove all authors of video (clean m2m records)
        :return: None
        """
        self.authors = []
        db.session.commit()

    # authors association
    def add_sections(self, sections: List["SectionModel"]) -> None:
        """
        Add video sections entities to associated m2m model.
        :param sections: list of sections to add
        :return: None
        """
        self.sections.extend(sections)
        db.session.commit()

    def update_sections(self, sections: List["SectionModel"]) -> None:
        """
        Replace sections of video -> m2m records
        :param sections: list of new sections
        :return: None
        """
        self.sections = sections
        db.session.commit()

    def remove_all_sections(self):
        """
        Remove all sections of video (clean m2m records)
        :return: None
        """
        self.sections = []
        db.session.commit()
