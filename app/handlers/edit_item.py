from starlette.responses import JSONResponse

from app.constants import WrongPriorityException
from app.schemas.item import ItemUpdate
from app.schemas.slack import Command as CommandSchema
from app.handlers.base_handler import BaseHandler
from app.crud import item
from app.utils import split_by_first_space, log


class EditItem(BaseHandler):
    def parse_text(self, text: str):
        self.priority, self.title = split_by_first_space(text)

    def handle(self, full_command: CommandSchema):
        self.item_data = item.get_by_priority_and_user_id(
            db_session=self.db_session, priority=self.priority, user_id=full_command.user_id
        )
        if not self.item_data:
            raise WrongPriorityException
        log.info("BEFORE")
        log.info(self.item_data.title)
        log.info(self.item_data.priority)
        self.obj = item.update(
            db_session=self.db_session,
            db_obj=self.item_data,
            obj_in=ItemUpdate(title=self.title, priority=self.priority),
        )
        self.db_session.refresh(self.obj)
        log.info("AFTER")
        log.info(self.obj.title)
        log.info(self.item_data.title)
        log.info(self.obj.priority)

    def response(self):
        return JSONResponse({"text": "Edited fine."})
