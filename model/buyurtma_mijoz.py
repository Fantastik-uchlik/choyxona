from sqlalchemy import Column, Integer, String

from model.base import Base


class BuyurtmaMijoz(Base):
    __tablename__ = "buyurtma_mijoz"
    id = Column(Integer, primary_key=True)
    ism = Column(String, nullable=False)
    familiya = Column(String, nullable=False)
    telRaqam = Column(Integer,nullable=False)
    izoh = Column(Integer, nullable=False)
    