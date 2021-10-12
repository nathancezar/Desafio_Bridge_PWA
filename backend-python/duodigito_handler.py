import json
import traceback

from base_handler import BaseHandler
from database.controllers.duodigito_controller import DuodigitoController


class DuodigitoHandler(BaseHandler):
    def post(self):
        try:
            request = json.loads(self.request.body)
            duodigitoController = DuodigitoController()
            result = duodigitoController.calculate(request["number"])
            if result is not None:
                self.set_status(200)
                self.write(result)
            else:
                self.set_status(401)
        except Exception as ex:
            traceback.print_exc()
            self.set_status(500)