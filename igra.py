from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука"

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "У бойца нет оружия"

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"Монстр {self.name} побежден!"
        else:
            return f"У монстра {self.name} осталось {self.health} здоровья"

def battle(fighter: Fighter, monster: Monster):
    attack_message = fighter.attack()
    print(attack_message)
    damage = 50  # Предположим, что каждое оружие наносит 50 единиц урона
    result = monster.take_damage(damage)
    print(result)

fighter = Fighter("Боец")
monster = Monster("Монстр")

sword = Sword()
fighter.changeWeapon(sword)
battle(fighter, monster)

bow = Bow()
fighter.changeWeapon(bow)
battle(fighter, monster)
