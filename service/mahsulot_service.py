from sqlalchemy.exc import SQLAlchemyError

from repo.mahsulot_repo import MahsulotRepo


class MahsulotService:
    ms = MahsulotRepo()

    def add(self, m):
        try:
            return self.ms.add(m)
        except SQLAlchemyError as e:
            print("Mahsulot qo'shilmadi!!!")
            print(e)
            return False

    def update(self, m):
        try:
            return self.ms.update(m)
        except SQLAlchemyError as e:
            print("Mahsulotni o'zgartirib bo'lmadi!!!")
            print(e)
            return False

    def getAll(self):
        return self.ms.getAll()

    def delete(self, m):
        try:
            return self.ms.delete(m)
        except SQLAlchemyError as e:
            print("Mahsulotni o'chirib bo'lmadi!!!")
            print(e)
            return False