from config.sqlite_config import session
from model.buyurtma_xona import BuyurtmaXona


class BuyurtmaXonaRepo:
    def add(self, bx):
        session.add(bx)
        session.commit()
        return True


    def getAll(self):
        return session.query(BuyurtmaXona).all()


    def getById(self,id):
        return session.query(BuyurtmaXona).filter(BuyurtmaXona.id ==id).first()


    def update(self, bx):
        b = self.getById(bx.id)
        b.nom = bx.nom
        b.narx = bx.narx
        b.izoh = bx.izoh
        session.commit()
        return True

    def delete(self, bx):
        b = self.getById(bx.id)
        session.delete(b)
        session.commit()
        return True