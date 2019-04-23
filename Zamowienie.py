class Zamowienie:
    def __init__(self):
        self.id = -1
        self.kontener = None
        self.paid = False

    def set_zamowienie(self, id, kontener, paid):
        self.id = id
        self.kontener = kontener
        self.paid = paid

    def print_zamowienie(self, id):
        print("ID: {} \n"
              "Zamowienie opłacone? {}\n"
              "Na kontener o wielkości {} litrów kosztuje {}zł\n\n".format(id, self.paid, self.kontener.size,
                                                                       self.kontener.price))
