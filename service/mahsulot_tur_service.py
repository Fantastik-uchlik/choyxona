from sqlalchemy.exc import SQLAlchemyError

from repo.mahsulot_tur_repo import MahsulotTurRepo


class MahsulotTurService:
    mtr = MahsulotTurRepo()

    def add(self,mt):
        try:
            return self.mtr.add(mt)
        except SQLAlchemyError as e:
            print("Mahsulot turini qo'chib bo'lmadi!!!")
            print(e)
            return False

    def update(self,mt):
        try:
            return self.mtr.update(mt)
        except SQLAlchemyError as e:
            print("Mahsulot turini o'zgartirib bo'lmadi!!!")
            print(e)
            return False

    def getAll(self):
        return self.mtr.getAll()

    def delete(self, mt):
        try:
            return self.mtr.delete(mt)
        except SQLAlchemyError as e:
            print("Mahsulot turini o'chirib bo'lmadi!!!")
            print(e)
            return False