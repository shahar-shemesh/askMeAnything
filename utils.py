import logging
import os


# formatter to handle newlines
class CustomFormatter(logging.Formatter):
    def format(self, record):
        message = super().format(record)
        return message.replace('\\n', '\n')
