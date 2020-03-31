from app.main import app as main_app
from app.db.session import db_session
from app import crud
from starlette.testclient import TestClient
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.schemas.slack import Command
from app.utils import log

client = TestClient(main_app)

thedata2 = {
    "token": "i1WdxMDKKcKk1poifqbYhZ4X",
    "team_id": "T010E6NLJTX",
    "team_domain": "app-tests-group",
    "channel_id": "D01093L4CNM",
    "channel_name": "directmessage",
    "user_id": "U010DN4S2DA",
    "user_name": "radoslaw.jeruzal",
    "command": "/todo",
    "text": "add zajebiście",
    "response_url": "https://hooks.slack.com/commands/T010E6NLJTX/1015703244994/44Xn80UxNd6VQUkPueLh75FK",
    "trigger_id": "1016737228323.1014226698949.c22285eb0dcacaecc9fd444aeee783ec",
}


def test_add_api_item(api_item: Command):
    response = client.post("/task/", data=api_item.dict())

    assert response.status_code == 200
    assert response.json().get("text") == "Added fine."
    items = crud.item.get_multi_by_user_id(db_session, user_id=api_item.user_id)
    assert len(items) == 1


def test_add_item_increases_priority_for_user(api_item: Command):
    client.post("/task/", data=api_item.dict())
    items = crud.item.get_multi_by_user_id(db_session, user_id=api_item.user_id)
    assert len(items) == 1
    assert items[0].priority == 1

    # another item
    item2 = api_item.dict().copy()
    item2.update({"text": "add another"})
    client.post("/task/", data=item2)
    items = crud.item.get_multi_by_user_id(db_session, user_id=api_item.user_id)
    assert len(items) == 2
    assert items[0].priority != items[1].priority

    # another item but for different user
    item3 = api_item.dict().copy()
    item3.update({"user_id": "AN0TH3R"})
    client.post("/task/", data=item3)
    items = crud.item.get_multi_by_user_id(db_session, user_id=item3["user_id"])
    assert len(items) == 1
    assert items[0].priority == 1
