import logging
import os


# formatter to handle newlines
class CustomFormatter(logging.Formatter):
    def format(self, record):
        message = super().format(record)
        return message.replace('\\n', '\n')
    
 
def terminal_half_width():
    terminal_width = tuple((os.get_terminal_size()))[0]
    return terminal_width//2