import sys
from database import connection
from database.models import duodigito_model
from database.models.duodigito_model import DuodigitoModel

sys.path.append('..')
from engine.calculate_duodigito import Duodigit


class DuodigitoController():
    def __init__(self):
        connection.database.connect(reuse_if_open=True)

    def calculate(self, number):
        try:
            duodigit_instance = Duodigit(number)
            result = duodigit_instance.check_duodigit()
            old_duodigit = duodigito_model.getByNumber(number)
            if not old_duodigit:
                self.insertNewDuodigit(number, result['duodigit'])
            return result
        except Exception as ex:
            raise ex

    def insertNewDuodigit(self, number, result):
        with connection.database.atomic() as transaction:
            try:
                DuodigitoModel.create(
                    number=float(number),
                    result=float(result)
                )
            except Exception as e:
                transaction.rollback()
                raise e

    def close(self):
        connection.database.close()
