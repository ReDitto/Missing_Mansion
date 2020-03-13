class objects():
    def __init__ (self, name, desc):
        self.name = name
        self.description = desc

        def __str__ (self):
            return "{}\n".format(self.name, self.description)

        class weapon(objects):
            def __init__ (self, name, desc, damage):
                self.damage = damage
                super().__init__(name, desc)

            def __str__ (self):
                return "{}\nDamage: {}".format(self.name, self.desc, self.damage)

        class oddlamp(weapon):
            def __init__ (self):
                super().__init__ (name = "Odd Lamp", desc = "A very peculiarly shaped lamp. It isn't much, but if something were to attack, this would be worth a few hits.", damage = 2)

        class shield(weapon):
            def __init__ (self):
                super().__init__ (name = "Old Shield", desc = "The shield you grabbed off of the armour stand. Since the handles have been broken off, it isn't very viable for defense, however I'm sure you could use it to whack a thing or two.", damage = 5)

class enemy():
    def __init__ (self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class ghost(enemy):
    def __init__ (self):
        super().__init__ (name="Undefinable Attacker", hp=4, damage=1)

class blockingshadow(enemy):
    def __init__ (self):
        super().__init__ (name="Your shadow", hp=1234567891011121314151617181920.5, damage=0)

class realshadow(enemy):
    def __init__ (self):
        super().__init__ (name="Your shadow", hp=1, damage=0)