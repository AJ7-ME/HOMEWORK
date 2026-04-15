class Dog:
    species = "Canine"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def display(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", self.species)
        print()
dog1 = Dog("Jon", "Golden retriever")
dog2 = Dog("Max", "Labrador")
dog1.display()
dog2.display()