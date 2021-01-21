from random import randrange
from .requester import Requester

class Funny:
    def __init__(self, requester):
        self.requester = requester
        self.messageFuncs = [
            {"name": "Advice", "func": self.advice},
            {"name": "Chuck Norris Joke", "func": self.chucknorris},
            {"name": "Dad Joke", "func": self.dadjoke},
        ]

    def advice(self):
        j = self.requester.get('https://api.adviceslip.com/advice')
        if 'slip' in j and 'advice' in j['slip']:
            return {"message": j['slip']['advice']}
        return j

    def chucknorris(self):
        j = self.requester.get('https://api.chucknorris.io/jokes/random')
        if 'value' in j:
            return {"message": j['value']}
        return j

    def dadjoke(self):
        headers = {"Accept": "application/json"}
        j = self.requester.get('https://icanhazdadjoke.com/', headers=headers)
        if 'joke' in j:
            return {"message": j['joke']}
        return j

    def getmessage(self, index):
        if index >= 0 and index < len(self.messageFuncs):
            m = self.messageFuncs[index]
            return {"message": m["name"] + ": " + m["func"]()["message"]}
        return "Bad message index"

    def random_message(self):
        return self.getmessage(randrange(len(self.messageFuncs)))
