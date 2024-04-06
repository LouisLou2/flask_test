import time

from flask import jsonify, request
from flask_restful import Resource, reqparse

from test_data import ques_explaination, ques_recommend, ques_explaination_byQuesId

ques_times = 0


class Ques(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        global ques_times
        # args = self.parser.parse_args()
        token = request.form.get('token')
        img = request.files['pic']
        # 保存图片
        img.save('static/ques_pic/' + img.filename)
        print(img)
        ques_times += 1
        data = None
        if ques_times % 2 == 1:
            data = ques_explaination[0]
        else:
            data = ques_explaination[1]
        time.sleep(2)
        return jsonify(data)


class QusByQuesId(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('token', type=str, required=True)
        self.parser.add_argument('quesId', type=int, required=True)

    def post(self):
        args = self.parser.parse_args()
        token = args['token']
        ques_id = args['quesId']
        print('ques_id:', ques_id),
        res = {
            'code': 0,
            'message': None,
            'data': ques_explaination_byQuesId[ques_id]
        }
        time.sleep(1)
        return jsonify(res)


class RecommendQues(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('token', type=str, required=True)
        self.parser.add_argument('quesId', type=int, required=False)
        self.parser.add_argument('ques', type=str, required=False)

    def post(self):
        args = self.parser.parse_args()
        token = args['token']
        ques_id = args['quesId']
        ques = args['ques']
        # ques和quesId只能有一个, 如果说这道题题库中有，那么肯定客户端发quesId,因为你在之前发的数据就有quesId,但是如果之前的解释题库没有，当时quesId就是空的，这时会直接发ques，根据ques提供相似题目
        res = {
            'code': 0,
            'message': None,
            'data': ques_recommend
        }
        time.sleep(1)
        return jsonify(res)
