import pytest
from app import crud
from sqlalchemy.exc import ProgrammingError

from app.db.init_db import init_db
from app.db.session import Session, engine, db_session
from app.db.base_class import Base
from app.schemas.item import ItemCreate, Item
from app.schemas.slack import AddCommand
from app.tests.utils.utils import random_lower_string
from app.utils import log


# @pytest.fixture(autouse=True, scope="module")
# def database_service():
#     init_db(db_session, engine)
#
#
TABLE = "item"
STATEMENT = "TRUNCATE TABLE %s CASCADE"


@pytest.fixture(scope="function", autouse=True)
def clear_tables():
    """
    This fixture will be executed after every test, clearing the
    given table.
    You can remove the autouse, and specify when it executed whenever you want.
    """

    yield
    # db_session.autocommit = True
    db_session.execute("TRUNCATE TABLE item CASCADE")
    db_session.commit()
    # db_session.autocommit = False


# @pytest.fixture(autouse=True, scope="function")
# def cleanup_service():
#     # yield
#     tables = reversed(Base.metadata.sorted_tables)
#
#     for table in tables:
#         try:
#             log.error("TRYING")
#             log.error(table.name)
#             db_session.execute(f"DELETE from sitem")
#             # db_session.execute(f"truncate table {table.name} cascade;")
#         except ProgrammingError:
#             log.warning("table does not exist", table=table)


@pytest.fixture(scope="function")
def item() -> Item:
    title = random_lower_string()
    priority = 123
    user_id = "C@234"
    user_name = "user.name"
    item_in = ItemCreate(title=title, priority=priority, user_id=user_id, user_name=user_name)
    return crud.item.create(db_session=db_session, obj_in=item_in)


@pytest.fixture()
def api_item() -> AddCommand:
    return AddCommand(
        **{
            "token": "i1WdxMDKKcKk1poifqbYhZ4X",
            "team_id": "T010E6NLJTX",
            "team_domain": "app-tests-group",
            "channel_id": "D01093L4CNM",
            "channel_name": "directmessage",
            "user_id": "U010DN4S2DA",
            "user_name": "radoslaw.jeruzal",
            "command": "/todo",
            "text": "add zajebiście to działa",
            "response_url": "https://hooks.slack.com/commands/T010E6NLJTX/1015703244994/44Xn80UxNd6VQUkPueLh75FK",
            "trigger_id": "1016737228323.1014226698949.c22285eb0dcacaecc9fd444aeee783ec",
        }
    )
