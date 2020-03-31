from starlette.responses import JSONResponse

WRONG_COMMAND = "Ouch! That command does not exist."
WRONG_DIRECTION = "Available directions are 'up' and 'down'."
WRONG_PRIORITY = "Item with given number doesn't exist."


class InternalException(Exception):
    msg = "Error"

    def get_message(self):
        return JSONResponse({"text": self.msg})


class WrongCommandException(InternalException):
    msg = WRONG_COMMAND


class WrongDirectionException(InternalException):
    msg = WRONG_DIRECTION


class WrongPriorityException(InternalException):
    msg = WRONG_PRIORITY
