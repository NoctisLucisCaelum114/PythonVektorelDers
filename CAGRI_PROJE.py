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
    print("║  3-Çizimler             ║")
    print("║  4-Resimler             ║")
    print("║  5-Anime önerileri      ║")
    print("║    Seçiminiz nedir?     ║")
    print("╚═════════════════════════╝")

    secim = input("Seçiminiz: ")

    if secim == "1":
        Konsolprojem.Konsol.hmmenu()
        anamenu()
    elif secim == "2":
       oyunlar.oyun.oyunmenu()
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin")
    if secim == "5":
        animeönerileri.Animeönerileri.animemenu()
    # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚
    # 188 ╝
    
anamenu()
    ##hesapmakinesi ()
    #print("╔"+"="*20+"╗"