from flask import abort, request
from flask_restx import Namespace, Resource, fields

from src.api import repository
from src.api.users.models import User

ns = Namespace("users")

user_model = ns.model("User", {"id": fields.Integer, "name": fields.String})

user_input_model = ns.model(
    "User",
    {"name": fields.String(required=True), "password": fields.String(required=True)},
)


@ns.route("/")
class UserListResource(Resource):

    @ns.marshal_list_with(user_model)
    def get(self):
        return repository.get_all(User), 200

    @ns.marshal_with(user_model)
    @ns.expect(user_input_model)
    def post(self):
        data = request.get_json()
        user = User(name=data.get("name"), password=data.get("password"))
        return repository.create(user), 201


@ns.route("/<int:id>")
class UserResource(Resource):

    @ns.marshal_with(user_model)
    def get(self, id):
        user = repository.get_by_id(User, id)
        if not user:
            abort(404, f"User with id {id} was not found!!!")
        return user, 200

    @ns.marshal_with(user_model)
    @ns.expect(user_input_model)
    def put(self, id):
        data = request.get_json()
        user = repository.update(User, id, data)
        if not user:
            abort(404, f"User with id {id} was not found!!!")
        return user, 200

    def delete(self, id):
        user = repository.delete(User, id)
        if not user:
            abort(404, f"User with id {id} was not found!!!")
        return user, 204
