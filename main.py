from abc import ABC, abstractmethod

class Kaynak(ABC):
    """Tüm kaynakların ortak özelliklerini barındıran soyut sınıf"""

    def __init__(self, baslik, kayitNo):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @baslik.setter
    def baslik(self, value):
        self._baslik = value

    @property
    def kayitNo(self):
        return self._kayitNo

    @kayitNo.setter
    def kayitNo(self, value):
        self._kayitNo = value


class Kitap(Kaynak):
    """Kaynak soyut sınıfından türetilen Kitap sınıfı"""

    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @yazar.setter
    def yazar(self, value):
        self._yazar = value

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    @sayfa_sayisi.setter
    def sayfa_sayisi(self, value):
        self._sayfa_sayisi = value

    # Bonus: __str__ metodu ile düzgün çıktı alma
    def __str__(self):
        return f"Kitap No: {self.kayitNo} | Başlık: {self.baslik} | Yazar: {self.yazar} | Sayfa: {self.sayfa_sayisi}"


class Dergi(Kaynak):
    """Kaynak soyut sınıfından türetilen Dergi sınıfı"""

    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)
        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @yayin_donemi.setter
    def yayin_donemi(self, value):
        self._yayin_donemi = value

    @property
    def sayi_no(self):
        return self._sayi_no

    @sayi_no.setter
    def sayi_no(self, value):
        self._sayi_no = value

    # Bonus: __str__ metodu ile düzgün çıktı alma
    def __str__(self):
        return f"Dergi No: {self.kayitNo} | Başlık: {self.baslik} | Dönem: {self.yayin_donemi} | Sayı No: {self.sayi_no}"


# ----------------------------
# CRUD İşlemleri

class Islem(ABC):
    """CRUD işlemlerini zorunlu kılan soyut sınıf"""

    @abstractmethod
    def ekle(self):
        pass

    @abstractmethod
    def sil(self):
        pass

    @abstractmethod
    def guncelle(self):
        pass

    @abstractmethod
    def listele(self):
        pass


class KitapIslem(Islem):
    """Kitaplar için CRUD operasyonları"""

    kitaplar_listesi = []
    kitap_sayisi = 0

    def ekle(self):
        print("\n--- Kitap Ekle ---")
        kayitNo = input("Kitabın kayıt numarasını girin: ")

        # Bonus: Kayıt numarası tekrar kontrolü
        for k in self.kitaplar_listesi:
            if k.kayitNo == kayitNo:
                print("Hata: Bu kayıt numarası zaten mevcut!")
                return

        baslik = input("Kitabın başlığını girin: ")
        yazar = input("Kitabın yazarını girin: ")

        # Sayfa sayısı hata kontrolü
        while True:
            try:
                sayfa_sayisi = int(input("Kitabın sayfa sayısını girin: "))
                break
            except ValueError:
                print("Geçersiz giriş! Sayfa sayısı sadece sayılardan oluşmalıdır. Lütfen tekrar deneyin.")

        yeni_kitap = Kitap(baslik, kayitNo, yazar, sayfa_sayisi)
        self.kitaplar_listesi.append(yeni_kitap)
        KitapIslem.kitap_sayisi += 1
        print("Kitap başarıyla eklendi.")
        print(f"Toplam Kitap Sayısı: {KitapIslem.kitap_sayisi}")

    def sil(self):
        print("\n--- Kitap Sil ---")
        kayitNo = input("Silinecek kitabın kayıt numarasını girin: ")
        for k in self.kitaplar_listesi:
            if k.kayitNo == kayitNo:
                self.kitaplar_listesi.remove(k)
                KitapIslem.kitap_sayisi -= 1
                print("Kitap başarıyla silindi.")
                return
        print("Kayıt bulunamadı.")

    def guncelle(self):
        print("\n--- Kitap Güncelle ---")
        kayitNo = input("Güncellenecek kitabın kayıt numarasını girin: ")
        for k in self.kitaplar_listesi:
            if k.kayitNo == kayitNo:
                k.baslik = input(f"Yeni Başlık ({k.baslik}): ") or k.baslik
                k.yazar = input(f"Yeni Yazar ({k.yazar}): ") or k.yazar

                while True:
                    yeni_sayfa = input(f"Yeni Sayfa Sayısı ({k.sayfa_sayisi}): ")
                    if not yeni_sayfa:
                        break
                    try:
                        k.sayfa_sayisi = int(yeni_sayfa)
                        break
                    except ValueError:
                        print("Geçersiz giriş! Lütfen sadece sayı girin.")

                print("Kitap başarıyla güncellendi.")
                return
        print("Kayıt bulunamadı.")

    def listele(self):
        print("\n--- Kitapları Listele ---")
        if not self.kitaplar_listesi:
            print("Kayıt bulunamadı.")
            return
        for k in self.kitaplar_listesi:
            print(k)


