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


class AirHero(SuperHero):
    element = 'air'

    def __init__(self, name, nickname, super_power, health_points, catch_phrase, damage, fly):
        super().__init__(name, nickname, super_power, health_points, catch_phrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points = 2 ** self.health_points
        self.fly = True

    def true_phrase(self):
        return 'True in the true phrase'


class EarthHero(SuperHero):
    element = 'earth'

    def __init__(self, name, nickname, super_power, health_points, catch_phrase, damage, fly):
        super().__init__(name, nickname, super_power, health_points, catch_phrase)
        self.damage = damage
        self.fly = fly

    def double_health(self):
        self.health_points = 2**self.health_points
        self.fly = True

    def true_phrase(self):
        return 'True in the true phrase'


airman = AirHero('Leo', 'AirMan', 'wind blast', 10, 'fly high', damage=15, fly=False)
earthman = EarthHero('Max', 'Grounder', 'earth quake', 12, 'solid as rock', damage=20, fly=False)

print(airman)
print(earthman)

airman.double_health()
earthman.double_health()

print(airman)
print(f"Fly status: {airman.fly}")
print(earthman)
print(f"Fly status: {earthman.fly}")

print(airman.true_phrase())
print(earthman.true_phrase())

print(f"AirHero's name: {airman.get_hero_name()}")
print(f"EarthHero's name: {earthman.get_hero_name()}")

print(f"Length of airman's catch phrase: {len(airman)}")
print(f"Length of earthman's catch phrase: {len(earthman)}")


class Villain(AirHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, other):
        other.health_points -= self.damage**2
        return f'the {self.nickname} has caused {self.damage**2}-damage to the {other.nickname}'


sindrome = Villain('Vlad', 'DarkLord', 'shadow strike', 15, 'darkness is power',
                   damage=24, fly=False)

print(sindrome.crit(freon))
