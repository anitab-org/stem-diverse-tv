from flask_restplus import Api

from .video import video_ns as ns1
from .author import author_ns as ns2
from .user import user_ns as ns3
from .section import section_ns


api = Api(
    title='STEM Diverse TV',
    version='0.1.0',
    description='',
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
api.add_namespace(section_ns)