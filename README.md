## Taras Devil Web
Web application for pet project

## Setup
```shell
# Create and activate virtual environment
python3 -m venv 'venv'
source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Create database
sqlite3 taras.db

# Upgrade database to latest revision
alembic upgrade head
```

## Start
```shell
uvicorn app.main:app --reload
```

## Development
### Alembic
```shell

# Add models to `alembic/env.py` to autogenerate revisions

# Create revision
alembic revision --autogenerate  -m "message"

# Upgrade database to latest revision
alembic upgrade head
```