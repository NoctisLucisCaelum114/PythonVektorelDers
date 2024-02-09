import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="Deneme",


)

mycursor = mydb.cursor()
arnn = input("Aradığınız isim?")
sql = "SELECT * FROM ogrenciler WHERE adSoyad