from starlette.responses import JSONResponse

from app.constants import WrongDirectionException, WrongPriorityException
from app.schemas.item import ItemUpdate
from app.schemas.slack import Command as CommandSchema
from app.handlers.base_handler import BaseHandler
from app.crud import item
from app.utils import split_by_first_space, log


class MoveItem(BaseHandler):
    direction_mapping = {"up": -1, "upper": -1, "high": -1, "higher": -1, "down": 1, "low": 1, "lower": 1}

    def parse_text(self, text: str):
        self.priority, self.direction = split_by_first_space(text)

    def handle(self, full_command: CommandSchema):
        priority_adjustment = self.direction_mapping.get(self.direction)
        if not priority_adjustment:
            raise WrongDirectionException
        self.item_data = item.get_by_priority_and_user_id(
            db_session=self.db_session, priority=self.priority, user_id=full_command.user_id
        )
        if not self.item_data:
            raise WrongPriorityException
        previous_priority = self.item_data.priority
        new_priority = self.item_data.priority + priority_adjustment
        # don't lower down the priority to 0
        if new_priority == 0:
            return
        max_priority = item.get_last_priority_by_user_id(db_session=self.db_session, user_id=full_command.user_id)
        # don't increase priority above available maximum
        if new_priority >= max_priority:
            return

        # find the other item we need to switch with
        other_item = item.get_by_priority_and_user_id(
            db_session=self.db_session, priority=new_priority, user_id=full_command.user_id
        )

        # TODO WTF DUDE
        from copy import deepcopy, copy

        copied_item = deepcopy(other_item)  # db_session PROBLEM!!
        # END OF WTF DUDE

        item.update_many(
            db_session=self.db_session,
            db_objs=[
                {self.item_data: ItemUpdate(priority=new_priority)},
                {copied_item: ItemUpdate(priority=previous_priority)},
            ],
        )
        # item.update(db_session=self.db_session, db_obj=self.item_data, obj_in=ItemUpdate(priority=new_priority))
        # item.update(db_session=self.db_session, db_obj=copied_item, obj_in=ItemUpdate(priority=previous_priority))

    def response(self):
        return JSONResponse({"text": "Moved fine."})
