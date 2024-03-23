def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Sıfıra bölme hatası!"
    else:
        return x / y

print("Toplama için 1'i, Çıkarma için 2'yi, Çarpma için 3'ü, Bölme için 4'ü tuşlayın")
secim = input("İşlem seçiniz (1/2/3/4): ")

if secim in ('1', '2', '3', '4'):
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    if secim == '1':
        print("Sonuç:", toplama(sayi1, sayi2))
    elif secim == '2':
        print("Sonuç:", cikarma(sayi1, sayi2))
    elif secim == '3':
        print("Sonuç:", carpma(sayi1, sayi2))
    elif secim == '4':
        print("Sonuç:", bolme(sayi1, sayi2))
else:
    print("Geçersiz giriş")