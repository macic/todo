from app.schemas.slack import Command as CommandSchema
from app.handlers.add_item import AddItem
from app.handlers.edit_item import EditItem

class CommandHandler():
    mapping = {
        "add": AddItem,
        "create": AddItem,
        "edit": EditItem
    }

    def __init__(self, command: str) -> bool:
        actual_handler = self.mapping.get(command.lower())
        self._handler = actual_handler()
        if not self._handler:
            raise AttributeError

    def parse_text(self, rest: str):
        return self._handler.parse_text(rest)

    def handle(self, full_command: CommandSchema):
        return self._handler.handle(full_command)

    def response(self):
        return self._handler.response()