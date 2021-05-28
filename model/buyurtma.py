from sqlalchemy import Column, Integer, Date, String

from model.base import Base


class Buyurtma(Base):
    __tablename__ = "buyurtma"
    id = Column(Integer, primary_key=True)
    xona = Column(Integer, nullable=False)
    yaratilganVaqt = Column(Date, nullable=False)
    mijoz = Column(Integer, nullable=False)
    sana = Column(Date, nullable=False)
    smena = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    boshlanishVaqti = Column(Date, nullable=False)
    tugashVaqti = Column(Date, nullable=False)
    izoh = Column(String, nullable=False)
