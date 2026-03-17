from sqlalchemy import Column, Integer, String
from backend.database import Base

class UserData(Base):
    __tablename__ = "user_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)