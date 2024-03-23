class Ilan ():
    IlanNo = 0
    IlanBaslik = ""
    IlanSahibi = ""
    def __init__(self, x, y, z):
        self.IlanNo = x
        self.IlanBaslik = y
        self.IlanSahibi = z
    def bilgi(self):
        print("No:", self.IlanNo, "Başlık:", self.IlanBaslik)

    def kaydet(self):
        d = open("deneme.txt","w")
        kb = f"{self.IlanNo} {self.IlanBaslik} {self.IlanSahibi}\n"

ilan1 = Ilan(n = 13246, b = "Metroyayakın ev", s = "Eren Korkmaz")

print(ilan1.bilgi())
print(ilan1.IlanNo)