class Zamowienie:
    def __init__(self):
        self.id = -1
        self.kontener = None
        self.paid = False

    def set_zamowienie(self,id,kontener,paid):
        self.id = id
        self.kontener = kontener
        self.paid = paid

    def print_zamowienie(self):
        print("ID: {} Zamowienie opłacone? {}\n"
              "Na kontener: {}",
              self.id, self.paid, self.kontener.print_info_noID())
