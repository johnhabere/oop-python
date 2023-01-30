
class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f"Status Code: {self.statusCode}! Message: {self.message}")
    
class NotFoundError(HttpException):
    statusCode = 404
    message = "Server Not Found"

class ServerError(HttpException):
    statusCode = 500
    message = "Server is down! We shall soon be vailable"
    
def raiseNotFoundError():
    raise NotFoundError()

raiseNotFoundError()