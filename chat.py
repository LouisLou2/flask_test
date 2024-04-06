import time

from flask import jsonify, request
from flask_restful import Resource, reqparse

from test_data import chat_sessions, bot_ques_answers, bot_normal_answers, title_examples

get_answer_times = 0
chat_id = 1000


class GetChatSession(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('token', type=str, required=True)
        self.parser.add_argument('page', type=int, required=True)

    def post(self):
        args = self.parser.parse_args()
        token = args['token']
        page = args['page']
        data = {
            'code': 0,
            'message': None,  # None或者不写此字段，dio解析到的就是null
            'data': chat_sessions[page * 10: (page + 1) * 10]
        }
        time.sleep(2)
        return jsonify(data)


class GetAnswer(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('token', type=str, required=True)
        self.parser.add_argument('chatId', type=int, required=True)
        self.parser.add_argument('ques', type=str, required=True)

    def post(self, ):
        global get_answer_times
        args = self.parser.parse_args()
        token = args['token']
        chat_id = args['chatId']
        ques = args['ques']
        data = {
            'code': 0,
            'message': None,  # None或者不写此字段，dio解析到的就是null
            'data': {
                'ans': bot_ques_answers[get_answer_times % len(bot_ques_answers)],
            }
        }
        get_answer_times += 1
        time.sleep(1)
        return jsonify(data)


class NewChat(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('token', type=str, required=True)
        self.parser.add_argument('ques', type=str,
                                 required=True)  # 用户关于问题的提问，如果此次回答并非来自一个具体问题，只是普通Ti问，下面的fromQues字段为False
        self.parser.add_argument('fromQues', type=bool, required=True)

    def post(self):
        global chat_id
        global get_answer_times
        args = self.parser.parse_args()
        token = args['token']
        ques = args['ques']
        fromQues = args['fromQues']
        data = {
            'code': 0,
            'message': None,  # None或者不写此字段，dio解析到的就是null
            'data': {
                'chatId': chat_id,
                'ans': bot_ques_answers[get_answer_times % len(bot_ques_answers)],
                'title': title_examples[chat_id % len(title_examples)],
            }
        }
        chat_id += 1
        get_answer_times += 1
        time.sleep(1)
        return jsonify(data)


class GetChatHistory(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('token', type=str, required=True)
        self.parser.add_argument('chatId', type=int, required=True)
        self.parser.add_argument('page', type=int, required=True)

    def post(self):
        args = self.parser.parse_args()
        token = args['token']
        page = args['page']
        data = {
            'code': 0,
            'message': None,  # None或者不写此字段，dio解析到的就是null
            'data': chat_sessions[page * 10: (page + 1) * 10]
        }
        time.sleep(2)
        return jsonify(data)
