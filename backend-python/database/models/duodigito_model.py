from peewee import FloatField
from database import connection


class DuodigitoModel(connection.BaseModel):
    number = FloatField()
    result = FloatField()


    class Meta:
        table_name = "duodigito"

def getByNumber(number):
    try:
        return DuodigitoModel.select().where(DuodigitoModel.number == number).get()
    except DuodigitoModel.DoesNotExist:
        return None
    except Exception as ex:
        raise ex
