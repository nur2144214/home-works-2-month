class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, super_power, health_points, catch_phrase):
        self.name = name
        self.nickname = nickname
        self.super_power = super_power
        self.health_points = health_points
        self.catch_phrase = catch_phrase

    def get_hero_name(self):
        return self.name

    def double_health(self):
        self.health_points = 2*self.health_points

    def __str__(self):
        return (f'nickname: {self.nickname}, '
                f'super power: {self.super_power}, health points: {self.health_points}')

    def __len__(self):
        return len(self.catch_phrase)


freon = SuperHero('Lucius', 'Freon', 'freeze', 250,
                  'where is my super soup')
freon.double_health()
print(freon.get_hero_name())
print(len(freon))
print(freon)
