from .router import SetupRoute
from .requester import Requester

def main():
    app = SetupRoute(Requester())
    app.run(host='0.0.0.0')

if __name__ == '__main__':
   main()
