import json

def gorev():
    with open('Muhasebe.json', 'r', encoding='utf-8-sig') as dosya:
        veri = json.load(dosya)

    veri_listesi = veri  # JSON bir liste, doğrudan atayabiliriz

    grup_listesi = []
    hes_listesi = []

    # Her kayıt için grup ve hes değerlerini belirle
    for i in range(len(veri_listesi)):
        hes = veri_listesi[i]["heskod"]
        
        # Grup belirleme mantığı düzeltildi
        if '.' in hes:
            # Nokta varsa, noktadan önceki kısmı grup olarak al
            grup_deger = hes.split('.')[0]
        else:
            # Nokta yoksa, son rakamı çıkar (153 -> 15, 15 -> 1)
            if len(hes) > 1:
                grup_deger = hes[:-1]
            else:
                grup_deger = ""  # Tek haneli sayılar için grup yok

        grup_listesi.append(grup_deger)
        hes_listesi.append(hes)

        print(f"{hes} kodunun grubu: {grup_deger}")

    # Hesap grubu / hesap planı ayrımı
    # Bir hesap kodu başka hesapların grubu ise "hesap grubu"dur
    # Aksi halde "hesap planı"dır
    for hes in hes_listesi:
        # Bu hesap kodu, başka hesapların grubu mu kontrol et
        is_grup = False
        for other_hes in hes_listesi:
            if other_hes != hes:
                # other_hes'in grubu bu hes mi?
                if '.' in other_hes:
                    other_grup = other_hes.split('.')[0]
                else:
                    if len(other_hes) > 1:
                        other_grup = other_hes[:-1]
                    else:
                        other_grup = ""
                
                if other_grup == hes:
                    is_grup = True
                    break
        
        if is_grup:
            print(f"{hes} bir hesap grubudur.")
        else:
            print(f"{hes} bir hesap planıdır.")

gorev()