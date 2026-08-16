from database import (veritabani_olustur, ornek_filmler_ekle,
                      filmleri_listele, ture_gore_filtrele, film_puanla)
from ai_engine import film_oner, istatistikler

#ANA PROGRAM

def menu():
    print("\n" + "="*50)
    print("  🎬  FİLMBOT - Akıllı Film Öneri Sistemi")
    print("="*50)
    print("1. Tüm Filmleri Listele")
    print("2. Türe Göre Filtrele")
    print("3. Film Puanla")
    print("4. Çıkış")
    print("5. 🤖 Film Öner (Yapay Zeka)")
    print("6. 📊 İstatistikler")

    print("-"*50)
    return input("Seçiminiz (1-6): ")


def filmleri_goster():
    filmler = filmleri_listele()
    print(f"\n📋 Toplam {len(filmler)} film bulundu:\n")
    for f in filmler:
        print(f'  {f[0]:>2}. {f[1]:<30} | {f[2]:<15} | {f[3]} | ★ {f[4]}')


def ture_gore_goster():
    tur = input("Tür girin (Dram/Aksiyon/Bilim Kurgu/Fantastik/Gerilim/Gizem): ")
    filmler = ture_gore_filtrele(tur)
    if filmler:
        print(f"\n🎭 {tur} türündeki filmler:")
        for f in filmler:
            print(f'  • {f[0]} ({f[1]}) - ★ {f[2]}')
    else:
        print("Bu türde film bulunamadı.")


def puanla():
    film_id = int(input("Film ID: "))
    puan = int(input("Puanınız (1-5): "))
    yorum = input("Yorumunuz (opsiyonel): ")
    film_puanla(1, film_id, puan, yorum)


def main():
    veritabani_olustur()
    ornek_filmler_ekle()

    while True:
        secim = menu()
        if secim == "1":
            filmleri_goster()
        elif secim == "2":
            ture_gore_goster()
        elif secim == "3":
            puanla()
        elif secim == "4":
            print("Görüşmek üzere! 🎬")
            break
        elif secim == "5":
            oneriler = film_oner(1)
            print("\n🤖 Size önerilen filmler:")
            for film, skor in oneriler:
                print(f'  ★ {film[1]} ({film[3]}) - {film[2]} - Skor: {skor}')
        elif secim == "6":
        for stat in istatistikler():
            print(f'  {stat[0]:<15} | {stat[1]} film | ★ {stat[2]}')

        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()
