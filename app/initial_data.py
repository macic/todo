import logging

from app.db.init_db import init_db
from app.db.session import db_session, engine
from app.utils import log


def init():
    try:
        # Try to create session to check if DB is awake
        db_session.execute("SELECT 1")
    except Exception as e:
        log.error(e)
        raise e
    init_db(db_session, engine)


def main():
    log.info("Creating initial data")
    init()
    log.info("Initial data created")


if __name__ == "__main__":
    main()
