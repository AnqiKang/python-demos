class Restaurant():
    def make_reservation(self, party_size):
        print(f"Booked a table for {party_size}")


class Steakhouse(Restaurant):
    pass


class Bar():
    def make_reservation(self, party_size):
        print(f"booked a lounge for {party_size}")


class BarAndGrill(Steakhouse, Bar):
    pass


bag = BarAndGrill()
# default, DFS : depth first search
bag.make_reservation(2)  # Booked a table for 2
