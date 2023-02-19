import pickle

class St:
    def __init__(self, name, age, roll):
        self.name= name
        self.age= age
        self.roll= roll
    def info(self):
        print(self.name, self.age, self.roll)

with open('a.txt', 'rb') as fh:
    data= pickle.load(fh)
    data.info()
    data= pickle.load(fh)
    data.info()
