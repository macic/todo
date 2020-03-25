import pytest
from sqlalchemy.exc import ProgrammingError

from app.db.init_db import init_db
from app.db.session import db_session, engine
from app.db.base_class import Base
from app.utils import log

@pytest.fixture(autouse=True, scope="module")
def database_service():
    init_db(db_session, engine)

@pytest.fixture(autouse=True)
def cleanup_service(database_service):
    yield
    tables = reversed(Base.metadata.sorted_tables)

    for table in tables:
        try:
            db_session.execute(f"truncate table {table.name} cascade;")
        except ProgrammingError:
            log.warning("table does not exist", table=table)
