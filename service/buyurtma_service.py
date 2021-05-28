from sqlalchemy.exc import SQLAlchemyError

from repo.buyurtma_repo import BuyurtmaRepo


class BuyurtmaService:
    br = BuyurtmaRepo()

    def add(self,b):
        try:
            return self.br.add(b)
        except SQLAlchemyError as e:
            print("Buurtma qo'shib bo'lmadi!!!")
            print(e)
            return False

    def update(self,b):
        try:
            return self.br.update(b)
        except SQLAlchemyError as e:
            print("Buyurtmani o'zgartirib bo'lmadi!!!")
            print(e)
            return False

    def getAll(self):
        return self.br.getAll()

    def delete(self, b):
        try:
            return self.br.delete(b)
        except SQLAlchemyError as e:
            print("Buyurtmani o'chirib bo'lmadi!!!")
            print(e)
            return False