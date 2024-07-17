import sqlalchemy as sa
import sqlalchemy.orm as so
from app import create_app, session
from app.models import Question

app = create_app()


# @app.shell_context_processor
# def make_shell_context():
#     return {'sa': sa, 'so': so, 'session': session, 'Question': Question}
