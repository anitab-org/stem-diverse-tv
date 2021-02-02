from app.database.models.video import VideoModel
from typing import List


class VideoDAO:
    @staticmethod
    def create_video(
        title: str,
        url: str,
        preview_url: str,
        date_published: str,
        source: str,
        channel: str,
        duration: str,
        archived: bool,
        free_to_reuse: bool,
        authorized_to_reuse: bool,
    ):
        """
        Create new video if the params fields are valid
        :param title: video title <str>,
        :param url: video url <str>
        :param preview_url: video preview content <str>
        :param date_published: date of video publishing <str>
        :param source: source of the video <str>
        :param channel: channel to which video belongs <str>
        :param duration: video duration in seconds <int>
        :param archived: is video archived <str>
        :param free_to_reuse: is video free to reuse <bool>
        :param authorized_to_reuse:  has authorization to use <bool>
        :return: Video object
        """
        video = VideoModel(
            title=title,
            url=url,
            preview_url=preview_url,
            date_published=date_published,
            source=source,
            channel=channel,
            duration=duration,
            archived=archived,
            free_to_reuse=free_to_reuse,
            authorized_to_reuse=authorized_to_reuse,
        )
        video.save_to_db()
        return video

    @staticmethod
    def find_video_by_url(url: str) -> "VideoModel":
        return VideoModel.query.filter_by(url=url).first()

    # associated model methods
    # authors
    @staticmethod
    def add_video_authors(video: "VideoModel", authors: List["AuthorModel"]) -> None:
        video.add_authors(authors)

    @staticmethod
    def replace_video_authors(
        video: "VideoModel", authors: List["AuthorModel"]
    ) -> None:
        video.update_authors(authors)

    @staticmethod
    def remove_video_authors(video: "VideoModel") -> None:
        video.remove_all_authors()

    # sections
    @staticmethod
    def add_video_sections(video: "VideoModel", sections: List["SectionModel"]) -> None:
        video.add_sections(sections)

    @staticmethod
    def replace_video_sections(
        video: "VideoModel", sections: List["SectionModel"]
    ) -> None:
        video.update_sections(sections)

    @staticmethod
    def remove_video_sections(video: "VideoModel") -> None:
        video.remove_all_sections()
