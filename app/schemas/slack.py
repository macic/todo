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
    text: str

class BasicMessage(BaseModel):
    response_type: str = "in_channel"
    text: str