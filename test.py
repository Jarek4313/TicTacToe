listA = []


listA.append("JAREK")
listA.append("Dziura")

listA[0] += "*****"
listA[1] += "*****"
#listA[2] += "*****"

for i in range(7):
    print(i)



class Gracz:
    def __init__(self, imie, punkty):
        self.imie = imie   
        self.punkty = punkty

gracz_00 = Gracz("Antonina", 99)
gracz_01 = Gracz("Jarek", 55)
gracz_02 = Gracz("Jan", 150)
gracz_03 = Gracz("Marek", 33)
gracz_04 = Gracz("Sławek", 142)

lista_graczy = [gracz_00, gracz_01, gracz_02, gracz_03, gracz_04]


