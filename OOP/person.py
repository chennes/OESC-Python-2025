class Person:
    def __init__(self, name:str, job):
        self.name = name
        self.job = job
        self.hobbies = []

    def __repr__(self):
        return self.name
    
    def change_name(self, new_name:str):
        self.name = new_name

    def do_your_job(self):
        self.job()

    def add_hobby(self, hobby):
        if not hasattr(hobby, "run"):
            raise RuntimeError("Invalid hobby given. No run() method.")
        self.hobbies.append(hobby)

    def do_hobby(self):
        for hobby in self.hobbies:
            hobby.run()
