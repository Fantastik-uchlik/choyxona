from sqlalchemy import Column, Integer, String, Date

from model.base import Base


class BuyurtmaSmena(Base):
    __tablename__ = "buyurtma_smena"
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    boshVaqt = Column(Date, nullable=False)
    tugashVaqt = Column(Date, nullable=False)
    