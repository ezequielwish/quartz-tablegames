from classes import Player

def set_default():
    autunita = ["Autunita" for c in range(18)]
    quartzo = ["Quartzo" for c in range(15)]
    rubelita = ["Rubelita" for c in range(12)]
    esmeralda = ["Esmeralda" for c in range(10)]
    safira = ["Safira" for c in range(7)]
    rubi = ["Rubi" for c in range(4)]
    ambar = ["Âmbar" for c in range(2)]

    return autunita + quartzo + rubelita + esmeralda + safira + rubi + ambar

def clean_players_cart(players):
    for player in players:
        player.clean_cart()

cristals = set_default()

player1 = Player(name="Eze")
player2 = Player(name="Megan")
player3 = Player(name="Cris")
player4 = Player(name="Lip")
players = [player1, player2, player3, player4]
alive_players = players[::]

round = 1

for day in range(5):
    print(f"\033[33mDia {day+1}\033[0m")
    # Dia
    while True:
        if len(alive_players) == 0:
            break
        print(f"\033[34mrodada {round}\033[0m")
        for player in players:
            if player in alive_players:
                answer = input(f"{player.name}: [M]Minerar [S]Sair ").upper().strip()
                if answer == "M":
                    cristal = player.mine(cristals)
                    player.cart.append(cristal)
                    cristals.remove(cristal)
                    if cristal == "Autunita":
                        if player.cart.count(cristal) > 1:
                            player.alive = False
                            alive_players.remove(player)
                            cristals += player.cart
                            player.clean_cart()
                            print(f"\033[31m{player.name} se acidentou e seus cristais estão espalhados pela mina!\033[0m")
                elif answer == "S":
                    player.alive = False
                    alive_players.remove(player)
                    print(f"\033[32m{player.name} saiu da mina com segurança!\033[0m")
                    print(f"\033[32mCristais obtidos: {", ".join(player.cart)}\033[0m")
            if len(alive_players) == 1:
                print(f"\033[33m{alive_players[0].name} foi retirado à força...\033[0m")
                print(f"\033[32mCristais obtidos: {", ".join(alive_players[0].cart)}\033[0m")
                alive_players[0].alive = False
                alive_players.remove(alive_players[0])
        round += 1
    cristals = set_default()
    alive_players = players[::]
    clean_players_cart(players)
    # venda
