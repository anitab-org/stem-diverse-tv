from flask_restplus import Namespace, Resource
from flask import request

from app.utils.extract_video_id import extract_video_id
from app.utils.messages import SECTION_ID_NOT_PROVIDED, RESOURCE_NOT_FOUND
from app.utils.youtube_dl import youtube_dl_extract_info, youtube_dl_extract_format
from ..dao.section_dao import SectionDAO
from ..mappers.video_mapper import map_to_feed_dto
from app.api.mappers import feed_mapper

feed_ns = Namespace("feed", description="Feed endpoints")


@feed_ns.route("/")
class Feed(Resource):
    DEFAULT_VIDEO_FORMAT = 22

    @feed_ns.doc(
        "section feed",
        params={
            "section_id": "id of the section",
        },
    )
    def get(self):
        query_params = request.args
        section_id = query_params.get("section_id")
        if not section_id:
            return SECTION_ID_NOT_PROVIDED, 400
        section = SectionDAO.find_section_by_id(section_id)
        if not section:
            return RESOURCE_NOT_FOUND, 404
        videos = section.videos
        videos_data = []
        for video in videos:
            stream_url = video.url
            if "youtube" in video.url:
                yt_id = extract_video_id(video.url)
                video_info = youtube_dl_extract_info(yt_id)
                stream_data = youtube_dl_extract_format(
                    video_info, Feed.DEFAULT_VIDEO_FORMAT
                )
                if "message" in stream_data or len(stream_data) == 0:
                    return stream_data, 500
                stream_url = stream_data[0]

            video_dto = map_to_feed_dto(video, stream_url)
            videos_data.append(video_dto)
        return feed_mapper.map_to_dto(section, videos_data), 200
