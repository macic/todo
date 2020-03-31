from typing import Tuple, Optional
from starlette.responses import JSONResponse
from app.db.session import db_session
from app.schemas.item import ItemCreate
from app.schemas.slack import Command as CommandSchema
from app.handlers.base_handler import BaseHandler
from app.crud import item
from app.utils import log


class EditItem(BaseHandler):

    def parse_text(self, rest: str):
        pass

    def handle(self, full_command: CommandSchema):
        last_priority = item.get_last_priority_by_user_id(db_session=db_session, user_id=full_command.user_id)
        self.obj = item.create(db_session=db_session,
                               obj_in=ItemCreate(title=title,
                                                 user_id=full_command.user_id,
                                                 user_name=full_command.user_name,
                                                 priority=last_priority + 1))

    def response(self):
        return JSONResponse({"text": "Added fine."})
