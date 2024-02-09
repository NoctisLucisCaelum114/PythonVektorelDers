class Ilan ():
    IlanNo = 0
    IlanBaslik = ""
    IlanSahibi = ""
    def __init__(self, x, y, z):
        self.IlanNo = x
        self.IlanBaslik = y
        self.IlanSahibi = z

ilan1 = Ilan(n = 13246, b = "Metroyayakn ev", s = "Eren Korkmaz")

print(ilan1.bilgi())
print(ilan1.IlanNo)