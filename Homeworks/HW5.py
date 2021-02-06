class Animals():
    def __init__(self, animal, species):
        self.species = species
        self.animal = animal
    def print_species(self):
        print(self.species)
    def print_animal(self):
        print(self.animal)

class Dogs(Animals):
    def __init__(self, species, animal, name, age, gender):
        super().__init__(species, animal)
        self.name = name
        self.age = age
        self.gender = gender
        self.says = "\'Dogs bark\'"
    def print_name(self):
        print(self.name)
    def print_age(self):
        print(self.age)
    def print_gender(self):
        print(self.gender)
    def print_info(self):
        print(self.animal + " " + self.species + " " + self.name + " " + str(self.age) + " " +  self.gender + " " + self.says)

class Cats(Animals):
    def __init__(self, species, animal, name, age, gender):
        super().__init__(species, animal)
        self.name = name
        self.age = age
        self.gender = gender
        self.says = "\'Cats meow\'"
    def print_name(self):
        print(self.name)
    def print_age(self):
        print(self.age)
    def print_gender(self):
        print(self.gender)
    def print_info(self):
        print(self.animal + " " + self.species + " " + self.name + " " + str(self.age) + " " + self.gender + " " + self.says )


