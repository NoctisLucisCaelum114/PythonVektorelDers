import Tür1.Animeönerileritür1

def animemenu():
    print("\033[31m")
    print("╔═════════════════════════╗")
    print("║\033[31m                 ║")
    print("║                         ║")
    print("║  1-Doğaüstü güçler      ║")
    print("║  2-Aksiyon              ║")
    print("║  3-Dram                 ║")
    print("║  4-Mecha                ║")
    print("║  5-İsekai               ║")
    print("║    Seçiminiz nedir?     ║")
    print("╚═════════════════════════╝")

    secim = input("Seçiminiz: ")

    if secim == "5":
       Tür1.Animeönerileritür1.animeisekai() # beni duyuyor musun?
