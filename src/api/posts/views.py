from flask_restx import Resource, Namespace, fields
from flask import request, abort
from src.api.posts.models import Post
from src.api.db import get_db_session
from flask_restx import fields
from src.api import repository

ns = Namespace("posts")

post_model = ns.model(
    "Post", {
        "id": fields.Integer,
        "title": fields.String,
        "content": fields.String,
        "date_posted": fields.DateTime,
        "user_id": fields.Integer
    }
)

post_input_model = ns.model(
    "Post", {
        "title": fields.String(required=True),
        "content": fields.String(required=True),
        "user_id": fields.Integer(required=True)
    }
)

@ns.route("/")
class PostListResource(Resource):

    @ns.marshal_list_with(post_model)
    def get(self):
        with get_db_session() as session:
            return repository.get_all(Post), 200

    @ns.marshal_with(post_model)
    @ns.expect(post_input_model)
    def post(self):
        data = request.get_json()
        post = Post(
            title = data.get("title"),
            content = data.get("content"),
            user_id = data.get("user_id")
        )
        return repository.create(post), 201


@ns.route("/<int:id>")
class PostResource(Resource):

    @ns.marshal_with(post_model)
    def get(self, id):
        post = repository.get_by_id(Post, id)
        if not post:
            abort(404, f"Post with id {id} was not found!!!")
        return post, 200


    @ns.marshal_with(post_model)
    @ns.expect(post_input_model) 
    def put(self, id):
        data = request.get_json()
        post = repository.update(Post, id, data)
        if not post:
            abort(404, f"Post with id {id} was not found!!!")
        return post, 200

    @ns.marshal_with(post_model)
    def delete(self, id):
        post = repository.delete(Post, id)
        if not post:
            abort(404, f"Post with id {id} was not found!!!")
        return post, 204