import json

class ErrorExceptions:
    message = ''
    
    def __init__(self, message):
        self.message = message
        return message