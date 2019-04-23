from Zamowienie import Zamowienie


class Klient:

    def main_loop(self, id, kontenerlist, zamowienia):
        print("Hello in Klient App")

        select_char = "s"
        while select_char != "q":
            select_char = input("Select action:\n"
                                "1.Pokaz oferte\n"
                                "2.Złóż zamowienie\n"
                                "3.Moje zamowienia\n"
                                "q/Q - Exit\n").upper()
            if select_char not in "123qQ" or len(select_char) != 1:
                print("No such action")
                continue
            if select_char == '1':
                for i in range(len(kontenerlist)):
                    kontenerlist[i].print_info(i)
            elif select_char == '2':
                zamowienie = Zamowienie()
                for i in range(len(kontenerlist)):
                    kontenerlist[i].print_info(i)
                kontener_id = int(input("Podaj id kontenera: "))
                zamowienie.set_zamowienie(id, kontenerlist[kontener_id], False)
                zamowienia.append(zamowienie)
            elif select_char == '3':
                for i in range(len(zamowienia)):
                    if zamowienia[i].id == id:
                        zamowienia[i].print_zamowienie(i)
            elif select_char == "q" or select_char == "Q":
                return
