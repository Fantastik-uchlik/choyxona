from config.sqlite_config import session
from model.buyurtma_mijoz import BuyurtmaMijoz


class BuyurtmaMijozRepo:
    def add(self,bm):
        session.add(bm)
        session.commit()
        return True

    def getAll(self):
        return session.query(BuyurtmaMijoz).all()

    def getById(self,id):
        return session.query(BuyurtmaMijoz).filter(BuyurtmaMijoz.id==id).first()

    def update(self, bm):
        b = session.getById(bm.id)
        b.ism = bm.ism
        b.familiya = bm.familiya
        b.telRaqam = bm.telRaqam
        b.izoh = bm.izoh
        session.commit()
        return True

    def delete(self, bm):
        b = self.getById(bm.id)
        session.delete(b)
        session.commit()
        return True
