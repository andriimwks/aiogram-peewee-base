from peewee import Model, IntegerField, TextField
from app.models.db import db

class User(Model):
    id = IntegerField(null=False, unique=True)
    first_name = TextField(null=False)
    last_name = TextField(null=True)
    username = TextField(null=True)
    language_code = TextField(null=False)

    class Meta:
        database = db
