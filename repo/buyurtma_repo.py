from config.sqlite_config import session
from model.buyurtma import Buyurtma


class BuyurtmaRepo:
    def add(self, b ):
        session.add(b)
        session.commit()
        return True

    def getAll(self):
        return session.query(Buyurtma).all()

    def getById(self,id):
        return session.query(Buyurtma).filter(Buyurtma.id==id).first()

    def update(self, b):
        m = session.getById(b.id)
        m.xona = b.xona
        m.yaratilganVaqt = b.yaratilganVaqt
        m.mijoz = b.mijoz
        m.sana = b.sana
        m.smena = b.smena
        m.status = b.status
        m.boshlanishVaqti = b.boshlanishVaqti
        m.tugashVaqti = b.tugashVaqti
        m.izoh = b.izoh
        return True

    def delete(self, b):
        m = self.getById(b.id)
        session.delete(m)
        session.commit()
        return True