import tornado.ioloop
import tornado.web

from duodigito_handler import DuodigitoHandler


def make_app():
    return tornado.web.Application([
        (r"/calculate", DuodigitoHandler),
    ])

def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()