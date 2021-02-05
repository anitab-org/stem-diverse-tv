from flask import request
from flask_restplus import Namespace, Resource
from app.database.models.category import CategoryModel
from app.api.middlewares.auth import token_required

category_ns = Namespace("category", description="Category Details")


@category_ns.route("/")
class Category(Resource):
    @token_required
    @category_ns.doc(params={"title": "Title of category"})
    @category_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def post(self):
        args = request.args
        title = args["title"]
        existing_category = CategoryModel.find_by_title(title)
        if existing_category:
            return {"message": "Category already exists"}, 409

        """ Saving title in capitalized letter. Which can prevent inconsistency in finding existing category title. """
        category = CategoryModel(title.capitalize())
        category.save_to_db()

        return {"message": "Category added"}, 201

@category_ns.route("/all")
class AllCategories(Resource):
    def get(self):
        category_models = CategoryModel.query.all()
        result = list(map(lambda category: category.json(), category_models))
        return {"categories": result}, 200

