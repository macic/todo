from starlette.responses import JSONResponse
from app.db.session import db_session
from app.schemas.item import ItemCreate
from app.schemas.slack import Command as CommandSchema
from app.handlers.base_handler import BaseHandler
from app.crud import item
from app.utils import log


class AddItemCommand(BaseHandler):

    def handle(self, rest: str, full_command: CommandSchema):
        self.obj = item.create(db_session=db_session,
                    obj_in=ItemCreate(title=rest, user_id=full_command.user_id, user_name=full_command.user_name))

    def response(self):
        return JSONResponse({"text": "Added fine."})