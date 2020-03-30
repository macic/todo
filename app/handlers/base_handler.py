from app.schemas.slack import Command as CommandSchema

class BaseHandler:
    def handle(self, rest: str, full_command: CommandSchema):
        raise NotImplementedError

    def response(self):
        raise NotImplementedError