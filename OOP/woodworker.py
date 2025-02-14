class Woodworker:
    def __init__(self, thing:str, wood_species:str):
        self.thing = thing
        self.wood_species = wood_species

    def run(self):
        print(f"Making a {self.thing} out of {self.wood_species}")