import sys
from peewee import SqliteDatabase, Model
from app.config import SQLITE_DB_PATH

db = SqliteDatabase(SQLITE_DB_PATH)

def setup(*models: Model) -> None:
    db.connect(reuse_if_open=True)

    if '--drop' in sys.argv[1:]:
        for model in models:
            model.drop_table(safe=True)

    db.create_tables(models, safe=True)

def close() -> None:
    if not db.is_closed():
        db.close()
