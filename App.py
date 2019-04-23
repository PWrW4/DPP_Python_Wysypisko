from FirmApp import Firm
from KlientApp import Klient


class App:
    if __name__ == '__main__':

        firm = Firm()
        klient = Klient()
        selectChar = "s"
        while selectChar != "q":
            selectChar = input("Select view:\n"
                               "1.Aplikacja Firmy\n"
                               "2.Aplikacja Klienta\n"
                               "q/Q - Exit\n").upper()
            if selectChar not in "12qQ" or len(selectChar) != 1:
                print("No such action")
                continue
            if selectChar == '1':
                firm.main_loop()
            elif selectChar == '2':
                id = int(input("Podaj id klienta: "))
                klient.main_loop(id, firm.kontenerlist, firm.zamowienia)
            elif selectChar == "q" or selectChar == "Q":
                exit()
