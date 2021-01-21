class RequesterMock:
    def __init__(self):
        self.response = {}

    def set_response(self, response):
        self.response = response

    def get(self, url, headers={}):
        return self.response
