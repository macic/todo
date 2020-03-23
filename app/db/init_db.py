from app.db import base


def init_db(db_session, engine):
    base.Base.metadata.create_all(bind=engine)
