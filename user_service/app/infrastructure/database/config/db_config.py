"""
Database configurations
It would keep all database related settings, such as the database URL and other configuration parameters
"""

from sqlalchemy import create_engine


DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost/postgres"
engine = create_engine(DATABASE_URL)
