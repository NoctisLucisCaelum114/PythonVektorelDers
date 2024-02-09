 #veritabanı sistemine bağlanma
import mysql.connector
try:
    xxx = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password="1234")
    print("Bağlandı")
    print(xxx)

    secilenvt = xxx.cursor() # verritabanı seçim işlemi USE .....
    secilenvt.execute("SHOW DATABASE") #veritabanında SQL komutu
    print ("\nVeritabanları:")
    for x in secilenvt: print(x)
except mysql.connector.Error as xx:
    print("hata oluştu")
    print(f"hata kodu:\n{xx}")