from app.schemas.slack import Command as CommandSchema


class BaseHandler:
    def __init__(self, db_session):
        self.db_session = db_session

    def parse_text(self, rest: str):
        return rest

    def handle(self, full_command: CommandSchema):
        raise NotImplementedError

    def response(self):
        raise NotImplementedError
