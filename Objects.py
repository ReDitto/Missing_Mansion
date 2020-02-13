class things():
    def __init__ (self, name, desc):
        self.name = name
        self.description = desc

        def __str__ (self):
            return "{}\n".format(self.name, self.description)

        class weapon(things):
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