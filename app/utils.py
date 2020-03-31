import logging
import sys
from typing import Optional, Tuple
from app.constants import WrongCommandException
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.StreamHandler()
json_handler.setFormatter(formatter)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

log = logging.getLogger(__name__)
log.addHandler(json_handler)


def split_by_first_space(text: str) -> Optional[Tuple[str, str]]:
    parts = text.split(" ", 1)
    if len(parts) == 2:
        first_part = parts[0].lower()
        rest = parts[1]
        return first_part, rest
    raise WrongCommandException
