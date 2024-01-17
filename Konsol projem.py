import CAGRI_PROJE  # Import the module directly
import oyunlar.oyun
import animeönerileri.Animeönerileri

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
        CAGRI_PROJE.hmmenu()  # Call the function directly
    elif secim == "2":
        oyunlar.oyun.oyunmenu()
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin")
    if secim == "5":
        animeönerileri.Animeönerileri.animemenu()
# Call the function to start the menu
anamenu()
