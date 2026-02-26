from random import choice, shuffle

class Player:
    def __init__(self, name):
        self.name = name
        self.cart = []
        self.cards = []
        self.alive = True
    
    def mine(self, cristals):
        shuffle(cristals)
        print(f"{self.name} está minerando...")
        cristal = choice(cristals) # Minera o cristal
        print(self.name, "minerou", cristal)
        return cristal

    def use_card(self):
        pass
    
    def clean_cart(self):
        self.cart.clear()

