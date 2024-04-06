import time

from flask import jsonify, request, app
from flask_restful import Resource, reqparse


class GetNoteFile(Resource):
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
        file = request.files.get('file')
        # 保存图片
        if file is not None:
            file.save('static/note' + file.filename)
            print(file)
        data = {
            'code': 0,
            'message': None,  # None或者不写此字段，dio解析到的就是null
            'data': {
                'fileUrl': 'http://192.168.5.101:8091/gen/note/def_note.pdf',
            }
        }
        time.sleep(2)
        return jsonify(data)

