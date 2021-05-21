from sqlalchemy.exc import SQLAlchemyError

from repo.buyurtma_xona_repo import BuyurtmaXonaRepo


class BuyurtmaXonaService:
    bxs = BuyurtmaXonaRepo()

    def add(self,bx):
        try:
            return self.bxs.add(bx)
        except SQLAlchemyError as e:
            print("Buyurtma xonasi qushilmadi!!!")
            print(e)
            return False


    def update(self,bx):
        try:
            return self.bxs.update(bx)
        except SQLAlchemyError as e:
            print("Buyurtma xonasi o'zgartirib bo'lmadi!!!")
            print(e)
            return False

    def getAll(self):
        return self.bxs.getAll()

    def delete(self,bx):
        try:
            return self.bxs.delete(bx)
        except SQLAlchemyError as e:
            print("Buyurtma xonasi o'chirib bo'lmadi!!!")
            print(e)
            return False