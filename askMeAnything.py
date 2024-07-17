import os
from app import create_app
import secrets # type: ignore

apikey = secrets.get('apikey')
os.environ["OPENAI_API_KEY"] = apikey

app = create_app()