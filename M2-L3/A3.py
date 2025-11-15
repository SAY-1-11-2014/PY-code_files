class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
blu = parrot("blu",50)
woo = parrot("woo",100)

print("Blu is a ",blu.species)
print("Woo is a ",woo.species)

print("The name of the bird is ",blu.name," and it's age is ",blu.age)
print("The name of the bird is ",woo.name," and it's age is ",woo.age)