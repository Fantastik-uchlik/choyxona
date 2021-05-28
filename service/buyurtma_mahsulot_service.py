from sqlalchemy.exc import SQLAlchemyError

from repo.buyurtma_mahsulot_repo import BuyurtmaMahsulotRepo


class BuyurtmaMahsulotService:
    bmr = BuyurtmaMahsulotRepo()

    def add(self, bm):
        try:
            return self.bmr.add(bm)
        except SQLAlchemyError as e:
            print("Buyurtma mahsulotni qo'shib bo'lmadi!!!")
            print(e)
            return False

    def update(self, bm):
        try:
            return self.bmr.update(bm)
        except SQLAlchemyError as e:
            print("Buyurtma mahsulotni o'zgrtirib bo'lmadi!!!")
            print(e)
            return False

    def getAll(self):
        return self.bmr.getAll()

    def delete(self, bm):
        try:
            return self.bmr.delete(bm)
        except SQLAlchemyError as e:
            print("Buyurtma mahsulotni o'chirib bo'lmadi!!!")
            print(e)
            return False