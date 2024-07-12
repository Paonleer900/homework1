class Hero:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = int(health_points)
        self.catchphrase = catchphrase

    def __str__(self):
        return f"{self.nickname}, {self.superpower}, {self.health_points*2}"

    def name_print(self):
        return self.name

    def nickname_print(self):
        return self.nickname

    def superpower_print(self):
        return self.superpower

    def health_points_print(self):
        return self.health_points * 2

    def catchphrase_print(self):
        return self.catchphrase

    def __len__(self):
        return len(self.catchphrase)

hero1 = Hero("Superman","chelovek is stali","move giant objects and strike with incredible power","10000","I shoot with my eyes")

print(hero1)
print(hero1.name_print())
print(len(hero1))
