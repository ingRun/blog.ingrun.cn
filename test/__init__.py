from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app, prefix="/v1", title="Users", description="Users CURD api.")

@api.route('/users')
class UserApi(Resource):
    def get(self):
        return {'user': '1'}

@api.route('/getUser/<int:iid>')
class GetUserInfo(Resource):
    def get(self, iid):
        return {'user': iid}


if __name__ == '__main__':
    app.run()
