meyveler = ["elma","armut","kiraz"]
print(meyveler)

print(meyveler[1]) # 1indisi
print(meyveler[-1]) # tersten 1.indisi

print(len(meyveler))
print("----------------")
for a in range(len(meyveler)):
    # print(a)
    print(meyveler[a])
print("----------------")

for a in meyveler:
    print(a)

    meyveler.pop(0)     