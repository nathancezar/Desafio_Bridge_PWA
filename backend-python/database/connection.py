from peewee import SqliteDatabase, Model

database = SqliteDatabase(("database/duodigito.db"), pragmas={
    'foreign_keys': 1,
})


class BaseModel(Model):
    class Meta:
        database = database