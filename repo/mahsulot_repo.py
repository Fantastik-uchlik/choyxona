from config.sqlite_config import session
from model.mashsulot import Mahsulot


class MahsulotRepo:
    def add(self,mr):
        session.add(mr)
        session.commit()
        return True

    def getAll(self):
        return session.query(Mahsulot).all()

    def getById(self, id):
        return session.query(Mahsulot).filter(Mahsulot.id==id).first()

    def update(self,mr):
        m = self.getById(mr.id)
        m.nom = mr.nom
        m.narx = mr.narx
        m.tur = mr.tur
        m.ulchovi = mr.ulchovi
        m.izoh = mr.izoh
        m.show = mr.show

    def delete(self, mr):
        m = self.getById(mr.id)
        session.delete(m)
        session.commit()
        return True