from sqlalchemy.exc import SQLAlchemyError

from repo.mahsulot_ulchov_repo import MahsulotUlchov, MahsulotUlchovRepo


class MahsulotUlchovService:
    mur=MahsulotUlchovRepo()
    def add(self, mu):
        try:

            return self.mur.add(mu)
        except SQLAlchemyError as e:
            print("Mahsulot o'lchovi qo'shib bo'lmadi!!!")
            print(e)
            return  False
    def update(self, mu):
        try:

            return self.mur.update(mu)
        except SQLAlchemyError as e:
            print("Mahsulot o'lchovi o'zgartirib bo'lmadi!!!")
            print(e)
            return  False

    def getAll(self):
        return self.mur.getAll()
    def delete(self, mu):
        try:

            return self.mur.delete(mu)

        except SQLAlchemyError as e:
            print("Mahsulot o'lchovi o'chirib bo'lmadi!!!")
            print(e)
            return  False