class Avenger:
    def __init__(self, name, age, gender, power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.power = power
        self.weapon = weapon

    def display(self):
        print(self.name, self.power, self.weapon)

    def is_leader(self):
        if self.name == "Captain America":
            print(self.name, "is a leader")
        else:
            print(self.name, "is not a leader")


# objects
a1 = Avenger("Captain America", 100, "Male", "Strength", "Shield")
a2 = Avenger("Iron Man", 45, "Male", "Technology", "Armor")

a1.display()
a1.is_leader()

a2.display()
a2.is_leader()
