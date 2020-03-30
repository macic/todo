from app.schemas.slack import Command as CommandSchema
from app.handlers.add_item import AddItemCommand

class CommandHandler():
    mapping = {
        "add": AddItemCommand
    }

    def __init__(self, command: str) -> bool:
        actual_handler = self.mapping.get(command.lower())
        self._handler = actual_handler()
        if not self._handler:
            raise AttributeError


    def handle(self, rest: str, full_command: CommandSchema):
        return self._handler.handle(rest, full_command)

    def response(self):
        return self._handler.response()