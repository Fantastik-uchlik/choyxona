from model.mahsulot_ulchov import MahsulotUlchov
from service.mahsulot_ulchov_service import MahsulotUlchovService

mus = MahsulotUlchovService()

"""
    qo'shishni tekshirish
"""
mu = MahsulotUlchov(id = 9, nom = "dona", izoh = "bu bilan kilogramni o'lchaymiz")

if mus.delete(mu):
    print("qo'shildi!")
else:
    print("qo'shilmadi?!")

for m in mus.getAll():
    print(m.id, m.nom)