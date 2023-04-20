class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets == 0:
            return "no bullets left"

        self.bullets -= 1
        return "shooting..."

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

