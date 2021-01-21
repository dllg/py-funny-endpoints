from .router import SetupRoute
from .requester import Requester

def main():
    app = SetupRoute(Requester())
    app.run()

if __name__ == '__main__':
   main()
