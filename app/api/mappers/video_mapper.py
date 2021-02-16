"""
Mapping from model object to representation object"
"""
from typing import List
from app.database.models.video import VideoModel
from datetime import datetime


def map_to_dto(video: "VideoModel"):
    """
    :param video: VideoModel object
    :return: corresponding response made by mapping object to DTO
    """
    return video.json() if video else None


def map_to_feed_dto(video: "VideoModel", stream_url: str):
    """
    Maps VideoModel to feed representation
    :param video: VideoModel
    :return: Feed json
    """
    return {
        "author": {"name": _map_authors_data(video.authors)},
        "type": {"value": "video"},
        "id": video.id,
        "title": video.title,
        "summary": None,  # we don't have this field in the database at the moment
        "published": datetime.strftime(video.date_published, "%Y-%m-%d %H:%M:%S"),
        "updated": datetime.strftime(
            video.date_published, "%Y-%m-%d %H:%M:%S"
        ),  # we don't have this field, use date_published
        "content": {"src": stream_url, "type": "video/hls"},
        "link": None,  # TEST
        "media_group": [
            {
                "type": "image",
                "media_item": [
                    {
                        "key": "image_base",
                        "src": video.preview_url,
                        "type": "extern_image",
                    }
                ],
            }
        ],
        "extensions": {"section": None},
    }


# helpers
def _map_authors_data(authors: List["AuthorModel"]):
    if not authors:
        return None
    return ", ".join([author.name for author in authors])
