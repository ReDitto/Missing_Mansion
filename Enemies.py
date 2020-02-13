class enemy():
    def __init__ (self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class ghost(enemy):
    def __init__(self):
        super().__init__ (name="Undefinable Attacker", hp=4, damage=1)

class blockingshadow(enemy):
    def __init__(self):
        super().__init__ (name="Your shadow", hp=1234567891011121314151617181920.5, damage=0)

class realshadow(enemy):
    def __init__(self):
        super().__init__ (name="Your shadow", hp=1, damage=0)