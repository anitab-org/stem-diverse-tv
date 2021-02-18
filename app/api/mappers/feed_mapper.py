from typing import List


def map_to_dto(section: "SectionModel", videos: List["dict"]):
    return {
        "type": {"value": "feed"},
        "id": section.id,
        "title": section.title,
        "media_group": [],
        "entry": videos,
    }
