from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    priority = Column(Integer, index=True)
    user_id = Column(String(50), index=True)
    user_name = Column(String)
