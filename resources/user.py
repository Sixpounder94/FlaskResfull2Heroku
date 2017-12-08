import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank"
                        )


    def post(self):
        data = UserRegister.parser.parse_args()
        res = UserModel.find_by_username(data['username'])

        if res:
            return {'message': 'username already exists!!!!'}

        new_user = UserModel(**data)
        new_user.save_to_db()
        return {'message':'User created'},201



