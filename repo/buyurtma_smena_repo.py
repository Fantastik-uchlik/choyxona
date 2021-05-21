from config.sqlite_config import session
from model.buyurtma_smena import BuyurtmaSmena


class BuyurtmaSmenaRepo:

    def add(self,bs):
        session.add(bs)
        session.commit()
        return True

    def getAll(self):
        return session.query(BuyurtmaSmena).all()

    def getById(self,id):
        return session.query(BuyurtmaSmena).filter(BuyurtmaSmena.id==id).first()

    def update(self,bs):
        b = session.getById(bs.id)
        b.nom = bs.nom
        b.boshVaqt = bs.boshVaqt
        b.tugashVaqt = bs.tugashVaqt
        b.izoh = bs.izoh
        session.commit()
        return True

    def delete(self, bs):
        b = self.getById(bs.id)
        session.delete(b)
        session.commit()
        return True
    