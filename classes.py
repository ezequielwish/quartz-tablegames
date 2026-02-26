from random import choice, shuffle

class Player:
    def __init__(self, name):
        self.name = name
        self.cart = []   # Cristais coletados na rodada atual
        self.cards = []  # Cartas especiais (não implementadas ainda)
        self.alive = True  # Indica se ainda está na mina
    
    def mine(self, cristals):
        # Embaralha a lista para evitar previsibilidade
        shuffle(cristals)

        print(f"{self.name} está minerando...")

        # Escolhe um cristal aleatório da pool disponível
        cristal = choice(cristals)

        print(self.name, "minerou", cristal)
        return cristal

    def use_card(self):
        # Placeholder para sistema de cartas futuras
        pass
    
    def clean_cart(self):
        # Remove todos os cristais do carrinho (reset de rodada)
        self.cart.clear()
        
