from app.constants import WrongCommandException
from app.db.session import Session
from app.schemas.slack import Command as CommandSchema
from app.handlers.add_item import AddItem
from app.handlers.edit_item import EditItem
from app.handlers.move_item import MoveItem


class CommandHandler:
    mapping = {"add": AddItem, "create": AddItem, "edit": EditItem, "move": MoveItem}

    def __init__(self, command: str, db_session: Session) -> bool:
        actual_handler = self.mapping.get(command.lower())
        self._handler = actual_handler(db_session) if actual_handler else None
        if not self._handler:
            raise WrongCommandException

    def parse_text(self, text: str):
        return self._handler.parse_text(text)

    def handle(self, full_command: CommandSchema):
        return self._handler.handle(full_command)

    def response(self):
        return self._handler.response()
