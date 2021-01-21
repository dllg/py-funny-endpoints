from flask import Flask
from .funny import Funny
from .requester import Requester

def SetupRoute(requester) -> Flask:
    app = Flask(__name__)
    funny = Funny(requester)

    @app.route('/v1/advice')
    def advice():
        return funny.advice()

    @app.route('/v1/chucknorris')
    def chucknorris():
        return funny.chucknorris()

    @app.route('/v1/dadjoke')
    def dadjoke():
        return funny.dadjoke()

    @app.route('/v1/random')
    def random():
        return funny.random_message()

    return app
