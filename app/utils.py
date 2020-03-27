import logging
import sys
from app.constants import WRONG_COMMAND
from app.schemas.slack import Command
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.StreamHandler()
json_handler.setFormatter(formatter)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

log = logging.getLogger(__name__)
log.addHandler(json_handler)

AVAILABLE_COMMANDS = ['add', 'edit', 'done', 'finish', 'move', 'switch', 'show']

def parse_command(command: Command):
    parts = command.text.split(" ", 1)
    if len(parts)==2:
        actual_command = parts[0].lower()
        rest = parts[1]
        if actual_command in AVAILABLE_COMMANDS:
            return actual_command, rest
    return False, WRONG_COMMAND
