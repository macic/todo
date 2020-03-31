from app.schemas.slack import Command as CommandSchema


class BaseHandler:

    def parse_text(self, rest: str):
        return rest

    def handle(self, full_command: CommandSchema):
        raise NotImplementedError

    def response(self):
        raise NotImplementedError
