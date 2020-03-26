from app.main import app as main_app
from app.db.session import db_session
from app import crud
from starlette.testclient import TestClient
import urllib

client = TestClient(main_app)
import json

default_headers = {"Content-type": "application/x-www-form-urlencoded"}
thedata2 = {'token': 'i1WdxMDKKcKk1poifqbYhZ4X',
            'team_id': 'T010E6NLJTX',
            'team_domain': 'app-tests-group',
            'channel_id': 'D01093L4CNM',
            'channel_name': 'directmessage',
            'user_id': 'U010DN4S2DA',
            'user_name': 'radoslaw.jeruzal',
            'command': '/todo',
            'text': 'add zajebiście',
            'response_url': 'https://hooks.slack.com/commands/T010E6NLJTX/1015703244994/44Xn80UxNd6VQUkPueLh75FK',
            'trigger_id': '1016737228323.1014226698949.c22285eb0dcacaecc9fd444aeee783ec'}


def test_hello_world():
    response = client.get(
        f"/",
        headers=default_headers
    )

    assert response.status_code == 200


def test_simple_add():
    response = client.post(
        f"/task/",
        data=urllib.parse.urlencode(thedata2),
        headers=default_headers
    )
    assert response.status_code == 200
    assert response.content == True
    items = crud.item.get_multi_by_owner(db_session, 'U010DN4S2DA')
    assert len(items) == 1
