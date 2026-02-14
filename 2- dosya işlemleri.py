import json
with open("data.json","r",encoding="utf-8") as file:
    data=json.load(file)

with open("data.json","w",encoding="utf-8") as file:
    kitapAdi=input("kitap adınızı giriniz: ")
    yazar=input("yazar adını gir: ")
    fiyat=int(input("fiyatı gir"))
    yayın_tarihi=input("yayın tarihinizi giriniz")
    yayıncı=input("yayıncınızı giriniz")
    kategori=input("kategorii gir")
    müsaitlik=bool(input("müsaitlik durumunu giriniz "))
    data.append(
        {
            "kitap_adi":kitapAdi,
            "yazar":yazar,
            "fiyat":fiyat,
            "yayın_tarihi":yayın_tarihi,
            "yayıncı":yayıncı,
            "kategori":kategori,
            "müsaitlik":müsaitlik,
        }
    )

    json.dump(data,file,indent=4,ensure_ascii=False)