# FastAPI CRUD API with PostgreSQL Database

This repository contains a FastAPI-based CRUD (Create, Read, Update, Delete) API for managing items in a PostgreSQL database. It uses the following Python packages: FastAPI, SQLAlchemy, and psycopg2 to interact with a PostgreSQL database hosted on [ElephantSQL](https://api.elephantsql.com/).

## Installation

Before you can run the application, make sure you have the following dependencies installed:

- [Python 3.6+](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [psycopg2](https://pypi.org/project/psycopg2/)
- [uvicorn](https://www.uvicorn.org/)

You can install the required Python packages using `pip`:

```bash
pip install fastapi sqlalchemy psycopg2-binary uvicorn

```

## Configuration
The application is configured to use a PostgreSQL database hosted on ElephantSQL. You will need to replace the database URL in main.py and create_db.py with your own credentials. Update the engine initialization in main.py as follows:

```bash
engine = create_engine('your_postgresql_database_url_here', echo=True)
```

```bash
uvicorn main:app
```

```bash
python create_db.py
```

To be completed....










