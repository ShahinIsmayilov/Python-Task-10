xallar = [1, 7, 3, 4, 8, 7, 9,]
def sirala():
    yer = 1
    for i in xallar:
        for j in range(len(xallar)):
            if i < xallar[j]:
                yer += 1
        print(f"{yer} yer")
        yer = 1
sirala()
