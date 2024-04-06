import time

from flask import jsonify, request
from flask_restful import Resource, reqparse


class SignIn(Resource):
    def __init__(self):
        self.auth_data_parser = reqparse.RequestParser()
        self.auth_data_parser.add_argument('email', type=str, required=True, help='email is needed')
        self.auth_data_parser.add_argument('password', type=str, required=True, help='password is needed')

    def post(self):
        args = self.auth_data_parser.parse_args()
        email = args['email']
        password = args['password']
        access_token = 'suadtfagdvcdc'
        data = {
            'code': 0,
            'message': None,  # None或者不写此字段，dio解析到的就是null
            'data': {
                'token': access_token
            }
        }
        time.sleep(2)
        return jsonify(data)


class SignUp(Resource):
    def __init__(self):
        self.auth_data_parser = reqparse.RequestParser()
        self.auth_data_parser.add_argument('email', type=str, required=True, help='email is needed')
        self.auth_data_parser.add_argument('password', type=str, required=True, help='password is needed')

    def post(self):
        args = self.auth_data_parser.parse_args()
        email = args['email']
        password = args['password']
        access_token = 'suadtfagdvcdc'
        data = {
            'code': 0,
            'message': None,  # None或者不写此字段，dio解析到的就是null
            'data': {
                'token': access_token
            }
        }
        time.sleep(2)
        return jsonify(data)


test_global = 0


class CheckCode(Resource):
    def __init__(self):
        self.auth_data_parser = reqparse.RequestParser()
        self.auth_data_parser.add_argument('token', type=str, required=True, help='token is needed')
        self.auth_data_parser.add_argument('code', type=str, required=True, help='code is needed')

    def post(self):
        global test_global
        test_global += 1
        args = self.auth_data_parser.parse_args()
        code = args['code']
        token= args['token']
        data = {
            'code': 0,
            'message': None,  # None或者不写此字段，dio解析到的就是null
            'data': {
                'match': True
            }
        }
        time.sleep(1)
        print(test_global)
        return jsonify(data)


class RequestSendVeriCode(Resource):
    def __init__(self):
        self.auth_data_parser = reqparse.RequestParser()
        self.auth_data_parser.add_argument('token', type=str, required=True, )

    def post(self):
        args = self.auth_data_parser.parse_args()
        token = args['token']
        data = {
            'code': 0,
            'message': None,  # None或者不写此字段，dio解析到的就是null
            'data': None
        }
        time.sleep(2)
        return jsonify(data)


class UpdateUserInfo(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        # self.parser.add_argument('token', type=str, required=True)
        # self.parser.add_argument('name', type=str, required=False,)
        # self.parser.add_argument('birthday', type=str, required=False,)
        # self.parser.add_argument('gender', type=bool, required=False)
        # self.parser.add_argument('file', type=FileStorage, required=False)
        # self.parser.add_argument('role', type=int, required=False)
        # self.parser.add_argument('goal', type=int, required=False)

    def post(self):
        # args = self.parser.parse_args()
        token = request.form.get('token')
        name = request.form.get('name')
        birthday = request.form.get('birthday')
        gender = request.form.get('gender')
        img = request.files.get('avater')
        role = request.form.get('role')
        goal = request.form.get('goal')
        # 保存图片
        if img is not None:
            img.save('static/avatar' + img.filename)
            print(img)
        data = {
            'code': 0,
            'message': None,  # None或者不写此字段，dio解析到的就是null
            'data': None
        }
        time.sleep(2)
        return jsonify(data)
