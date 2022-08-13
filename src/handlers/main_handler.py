from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    def get(self):
        response = {"response": [{
            "app": "DataTraker",
            "version": "1.0"
        }]}
        self.write(response)
