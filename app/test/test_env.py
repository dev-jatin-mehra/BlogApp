import os
from dotenv import load_dotenv,dotenv_values
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
# email = os.getenv('EMAIL')
print(os.getenv('SECRET_KEY'))