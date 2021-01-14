"""
Mapping from model object to representation object"
"""

from app.database.models.video import VideoModel


def map_to_dto(video: 'VideoModel'):
    """
    :param video: VideoModel object
    :return: corresponding response made by mapping object to DTO
    """
    return video.json() if video else None