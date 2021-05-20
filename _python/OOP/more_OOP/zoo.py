class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_animal(self, name):
        self.animals.append(name)
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(
            "Name:", self.name,
            "Age:", self.age,
            "Health:", self.health,
            "Happiness:", self.happiness
        )
        return self
    
    def feed_animal(self):
        self.health += 10
        self.happiness += 10
        return self

class Lion(Animal):
    def __init__(self, name, age, isFatty, health =70, happiness = 60):
        super().__init__(name, age, health, happiness)
        self.isFatty = isFatty

    def display_info(self):
        Animal.display_info(self)
        return self

    def feed_animal(self):
        if self.isFatty:
            self.health +=12
            self.happiness +=8
        else:
            super().feed_animal()

class Tiger(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)

    def display_info(self):
        Animal.display_info(self)
        return self

    def feed_animal(self):
        super().feed_animal()
        return self

class Bear(Animal):
    def __init__(self, name, age, color, health = 85, happiness = 68):
        super().__init__(name, age, health, happiness)
        self.color = color

    def display_info(self):
        Animal.display_info(self)
        return self

    def feed_animal(self):
        self.health += 12
        self.happiness +=14
        return self


zoo1 = Zoo("Aaron's Zoo")
lion_one = Lion("Simba", 2,False,95,90)
print(lion_one.isFatty)
lion_one.feed_animal()
# lion_one.feed_animal()
lion_two = Lion("Smoky The Cat", 10, True, 50, 60)
zoo1.add_animal(lion_one)
zoo1.add_animal(lion_two)
tiger_one = Tiger("Rajah", 5, 70, 55).feed_animal()
tiger_two = Tiger("Shere Khan", 7, 75, 91)
zoo1.add_animal(tiger_one)
zoo1.add_animal(tiger_two)
bear_one = Bear("Yogi", 20, "brown").feed_animal()
bear_two = Bear("BooBoo", 5, "brown").feed_animal()
zoo1.add_animal(bear_one)
zoo1.add_animal(bear_two)
zoo1.print_all_info()
