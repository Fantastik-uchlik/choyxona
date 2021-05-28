from sqlalchemy import Column, Integer, Date, String

from model.base import Base


class BuyurtmaMahsulot(Base):
    __tablename__ = "buyurtma_mahsulot"
    id = Column(Integer, primary_key=True)
    buyurtma = Column(Integer, nullable=False)
    mahsulot = Column(Integer, nullable=False)
    miqdori = Column(Integer, nullable=False)
    puli = Column(Integer, nullable=False)
    quyishVaqti = Column(Date, nullable=False)
    status = Column(Integer, nullable=False)
    izoh = Column(String, nullable=False)
