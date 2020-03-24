import os

DATABASE_URL = os.environ.get('DATABASE_URL') or "postgresql://postgres:postgres@"+os.environ.get('DB_HOST')+":5432/postgres"