import Konsolprojem.Konsol
import oyunlar.oyun
import animeönerileri.Animeönerileri
import CAGRI_PROJE

def anamenu():
    print("\033[31m")
    print("╔═════════════════════════╗")
    print("║\033[31m                 ║")
    print("║                         ║")
    print("║  1-Hesap makinesi       ║")
    print("║  2-Oyunlar              ║")
    print("║  3-Çizimler,Resimler    ║")
    print("║  4-Anime nedir          ║")
    print("║  5-Anime önerileri      ║")
    print("║    Seçiminiz nedir?     ║")
    print("╚═════════════════════════╝")

    secim = input("Seçiminiz: ")

    if secim == "1":
        Konsolprojem.Konsol.hmmenu()
        anamenu()
    elif secim == "2":
       oyunlar.oyun.oyunmenu()
    if secim == "5":
        animeönerileri.Animeönerileri.animemenu()
    if secim == "4":
        print("Anime, Japonya kökenli bir animasyon türüdür. Anime terimi, İngilizce konuşulan ülkelerde genellikle Japon çizgi filmlerini ve animasyonlarını ifade etmek için kullanılır. Anime, geniş bir tür yelpazesine sahiptir ve farklı yaş gruplarına hitap edebilecek birçok farklı tarza sahiptir.")
    # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚
    # 188 ╝
    
anamenu()
    ##hesapmakinesi ()
    #print"╔"+"="*20+"╗"