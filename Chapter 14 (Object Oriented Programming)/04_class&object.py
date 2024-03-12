class PartyAnimal:

    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")

j.party()
s.party()

# Constructors can have additional parameters. These can be used to set up instance variables for the particular instance of the class (i.e., for the particular object)
