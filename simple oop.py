class Human:

    def __init__(self, name, height, weight):
        self.height = height
        self.weight = weight
        self.name = name

    def walk(self):
        print(f"{self.name} walking")
        print(f"Height is: {self.height}")
        print(f"Weight is: {self.weight}")
        print("    ")


abhi = Human("abhi", 60, 70)
mohan = Human("mohan", 60, 70)

abhi.walk()
mohan.walk()
