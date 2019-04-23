from Kontener import Kontener
from Zamowienie import Zamowienie


class Firm:

    def __init__(self):
        self.kontenerlist = [Kontener() for i in range(5)]
        self.zamowienia = []
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
        self.zamowienia[0].set_zamowienie(0, self.kontenerlist[1], False)

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
                tmp_kontener = Kontener()
                tmp_kontener.price = int(input("Podaj cenę kontenera: "))
                tmp_kontener.size = int(input("Podaj rozmiar kontenera: "))
                self.kontenerlist.append(tmp_kontener)
            if select_char == '4':
                for i in range(len(self.zamowienia)):
                    self.zamowienia[i].print_zamowienie()

                zam_input = int(input("Co chcesz zrobić:\n"
                                  "1. Akceptuj zamowienie\n"
                                  "2. Usun zamowienie\n"
                                  "Inna akcja - powrót\n"))

                if zam_input == 1:
                    index = int(input("Podaj index zamowienia do akceptowanie"))
                    if 0 <= index <= len(self.zamowienia):
                        self.zamowienia[index].paid = True
                if zam_input == 2:
                    index = int(input("Podaj index zamowienia do uduniecia"))
                    if 0 <= index <= len(self.zamowienia):
                        self.zamowienia.remove(self.zamowienia[index])

            elif select_char == "q" or select_char == "Q":
                return
