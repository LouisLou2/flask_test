# using flask_restful
import os

from flask import Flask, send_file, abort, send_from_directory
from flask_restful import Api
from werkzeug.security import safe_join

from chat import GetAnswer, GetChatSession, NewChat
from note import GetNoteFile
from ques import *
from user_auth import *

# creating the flask app 
app = Flask(__name__)
# creating an API object 
api = Api(app)

api.add_resource(SignIn, '/account/sign_in')
api.add_resource(SignUp, '/account/sign_up')
api.add_resource(CheckCode, '/account/check_code')
api.add_resource(RequestSendVeriCode, '/account/request_veri_code')
api.add_resource(UpdateUserInfo, '/account/update_info')

api.add_resource(Ques, '/ques/search_ques')
api.add_resource(QusByQuesId, '/ques/search_quesId')
api.add_resource(RecommendQues, '/ques/recommend')

api.add_resource(GetChatSession, '/chat/chat_session')
api.add_resource(GetAnswer, '/chat/ongoing')
api.add_resource(NewChat, '/chat/new')

api.add_resource(GetNoteFile, '/note/get_note_url')

FILES_DIRECTORY = './gen'


@app.route('/gen/<path:filename>')
def download_file(filename):
    try:
        # 确保文件路径安全，防止路径遍历
        safe_path = safe_join(FILES_DIRECTORY, filename)
        # 检查文件是否真实存在
        if not os.path.exists(safe_path):
            # 如果文件不存在，返回404错误
            abort(404)
        # 从安全路径发送文件
        return send_from_directory(FILES_DIRECTORY, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


# driver function
if __name__ == '__main__':
    app.run(debug=True)
