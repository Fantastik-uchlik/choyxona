from sqlalchemy.exc import SQLAlchemyError

from repo.status_repo import StatusRepo


class StatusService:
    sr = StatusRepo()

    def add(self,s):
        try:
            return self.sr.add(s)
        except SQLAlchemyError as e:
            print("Statusni qo'shib bo'lmadi!!!")
            print(e)
            return False

    def update(self, s):
        try:
            return self.sr.update(s)
        except SQLAlchemyError as e:
            print("Status serviceni o'zgartirib bo'lmadi!!!")
            print(e)
            return False

    def getAll(self):
        return self.sr.getAll()

    def delete(self,s):
        try:
            return self.sr.delete(s)
        except SQLAlchemyError as e:
            print("Statusni o'chirib bo'madi!!!")
            print(e)
            return False
