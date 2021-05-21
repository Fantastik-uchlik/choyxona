from sqlalchemy.exc import SQLAlchemyError

from repo.buyurtma_smena_repo import BuyurtmaSmenaRepo


class BuyurtmaSmenaService:
    bSmenaRepo = BuyurtmaSmenaRepo()

    def add(self,bs):
        try:
            return self.bSmenaRepo.add(bs)
        except SQLAlchemyError as e:
            print("Buyurtma smena qo'chib bo'lmadi!!!")
            print(e)
            return False


    def update(self, bs):
        try:
            return self.bSmenaRepo.update(bs)
        except SQLAlchemyError as e:
            print("Buyurtma smenani o'zgartirib bo'lmadi!!!")
            print(e)
            return  False

    def getAll(self):
        return self.bSmenaRepo.getAll()

    def delete(self,bs):
        try:
            return self.bSmenaRepo.delete(bs)
        except SQLAlchemyError as e:
            print("Buyurtma smenani o'chirib bo'lmadi!!!")
            print(e)
            return False
