from config.sqlite_config import session
from model.mahsulot_tur import MahsulotTur


class MahsulotTurRepo:
    def add(self, mt):
        session.add(mt)
        session.commit()
        return True

    def getAll(self):
        return session.query(MahsulotTur).all()

    def getById(self, id):
        return session.query(MahsulotTur).filter(MahsulotTur.id==id).first()

    def update(self, mt):
        m = self.getById(mt.id)
        m.nom = mt.nom
        m.izoh = mt.izoh
        session.commit()
        return True

    def delete(self, mt):
        m = self.getById(mt.id)
        session.delete(m)
        session.commit()
        return True
    