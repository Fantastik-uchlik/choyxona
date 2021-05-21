from sqlalchemy import Column, Integer, String


from model.base import Base



class BuyurtmaXona(Base):
    __tablename__ = "buyurtma_xona"
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    narx = Column(Integer, nullable=False)
    izoh = Column(String, nullable=False)
