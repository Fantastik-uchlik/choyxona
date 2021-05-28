from config.sqlite_config import session
from model.buyurtma_mahsulot import BuyurtmaMahsulot


class BuyurtmaMahsulotRepo:
    def add(self, bm):
        session.add(bm)
        session.commit()
        return True

    def getAll(self):
        return session.query(BuyurtmaMahsulot).all()

    def getById(self, id):
        return session.query(BuyurtmaMahsulot).filter(BuyurtmaMahsulot.id==id).first()

    def update(self, bm):
        b = session.getById(bm.id)
        b.buyurtma = bm.buyurtma
        b.mahsulot = bm.mahsulot
        b.miqdori = bm.miqdori
        b.puli = bm.puli
        b.quyishVaqti = bm.quyishVaqti
        b.status = bm.status
        b.izoh = bm.izoh
        return  True

    def delete(self, bm):
        b = session.getById(bm.id)
        session.delete(b)
        session.commit()
        return True