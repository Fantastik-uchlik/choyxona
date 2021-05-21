from sqlalchemy import Column, Integer, String, ForeignKey
from model.base import Base



class MahsulotUlchov(Base):
    __tablename__ ="mahsulot_ulchov"
    id = Column(Integer, primary_key = True)
    nom = Column(String, nullable=False)
    izoh = Column(String, nullable=True)

