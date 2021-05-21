from config.sqlite_config import session
from model.mahsulot_ulchov import MahsulotUlchov



class MahsulotUlchovRepo:

    def add(self,mu):
        session.add(mu)
        session.commit()
        return True
    def getAll(self):
        return session.query(MahsulotUlchov).all()

    def getByID(self, id):
        return session.query(MahsulotUlchov).filter(MahsulotUlchov.id == id).first()
    def update(self, mu):
        m = self.getByID(mu.id)
        m.nom = mu.nom
        m.izoh = mu.izoh
        session.commit()

        return True
    def delete(self, mu):
        m = self.getByID(mu.id)
        session.delete(m)
        session.commit()
        return True