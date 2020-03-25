import os

DATABASE_URL = os.environ.get('DATABASE_URL') or \
               f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PW']}@{os.environ['DB_HOST']}:5432/{os.environ['DB_NAME']}"