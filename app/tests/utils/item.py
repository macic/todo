from app import crud
from app.db.session import db_session
from app.schemas.item import ItemCreate
from app.tests.utils.utils import random_lower_string
from random import randint

def create_random_item(user_id=1, priority=None):
    title = random_lower_string()
    if not priority:
        priority = randint(0,1000)
    item_in = ItemCreate(title=title, priority=priority)
    return crud.item.create_with_owner(
        db_session=db_session, obj_in=item_in, user_id=user_id
    )
