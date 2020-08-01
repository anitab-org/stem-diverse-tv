from flask_restplus import Api

from .content import api as ns1



api = Api(
    title='STEM Diverse TV',
    version='1.0',
    description='',
)

api.add_namespace(ns1)
