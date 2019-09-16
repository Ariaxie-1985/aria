# coding:utf-8
# @Time  : 2019-02-15 15:34
# @Author: Xiawang
import sys
sys.path.append('.')
from flask import Flask, config
from flask_restful import Api
from flask_cors import CORS
from flask_docs import ApiDoc
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

flask_bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    with app.app_context():
        flask_bcrypt.init_app(app)
        CORS(app)
        login_manager.init_app(app)
        app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'

        cors = CORS(app, resources={r"/*": {"origins": "*"}})

        ApiDoc(app)

        api = Api(app)
        app.config['API_DOC_MEMBER'] = ['api', 'platform']

        from backend.resources.user import user
        app.register_blueprint(user)

        from backend.resources.spring import spring
        app.register_blueprint(spring)

        from backend.resources.data import data
        app.register_blueprint(data)

        app.config.from_object(config)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=18980)
