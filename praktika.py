
class City:
    def __init__(self,name: str, region: str, country: str, citizen: int, index: int, phone_code: str ):
        self.name = name
        self.region = region
        self.country = country
        self.citizen = citizen
        self.index = index
        self.phone_code = phone_code
        print("Конструктор создал объект.")

    def setname(self, pname: str):
        self.name = pname

    def setregion(self, pregion: str):
        self.region = pregion

    def setcountry(self, pcountry: str):
        self.country = pcountry

    def setcitizen(self)->int:
        self.citizen = int(input("Введите количество жителей:"))

    def setindex(self)->int:
        self.index = int(input("Введите индекс:"))

    def setphone_code(self)->str:
        self.phone_code = input("Введите код города:")

    def getcitizen(self)->int:
        return self.citizen

    def getindex(self)->int:
        return self.index

    def getphone_code(self)->str:
        return self.phone_code

    def display(self):
        print(f" Название города: {self.name} Регион: {self.region} Страна: {self.country} Количество жителей: {self.citizen} Индекс: {self.index} Код города: {self.phone_code}")

objCity1 = City("Калининград", "Северо-западный", "Россия", 580000, 236000, "+7")
objCity1.display()
objCity1.setname("Калининград")
objCity1.setregion("Северо-западный")
objCity1.setcountry("Россия")
objCity1.setcitizen()
objCity1.setindex()
objCity1.setphone_code()
objCity1.display()
print(objCity1.getcitizen())
print(objCity1.getindex())
print(objCity1.getphone_code())


