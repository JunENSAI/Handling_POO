from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base


# 1. Connection String
SQLALCHEMY_DATABASE_URL = "sqlite:///./my_app.db"

# 2. The Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. The Session Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. The Base Class
Base = declarative_base()

"""
- Create a class User(Base).

- Add the configuration: __tablename__ = "users".

- Define the columns:

    id: Integer, primary key, index=True.

    email: String, unique, index=True.

    hashed_password: String.

    is_active: Boolean, default=True.
"""

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key =True, index = True)
    email = Column(String, unique=True, index = True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
