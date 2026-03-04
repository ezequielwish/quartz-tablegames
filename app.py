from flask import Flask, jsonify
from classes import Player


def set_default():
    # Cria a lista inicial de cristais com quantidades fixas
    autunita = [("Autunita", 0) for c in range(18)]
    quartzo = [("Quartzo", 1) for c in range(15)]
    rubelita = [("Rubelita", 2) for c in range(12)]
    esmeralda = [("Esmeralda", 3) for c in range(10)]
    safira = [("Safira", 4) for c in range(7)]
    rubi = [("Rubi", 6) for c in range(4)]
    ambar = [("Ambar", 8) for c in range(2)]

    # Junta todos em uma única lista (pool da mina)
    return autunita + quartzo + rubelita + esmeralda + safira + rubi + ambar

def clean_players_cart(players):
    # Limpa o carrinho de todos os jogadores
    for player in players:
        player.clean_cart()
        
def pool_update(cristals):
    pool=[]
    for cristal in cristals:
        if (cristal[0], cristals.count(cristal)) not in pool:
            pool.append((cristal[0], cristals.count(cristal)))
    return pool


app = Flask(__name__)

# Inicializa os cristais disponíveis
cristals = set_default()
pool = pool_update(cristals)

player1 = Player(name="Eze")
player2 = Player(name="Megan")
player3 = Player(name="Cris")
player4 = Player(name="Lip")
players = [player1, player2, player3, player4]
alive_players = [player.name for player in players]


def new_status():
    pool_update(cristals)
    return {
    "alive players": alive_players,
    "pool": pool,
    }

@app.route('/', methods=["GET"])
def status():
    return jsonify(new_status())

def mine(player):
    cristal = player.mine(cristals)
    player.cart_add(cristal)
    cristals.remove(cristal)

    # Regra especial: Autunita repetida mata o jogador
    if cristal == "Autunita":
        if player.cart.count(cristal) > 1:
            player.alive = False
            alive_players.remove(player)
            player.clean_temp_wallet()
            # Cristais voltam para a mina
            cristals += player.cart
            player.clean_cart()
            print(f"\033[31m{player.name} se acidentou e seus cristais estão espalhados pela mina!\033[0m")
    return jsonify(new_status())

if __name__ == "__main__":
    app.run(debug=True)

