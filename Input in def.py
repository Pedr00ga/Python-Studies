def medias():
    notaa = float(input("Digite a media de matematica: "))
    notab = float(input("Digite a media de portugues: "))
    notac = float(input("Digite a media de geografia: "))

    media = (notaa + notab + notac)
    return media / 3

print (medias())