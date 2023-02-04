## Taras Devil Web
Web application for pet project

## Setup
```shell
# Create & activate virtual environment
python3 -m venv "venv"
source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt
```

## Start
```shell
uvicorn app.main:app --reload
```

## Database
### Alembic
```shell
# Create db
sqlite3 name.db

# Init alembic
alembic init alembic

#Create revision
alembic revision --autogenerate  -m "initial"

#Upgrade db to latest revision
alembic upgrade head
```