from Kontener import Kontener
from Zamowienie import Zamowienie

class Firm:

    def __init__(self):
        self.kontenerlist = [Kontener() for i in range(5)]
        self.zamowienia = [Zamowienie() for i in range(0)]
        self.set_startup_kontener_values()

    def set_startup_kontener_values(self):
        tmp_price = 50
        tmp_size = 200

        for x in range(5):
            self.kontenerlist[x].size = tmp_size
            self.kontenerlist[x].price = tmp_price
            tmp_price *= 2
            tmp_size += 100

        self.zamowienia.append(Zamowienie())
        self.zamowienia[0].set_zamowienie(10,self.kontenerlist[0],True)

    def main_loop(self):
        print("Hello in Firm App")

        select_char = "s"
        while select_char != "q":
            select_char = input("Select action:\n"
                               "1.Pokaz kontenery\n"
                               "2.Edytuj kontenery\n"
                               "3.Dodaj kontenery\n"
                               "4.Zobacz zamówienia\n"
                               "q/Q - Exit\n").upper()
            if select_char not in "1234qQ" or len(select_char) != 1:
                print("No such action")
                continue
            if select_char == '1':
                for i in range(len(self.kontenerlist)):
                    self.kontenerlist[i].print_info(i)
            elif select_char == '2':
                for i in range(len(self.kontenerlist)):
                    self.kontenerlist[i].print_info(i)
                kontener_id = int(input("Podaj id kontenera: "))
                self.kontenerlist[kontener_id].edit_kontener()
            elif select_char == '3':
                tmpKontener = Kontener()
                tmpKontener.price = int(input("Podaj cenę kontenera: "))
                tmpKontener.size = int(input("Podaj rozmiar kontenera: "))
                self.kontenerlist.append(tmpKontener)
            if select_char == '4':
                for i in range(len(self.zamowienia)):
                    self.zamowienia[i].print_zamowienie()
            elif select_char == "q" or select_char == "Q":
                return