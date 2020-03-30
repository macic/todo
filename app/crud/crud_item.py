from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate
from app.crud.base import CRUDBase


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):

    def get_multi_by_user_id(
            self, db_session: Session, *, user_id: str, skip=0, limit=100
    ) -> List[Item]:
        return (
            db_session.query(self.model)
                .filter(Item.user_id == user_id)
                .offset(skip)
                .limit(limit)
                .all()
        )

    def get_last_priority_by_user_id(self, db_session: Session, *, user_id: str) -> int:
        item = (db_session.query(self.model)
                .filter(Item.user_id == user_id)
                .order_by(Item.priority.desc())
                .first()
                )
        return item.priority if item else 0


item = CRUDItem(Item)
