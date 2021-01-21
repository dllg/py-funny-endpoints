import requests

class Requester:
    def get(self, url, headers={}):
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            return {"error": "Cannot connect to " + url, "code": r.status_code}
