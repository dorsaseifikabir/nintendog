class Nintendogs:
    def __init__(self, name, character, breed, sex, hunger, thirst, happiness, energy, cleanliness):
        self.name = name
        self.character = character
        self.breed = breed
        self.sex = sex
        self.hunger = hunger
        self.thirst = thirst
        self.happiness = happiness
        self.energy = energy
        self.cleanliness = cleanliness

    def __str__(self):
        return self.name

    def feed(self):
        if self.hunger <= 20 and self.character == 'active, loves to play':
            print(f"{self.name} is munching on the chow.")
            self.happiness = min(100, self.happiness + 20)
            self.hunger = min(100, self.hunger + 50)
            self.cleanliness = max(0, self.cleanliness - 5)
        elif self.hunger <= 40 and self.character == 'lazy, loves eating and sleeping':
            print(f"{self.name} is gulping down food like there is no tomorrow!")
            self.happiness = min(100, self.happiness + 30)
            self.hunger = min(100, self.hunger + 50)
            self.cleanliness = max(0, self.cleanliness - 5)
        else:
            print(f"{self.name} is not hungry!")

    def give_water(self):
        if self.thirst <= 40:
            print(f"{self.name} is drinking and splashing water every where!")
            self.happiness = min(100, self.happiness + 10)
            self.thirst = min(100, self.thirst + 50)
        else:
            print(f"{self.name} is not thirsty!")

    def walk(self):
        if self.energy >= 20 and self.character == 'active, loves to play':
            print("let's go on an adventure together!")
            self.happiness = min(100, self.happiness + 30)
            self.energy = max(0, self.energy - 20)
            self.hunger = max(0, self.hunger - 20)
            self.thirst = max(0, self.thirst - 20)
            self.cleanliness = max(0, self.cleanliness - 20)
        elif self.energy >= 20 and self.character == 'lazy, loves eating and sleeping':
            print("let's go around the block a few times.")
            self.happiness = min(100, self.happiness + 20)
            self.energy = max(0, self.energy - 30)
            self.hunger = max(0, self.hunger - 30)
            self.thirst = max(0, self.thirst - 20)
            self.cleanliness = max(0, self.cleanliness - 10)
        else:
            print(f"{self.name} is too tired!")

    def play_fetch(self):
        if self.energy >= 20 and self.character == 'active, loves to play':
            print("let's play fetch till the sun goes down!")
            self.happiness = min(100, self.happiness + 40)
            self.energy = max(0, self.energy - 20)
            self.hunger = max(0, self.hunger - 20)
            self.thirst = max(0, self.thirst - 20)
        elif self.energy >= 40 and self.character == 'lazy, loves eating and sleeping':
            print("let's play fetch untill dinner.")
            self.happiness = min(100, self.happiness + 30)
            self.energy = max(0, self.energy - 30)
            self.hunger = max(0, self.hunger - 30)
            self.thirst = max(0, self.thirst - 20)
        else:
            print(f"{self.name} is too tired!")

    def bath(self):
        if self.cleanliness <= 20:
            print(f"{self.name} looks squeaky clean after the bath!")
            self.energy = min(100, self.energy + 10)
            self.thirst = max(0, self.thirst - 20)
        else:
            print(f"{self.name} looks clean!")

    def cuddle(self):
        print(f"{self.name} loves the pets!")
        self.happiness = min(100, self.happiness + 50)

    def sleep(self):
        if self.energy <= 20 and self.character == 'active, loves to play':
            print(f"{self.name} needs a nap!")
            self.energy = min(100, self.energy + 50)
            self.thirst = max(0, self.thirst - 20)
        elif self.energy <= 40 and self.character == 'lazy, loves eating and sleeping':
            print(f"{self.name} is dog tired")
            self.energy = min(100, self.energy + 50)
            self.thirst = max(0, self.thirst - 20)
        else:
            print(f"{self.name} is not tired!")

    def turn(self):
        self.energy = max(0, self.energy - 5)
        self.hunger = max(0, self.hunger - 5)
        self.thirst = max(0, self.thirst - 5)
        self.cleanliness = max(0, self.cleanliness - 5)

    def show_status(self):
        print(f"""
            name: {self.name}
            character: {self.character}
            breed: {self.breed}
            sex: {self.sex}
            hunger: {self.hunger}
            thirst: {self.thirst}
            happiness: {self.happiness}
            energy: {self.energy}
            cleanliness: {self.cleanliness}""")
