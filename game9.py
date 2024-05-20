import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")
        print(f"У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Начало игры: Битва героев!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if self.computer.is_alive():
                self.computer_turn()
        self.end_game()

    def player_turn(self):
        input("Нажмите Enter, чтобы атаковать.")
        self.player.attack(self.computer)

    def computer_turn(self):
        print("Ход компьютера.")
        self.computer.attack(self.player)

    def end_game(self):
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print("Компьютер победил!")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
