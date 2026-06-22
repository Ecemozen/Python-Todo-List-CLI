# Görevlerin saklanacağı dosya
dosya_adi = "gorevler.txt"


#Görevleri dosyadan okur
def gorevleri_yukle():
    gorevler = []
    try:
        # Dosya okuma modunda açılır
        with open(dosya_adi, "r", encoding="utf-8") as f:
            for satir in f:
                # Satır "|" karakterine göre parçalanır
                parcalar = satir.strip().split("|")

                # Veri eksik değilse listeye eklenir
                if len(parcalar) == 4:
                    gorevler.append({
                        "metin": parcalar[0],  # Görev metni
                        "tamamlandi": parcalar[1] == "True",  # True/False dönüşümü
                        "oncelik": parcalar[2],  # Öncelik bilgisi
                        "tarih": parcalar[3]  # Son tarih
                    })

    # Dosya yoksa hata vermek yerine boş liste döner
    except FileNotFoundError:
        print("Dosya bulunamadı, yeni liste oluşturuluyor.")

    return gorevler


# Görevleri dosyaya kaydeder
def gorevleri_kaydet(gorevler):
    # Dosya yazma modunda açılır (eski veriler silinir)
    with open(dosya_adi, "w", encoding="utf-8") as f:
        for g in gorevler:
            # Her görev tek satır halinde kaydedilir
            satir = f"{g['metin']}|{g['tamamlandi']}|{g['oncelik']}|{g['tarih']}\n"
            f.write(satir)


# Görevleri listeler
def gorevleri_listele(gorevler):
    # Liste boşsa bilgi verilir
    if not gorevler:
        print("Liste boş.")
        return

    print("\n--- GÖREVLER ---")

    # enumerate ile numaralı liste oluşturulur
    for i, g in enumerate(gorevler, 1):
        # Tamamlanma durumuna göre işaret
        durum = "✔️" if g["tamamlandi"] else "✘"

        print(f"{i}. [{durum}] {g['metin']} | Öncelik: {g['oncelik']} | Tarih: {g['tarih']}")


# Yeni görev ekler
def gorev_ekle(gorevler):
    metin = input("Görev: ").strip()

    # Boş giriş kontrolü
    if metin == "":
        print("Boş görev eklenemez!")
        return

    # Ek bilgiler alınır
    oncelik = input("Öncelik (Yüksek/Orta/Düşük): ").strip()
    tarih = input("Son tarih: ").strip()

    # Görev listeye eklenir
    gorevler.append({
        "metin": metin,
        "tamamlandi": False,
        "oncelik": oncelik,
        "tarih": tarih
    })

    # Dosyaya kaydedilir
    gorevleri_kaydet(gorevler)
    print("Görev eklendi.")


# Görev siler
def gorev_sil(gorevler):
    gorevleri_listele(gorevler)

    try:
        # Kullanıcıdan sayı alınır
        secim = int(input("Silinecek görev numarası: "))

        # Geçerli aralık kontrolü
        if not (1 <= secim <= len(gorevler)):
            raise IndexError

        # Görev silinir
        gorevler.pop(secim - 1)
        gorevleri_kaydet(gorevler)
        print("Görev silindi.")

    # Sayı yerine başka giriş yapılırsa
    except ValueError:
        print("Lütfen sayı giriniz!")

    # Geçersiz indeks girilirse
    except IndexError:
        print("Geçersiz görev numarası!")


# Görev düzenler
def gorev_duzenle(gorevler):
    gorevleri_listele(gorevler)

    try:
        secim = int(input("Düzenlenecek görev numarası: "))

        # Aralık kontrolü
        if not (1 <= secim <= len(gorevler)):
            raise IndexError

        yeni = input("Yeni görev: ").strip()

        # Boş giriş kontrolü
        if yeni == "":
            raise ValueError

        # Güncelleme yapılır
        gorevler[secim - 1]["metin"] = yeni
        gorevleri_kaydet(gorevler)
        print("Görev güncellendi.")

    except ValueError:
        print("Geçersiz giriş! Boş veya hatalı değer girdiniz.")

    except IndexError:
        print("Geçersiz görev numarası!")


# Tamamlanma durumunu değiştirir
def tamamlandi_degistir(gorevler):
    gorevleri_listele(gorevler)

    try:
        secim = int(input("İşaretlenecek görev numarası: "))

        # Aralık kontrolü
        if not (1 <= secim <= len(gorevler)):
            raise IndexError

        # True ↔️ False değişimi
        gorevler[secim - 1]["tamamlandi"] = not gorevler[secim - 1]["tamamlandi"]
        gorevleri_kaydet(gorevler)
        print("Durum değiştirildi.")

    except ValueError:
        print("Lütfen sayı giriniz!")

    except IndexError:
        print("Geçersiz görev numarası!")


# Ana menü
def menu():
    # Program başında görevler yüklenir
    gorevler = gorevleri_yukle()

    while True:
        print("\n--- TO DO LIST ---")
        print("1. Listele")
        print("2. Ekle")
        print("3. Düzenle")
        print("4. Sil")
        print("5. Tamamlandı işaretle")
        print("6. Çıkış")

        secim = input("Seçiminiz: ")

        # Menü seçimleri
        if secim == "1":
            gorevleri_listele(gorevler)
        elif secim == "2":
            gorev_ekle(gorevler)
        elif secim == "3":
            gorev_duzenle(gorevler)
        elif secim == "4":
            gorev_sil(gorevler)
        elif secim == "5":
            tamamlandi_degistir(gorevler)
        elif secim == "6":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")


# Program başlatılır
menu()
