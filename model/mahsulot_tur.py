from sqlalchemy import Column, Integer, String

from model.base import Base


class MahsulotTur(Base):
    __tablename__ = "mahsulot_tur"
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    izoh = Column(String, nullable=False)
    
