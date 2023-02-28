# aiogram-peewee-base

## Installation
Run following commands in your terminal:
```console
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pybabel compile -d locales -D bot
```
Create .env file:
```
TELEGRAM_TOKEN=...
SQLITE_DB_PATH=bot.db
LOCALES_DIR=locales
I18N_DOMAIN=bot
```

## Usage
```console
python -m app
```

## Extras
Extract texts:
```console
pybabel extract --input-dirs=app -o locales/bot.pot
```
Create .po files for different languages:
```console
pybabel init -i locales/bot.pot -d locales -D bot -l en
pybabel init -i locales/bot.pot -d locales -D bot -l uk
```
