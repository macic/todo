from starlette.responses import JSONResponse
from app.schemas.item import ItemCreate
from app.schemas.slack import Command as CommandSchema
from app.handlers.base_handler import BaseHandler
from app.crud import item


class AddItem(BaseHandler):
    def parse_text(self, text: str) -> None:
        self.title = text

    def handle(self, full_command: CommandSchema):
        last_priority = item.get_last_priority_by_user_id(db_session=self.db_session, user_id=full_command.user_id)
        self.obj = item.create(
            db_session=self.db_session,
            obj_in=ItemCreate(
                title=self.title,
                user_id=full_command.user_id,
                user_name=full_command.user_name,
                priority=last_priority + 1,
            ),
        )

    def response(self):
        return JSONResponse({"text": "Added fine."})
