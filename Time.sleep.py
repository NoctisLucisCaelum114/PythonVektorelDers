import time
import datetime
import os
print("Bu birinci mesajdır.")
time.sleep(2)  # Programı 2 saniye duraklatır
print("Bu ikinci mesajdır, 2 saniye sonra ekrana yazdırıldı.")
while True:


    simdi = datetime.datetime.now()
    print(simdi.strftime("%H:%M:%S"))
    time.sleep(3)

