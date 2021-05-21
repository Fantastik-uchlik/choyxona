from sqlalchemy.exc import SQLAlchemyError

from repo.buyurtma_mijoz_repo import BuyurtmaMijozRepo


class BuyurtmaMijozService:
    bmr = BuyurtmaMijozRepo()

    def add(self,bm):
        try:
            return self.bmr.add(bm)
        except SQLAlchemyError as e:
            print("Buyurtma mijozni qo'shib bo'lmadi!!!")
            print(e)
            return False

    def update(self, bm):
        try:
            return self.bmr.update(bm)
        except SQLAlchemyError as e:
            print("Buyurtma mijozni o'zgartirib bo'lmadi!!!")
            print(e)
            return False

    def getAll(self):
        return self.bmr.getAll()

    def delete(self, bm):
        try:
            return self.bmr.delete(bm)
        except SQLAlchemyError as e:
            print("Buyurtma mijozni o'chirib bo'lmadi!!!")
            print(e)
            return False

    