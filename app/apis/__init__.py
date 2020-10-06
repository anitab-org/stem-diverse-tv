from flask_restplus import Api

from .video import api as ns1
from .author import author_ns as ns2
from .user import user_ns as ns3



api = Api(
    title='STEM Diverse TV',
    version='0.1.0',
    description='',
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)
