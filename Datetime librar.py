import datetime
print("Bugün:",datetime.date.today())
print("Şimdi:",datetime.datetime.now())
Tarih = datetime.date.today()
print("Tarih:", Tarih)
simdi = datetime.datetime.now()
print(simdi.strftime("%m %M/%d, %D/%y%H:%M:%S"))
