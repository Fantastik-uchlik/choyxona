from sqlalchemy import Column, Integer, String

from model.base import Base


class Mahsulot(Base):
    __tablename__ = "mahsulot"
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    narxi = Column(Integer, nullable=False)
    tur = Column(Integer, nullable=False)
    ulchovi = Column(Integer, nullable=False)
    izoh = Column(String, nullable=False)
    show = Column(String, nullable=False)