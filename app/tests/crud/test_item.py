from app import crud
from app.schemas.item import ItemCreate, ItemUpdate
from app.tests.utils.utils import random_lower_string
from app.db.session import db_session


def test_create_item():
    title = random_lower_string()
    priority = 123
    item_in = ItemCreate(title=title, priority=priority)
    user_id = 'C@234'
    item = crud.item.create_with_owner(
        db_session=db_session, obj_in=item_in, user_id=user_id
    )
    assert item.title == title
    assert item.priority == priority
    assert item.user_id == user_id

def test_get_item():
    title = random_lower_string()
    priority = 123
    item_in = ItemCreate(title=title, priority=priority)
    user_id = 'C@234'
    item = crud.item.create_with_owner(
        db_session=db_session, obj_in=item_in, user_id=user_id
    )
    stored_item = crud.item.get(db_session=db_session, id=item.id)
    assert item.id == stored_item.id
    assert item.title == stored_item.title
    assert item.priority == stored_item.priority
    assert item.user_id == stored_item.user_id
#
def test_update_item():
    title = random_lower_string()
    priority = 123
    item_in = ItemCreate(title=title, priority=priority)
    user_id = 'C@234'
    item = crud.item.create_with_owner(
        db_session=db_session, obj_in=item_in, user_id=user_id
    )
    title2 = random_lower_string()
    item_update = ItemUpdate(title=title2)
    item2 = crud.item.update(db_session=db_session, db_obj=item, obj_in=item_update)
    assert item.id == item2.id
    assert item.title == item2.title
    assert item2.title == title2
    assert item.user_id == item2.user_id
#
#
def test_delete_item():
    title = random_lower_string()
    priority = 123
    item_in = ItemCreate(title=title, priority=priority)
    user_id = 'C@234'
    item = crud.item.create_with_owner(
        db_session=db_session, obj_in=item_in, user_id=user_id
    )
    item2 = crud.item.remove(db_session=db_session, id=item.id)
    item3 = crud.item.get(db_session=db_session, id=item.id)
    assert item3 is None
    assert item2.id == item.id
    assert item2.title == title
    assert item2.user_id == user_id
