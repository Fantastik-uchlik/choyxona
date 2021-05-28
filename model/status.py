from sqlalchemy import Column, Integer, String

from model.base import Base


class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    izoh = Column(String, nullable=False)
