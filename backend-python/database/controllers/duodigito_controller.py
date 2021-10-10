from database import connection
from database.models import duodigito_model

class DuodigitoController():
    def __init__(self):
        connection.database.connect(reuse_if_open=True)

    def calculate(self, number):
        try:
            duodigito = duodigito_model.getByNumber(number)
            if duodigito:
                return {
                    "result": duodigito.result
                }
            else:
                return None # Calcular duodigito
        except Exception as ex:
            raise ex