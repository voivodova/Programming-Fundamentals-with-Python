class Hero:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def cast_spell(self, spell_name, mp_needed):
        if self.mp >= mp_needed:
            self.mp -= mp_needed
            return f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!"
        else:
            return f"{self.name} does not have enough MP to cast {spell_name}!"

    def take_damage(self, damage, attacker):
        self.hp -= damage
        if self.hp > 0:
            return f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!"
        else:
            return f"{self.name} has been killed by {attacker}!"

    def recharge(self, amount):
        if self.mp + amount > 200:
            amount_recovered = 200 - self.mp
            self.mp = 200
        else:
            amount_recovered = amount
            self.mp += amount
        return f"{self.name} recharged for {amount_recovered} MP!"

    def heal(self, amount):
        if self.hp + amount > 100:
            amount_recovered = 100 - self.hp
            self.hp = 100
        else:
            amount_recovered = amount
            self.hp += amount
        return f"{self.name} healed for {amount_recovered} HP!"


n = int(input())
heroes = []

for _ in range(n):
    hero_info = input().split()
    hero_name = hero_info[0]
    hero_hp = int(hero_info[1])
    hero_mp = int(hero_info[2])
    hero = Hero(hero_name, hero_hp, hero_mp)
    heroes.append(hero)

command = input()
while command != "End":
    command_args = command.split(" - ")
    action = command_args[0]
    hero_name = command_args[1]

    hero = [h for h in heroes if h.name == hero_name][0]

    if action == "CastSpell":
        mp_needed = int(command_args[2])
        spell_name = command_args[3]
        print(hero.cast_spell(spell_name, mp_needed))
    elif action == "TakeDamage":
        damage = int(command_args[2])
        attacker = command_args[3]
        print(hero.take_damage(damage, attacker))
        if hero.hp <= 0:
            heroes.remove(hero)
    elif action == "Recharge":
        amount = int(command_args[2])
        print(hero.recharge(amount))
    elif action == "Heal":
        amount = int(command_args[2])
        print(hero.heal(amount))

    command = input()

for hero in heroes:
    print(hero.name)
    print(f"  HP: {hero.hp}")
    print(f"  MP: {hero.mp}")
