class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo._Zoo__animals += 1

    def get_info(self, species):
        info = ""
        if species == "mammal":
            info = f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            info = f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            info = f"Birds in {self.name}: {', '.join(self.birds)}"

        return f"{info}\nTotal animals: {Zoo._Zoo__animals}"


name = input()
rows = int(input())

zoo = Zoo(name)

for _ in range(rows):
    species, name = input().split()
    zoo.add_animal(species, name)


species = input()
print(zoo.get_info(species))