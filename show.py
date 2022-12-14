from connection import *
from product import *


class Przegladanie:
    def __init__(self):
        self.lista = []

        self.loadFromDB()
        self.strona = 1
        self.rozmiarStrony = 5

    def loadFromDB(self):
        self.lista = []
        cursor = connection.cursor()
        cursor.execute("SELECT _id, nazwa, cena, ilosc, opis FROM Produkty")
        fetchedRows = cursor.fetchall()

        for row in fetchedRows:
            id = row[0]
            nazwa = row[1]
            cena = row[2]
            ilosc = row[3]
            try:
                opis = row[5]
            except:
                opis = ""
            self.lista.append(Produkt(id, nazwa, cena, ilosc, opis))

        for x in self.lista:
            x.wyswietl()

    def przegladanie(self, lista):
        strona = []
        for x in range((self.strona-1)*self.rozmiarStrony, self.strona*self.rozmiarStrony):
            try:
                strona.append(lista[x])
            except:
                pass
        return strona

    def wyswietl(self, nazwa):
        for produkt in self.lista:
            if produkt.name == nazwa:
                produkt.wyswietl()

    def wyszukaj(self, nazwa):
        self.strona = 1
        wyszukane = []
        for produkt in self.lista:
            if nazwa.lower() in produkt.name:
                wyszukane.append(produkt)
        return wyszukane


Produkty = Przegladanie()