class DergiIslem(Islem):
    """Dergiler için CRUD operasyonları"""

    dergiler_listesi = []
    dergi_sayisi = 0

    def ekle(self):
        print("\n--- Dergi Ekle ---")
        kayitNo = input("Derginin kayıt numarasını girin: ")

        # Bonus: Kayıt numarası tekrar kontrolü
        for d in self.dergiler_listesi:
            if d.kayitNo == kayitNo:
                print("HATA: Bu kayıt numarası zaten mevcut!")
                return

        baslik = input("Derginin başlığını girin: ")
        yayin_donemi = input("Derginin yayın dönemini girin (Aylık/Haftalık): ")

        # Dergi sayı numarası hata kontrolü
        while True:
            try:
                sayi_no = int(input("Derginin sayı numarasını girin: "))
                break
            except ValueError:
                print("Geçersiz giriş! Sayı no sadece sayılardan oluşmalıdır. Lütfen tekrar deneyin.")

        yeni_dergi = Dergi(baslik, kayitNo, yayin_donemi, sayi_no)
        self.dergiler_listesi.append(yeni_dergi)
        DergiIslem.dergi_sayisi += 1
        print("Dergi başarıyla eklendi.")
        print(f"Toplam Dergi Sayısı: {DergiIslem.dergi_sayisi}")

    def sil(self):
        print("\n--- Dergi Sil ---")
        kayitNo = input("Silinecek derginin kayıt numarasını girin: ")
        for d in self.dergiler_listesi:
            if d.kayitNo == kayitNo:
                self.dergiler_listesi.remove(d)
                DergiIslem.dergi_sayisi -= 1
                print("Dergi başarıyla silindi.")
                return
        print("Kayıt bulunamadı.")

    def guncelle(self):
        print("\n--- Dergi Güncelle ---")
        kayitNo = input("Güncellenecek derginin kayıt numarasını girin: ")
        for d in self.dergiler_listesi:
            if d.kayitNo == kayitNo:
                d.baslik = input(f"Yeni Başlık ({d.baslik}): ") or d.baslik
                d.yayin_donemi = input(f"Yeni Dönem ({d.yayin_donemi}): ") or d.yayin_donemi

                while True:
                    yeni_sayi = input(f"Yeni Sayı No ({d.sayi_no}): ")
                    if not yeni_sayi:
                        break
                    try:
                        d.sayi_no = int(yeni_sayi)
                        break
                    except ValueError:
                        print("Geçersiz giriş! Lütfen sadece sayı girin.")

                print("Dergi başarıyla güncellendi.")
                return
        print("Kayıt bulunamadı.")

    def listele(self):
        print("\n--- Dergileri Listele ---")
        if not self.dergiler_listesi:
            print("Kayıt bulunamadı.")
            return
        for d in self.dergiler_listesi:
            print(d)

# ----------------------------
# Menü ve Ana Döngü

class Menu:
    """Kullanıcı arayüzünü yöneten sınıf"""

    def __init__(self):
        self.kitap_kontrolor = KitapIslem()
        self.dergi_kontrolor = DergiIslem()

    def goster(self):
        print("\n" + "* " * 15)
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Güncelle")
        print("4. Kitapları Listele")
        print("5. Dergi Ekle")
        print("6. Dergi Sil")
        print("7. Dergi Güncelle")
        print("8. Dergileri Listele")
        print("9. Çıkış")
        print("* " * 15)

    def calistir(self):
        while True:
            self.goster()
            secim = input("Yapmak istediğiniz işlemi seçin (1-9): ")

            if secim == "1":
                self.kitap_kontrolor.ekle()
            elif secim == "2":
                self.kitap_kontrolor.sil()
            elif secim == "3":
                self.kitap_kontrolor.guncelle()
            elif secim == "4":
                self.kitap_kontrolor.listele()
            elif secim == "5":
                self.dergi_kontrolor.ekle()
            elif secim == "6":
                self.dergi_kontrolor.sil()
            elif secim == "7":
                self.dergi_kontrolor.guncelle()
            elif secim == "8":
                self.dergi_kontrolor.listele()
            elif secim == "9":
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz seçim! Lütfen 1-9 arasında bir değer girin.")


# ----------------------------
# Programı başlat

if __name__ == "__main__":
    otomasyon = Menu()
    otomasyon.calistir()