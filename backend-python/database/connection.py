import os
from peewee import SqliteDatabase, Model

dirpath = os.path.abspath(os.path.dirname(__file__))
dirpath = dirpath[:dirpath.find("backend-python")]
path = lambda string: os.path.join(dirpath, string)

database = SqliteDatabase(path("database/duodigito.db"), pragmas={
    'foreign_keys': 1,
})


class BaseModel(Model):
    class Meta:
        database = database