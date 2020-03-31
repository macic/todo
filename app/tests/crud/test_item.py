from app import crud
from app.schemas.item import ItemCreate, ItemUpdate
from app.tests.utils.utils import random_lower_string
from app.db.session import db_session


def test_create_item():
    title = random_lower_string()
    priority = 123
    user_id = 'C@234'
    user_name = 'user.name'
    item_in = ItemCreate(title=title, priority=priority, user_id=user_id, user_name=user_name)
    item = crud.item.create(db_session=db_session, obj_in=item_in)
    assert item.title == title
    assert item.priority == priority
    assert item.user_id == user_id


def test_get_item(item):
    stored_item = crud.item.get(db_session=db_session, id=item.id)
    assert item.id == stored_item.id
    assert item.title == stored_item.title
    assert item.priority == stored_item.priority
    assert item.user_id == stored_item.user_id

def test_get_items_by_user_id(item):
    stored_items = crud.item.get_multi_by_user_id(db_session=db_session, user_id="non_existant")
    assert stored_items == []

    stored_items = crud.item.get_multi_by_user_id(db_session=db_session, user_id=item.user_id)
    assert item.id == stored_items[0].id
    assert item.title == stored_items[0].title
    assert item.priority == stored_items[0].priority
    assert item.user_id == stored_items[0].user_id

def test_get_item_by_priority_and_user_id(item):
    stored_item = crud.item.get_by_priority_and_user_id(db_session=db_session, priority=item.priority, user_id=item.user_id)
    assert item.id == stored_item.id
    assert item.title == stored_item.title
    assert item.priority == stored_item.priority
    assert item.user_id == stored_item.user_id

def test_update_item(item):
    title2 = random_lower_string()
    item_update = ItemUpdate(title=title2)
    item2 = crud.item.update(db_session=db_session, db_obj=item, obj_in=item_update)
    assert item.id == item2.id
    assert item.title == item2.title
    assert item2.title == title2
    assert item.user_id == item2.user_id


def test_delete_item(item):
    item2 = crud.item.remove(db_session=db_session, id=item.id)
    item3 = crud.item.get(db_session=db_session, id=item.id)
    assert item3 is None
    assert item2.id == item.id
    assert item2.title == item.title
    assert item2.user_id == item.user_id
