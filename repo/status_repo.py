from config.sqlite_config import session
from model.status import Status


class StatusRepo:

    def add(self,s):
        session.add(s)
        session.commit()
        return True

    def getAll(self):
        return session.query(Status).all()

    def update(self,s):
        m = self.getById(s.id)
        m.nom = s.nom
        m.izoh = s.izoh
        session.commit()
        return True

    def getById(self,id):
        return session.query(Status).filter(Status.id==id).first()

    def delete(self, s):
        m = self.getById(s.id)
        session.delete(m)
        session.commit()
        return True