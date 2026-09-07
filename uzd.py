class Car:
    def __init__(self, marka, modelis, gads):
        self.marka = marka
        self.modelis = modelis
        self.gads = gads

    def car_age(self):
        return 2026 - self.gads

masina = Car("Audi", "skaists", 2015)
print(masina.car_age())
        
