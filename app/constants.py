from starlette.responses import JSONResponse

WRONG_COMMAND = "Ouch! That command does not exist."


class InternalException(Exception):
    msg = "Error"

    def get_message(self):
        return JSONResponse({"text": self.msg})


class WrongCommandException(InternalException):
    msg = WRONG_COMMAND
