# Albus

A Telegram Bot that converts documents to more readable formats.

## Usage

```
cp .env.example .env
```

Put your Telegram Bot Token inside `.env`.

### Docker

```
make
make run
```

### Poetry
Ensure `pandoc` and `tectonic` are installed.

```
poetry install
poetry run python -m albus.bot
```
