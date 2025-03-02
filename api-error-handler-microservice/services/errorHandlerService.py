import datetime

class ErrorLog:
    """
    Represents an error log entry.
    """
    def __init__(self, service, message):
        self.service = service
        self.message = message
        self.timestamp = datetime.datetime.utcnow()

    def to_dict(self):
        """
        Converts error log object to a dictionary.
        """
        return {
            "service": self.service,
            "message": self.message,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
