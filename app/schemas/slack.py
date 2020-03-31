from pydantic import BaseModel


class Command(BaseModel):
    token: str
    command: str
    response_url: str
    trigger_id: str
    user_id: str
    user_name: str
    team_id: str
    channel_id: str
    channel_name: str
    team_domain: str
    text: str


class AddCommand(Command):
    pass


class BasicMessage(BaseModel):
    response_type: str = "in_channel"
    text: str


class ErrorMessage(BasicMessage):
    response_type: str = "in_channel"
    text: str
