import os, pathlib, dotenv

dotenv.load_dotenv()

_BASE_DIR = pathlib.Path(__file__).parent.parent
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
SQLITE_DB_PATH = _BASE_DIR / os.environ.get('SQLITE_DB_PATH')
LOCALES_DIR = _BASE_DIR / os.environ.get('LOCALES_DIR')
I18N_DOMAIN = os.environ.get('I18N_DOMAIN')
