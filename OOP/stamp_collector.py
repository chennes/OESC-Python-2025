class StampCollector:
    def __init__(self, country:str):
        self.country = country
    def run(self):
        print(f"Collecting the stamps from {self.country}")