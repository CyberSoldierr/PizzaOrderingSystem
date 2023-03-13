import csv
import datetime


class Pizza:
    def __init__(self):
        self.description = "Bir pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        return 0


class Klasik(Pizza):
    def __init__(self):
        self.description = "Klasik pizza"

    def get_cost(self):
        return 20


class Margherita(Pizza):
    def __init__(self):
        self.description = "Margherita pizza"

    def get_cost(self):
        return 25


class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Türk pizzası"

    def get_cost(self):
        return 30


class SadePizza(Pizza):
    def __init__(self):
        self.description = "Sade pizza"

    def get_cost(self):
        return 15


class Musteri:
    def __init__(self, isim, adres):
        self.isim = isim
        self.adres = adres
        self.siparisler = []

    def siparis_ver(self, pizza):
        self.siparisler.append(pizza)

    def get_siparisler(self):
        return self.siparisler

    def get_toplam_maliyet(self):
        toplam_maliyet = 0
        for pizza in self.siparisler:
            toplam_maliyet += pizza.get_cost()
        return toplam_maliyet

    def get_adres(self):
        return self.adres

    def get_isim(self):
        return self.isim

    def __str__(self):
        return f"{self.isim}, {self.adres} adresine teslim edilecek, toplam maliyet: {self.get_toplam_maliyet()} TL"


musteri1 = Musteri("Ali", "İstanbul")
musteri1.siparis_ver(Klasik())
musteri1.siparis_ver(Margherita())
musteri1.siparis_ver(TurkPizza())

musteri2 = Musteri("Ayşe", "Ankara")
musteri2.siparis_ver(SadePizza())
musteri2.siparis_ver(Klasik())

siparisler = [musteri1, musteri2]

with open("siparisler.txt", "w", encoding="cp1254", newline="") as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(["İsim", "Adres", "Siparişler", "Toplam Maliyet"])
    for musteri in siparisler:
        writer.writerow([musteri.get_isim(), musteri.get_adres(), '\t'.join([p.get_description() for p in musteri.get_siparisler()]), musteri.get_toplam_maliyet()])
