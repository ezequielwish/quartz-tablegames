from classes import Player

def set_default():
    # Cria a lista inicial de cristais com quantidades fixas
    autunita = ["Autunita" for c in range(18)]
    quartzo = ["Quartzo" for c in range(15)]
    rubelita = ["Rubelita" for c in range(12)]
    esmeralda = ["Esmeralda" for c in range(10)]
    safira = ["Safira" for c in range(7)]
    rubi = ["Rubi" for c in range(4)]
    ambar = ["Âmbar" for c in range(2)]

    # Junta todos em uma única lista (pool da mina)
    return autunita + quartzo + rubelita + esmeralda + safira + rubi + ambar

def clean_players_cart(players):
    # Limpa o carrinho de todos os jogadores
    for player in players:
        player.clean_cart()

# Inicializa os cristais disponíveis
cristals = set_default()

# Criação dos jogadores
player1 = Player(name="Eze")
player2 = Player(name="Megan")
player3 = Player(name="Cris")
player4 = Player(name="Lip")
players = [player1, player2, player3, player4]

# Lista de jogadores ainda ativos na rodada
alive_players = players[::]

round = 1  # Contador global de rodadas

# Loop principal (5 dias de jogo)
for day in range(5):
    print(f"\033[33mDia {day+1}\033[0m")
    
    # Fase de mineração do dia
    while True:
        if len(alive_players) == 0:
            break  # Termina o dia quando ninguém mais está na mina

        print(f"\033[34mrodada {round}\033[0m")

        for player in players:
            # Só joga quem ainda está ativo
            if player in alive_players:
                answer = input(f"{player.name}: [M]Minerar [S]Sair ").upper().strip()

                if answer == "M":
                    # Jogador minera um cristal aleatório
                    cristal = player.mine(cristals)
                    player.cart.append(cristal)
                    cristals.remove(cristal)

                    # Regra especial: Autunita repetida mata o jogador
                    if cristal == "Autunita":
                        if player.cart.count(cristal) > 1:
                            player.alive = False
                            alive_players.remove(player)

                            # Cristais voltam para a mina
                            cristals += player.cart
                            player.clean_cart()

                            print(f"\033[31m{player.name} se acidentou e seus cristais estão espalhados pela mina!\033[0m")

                elif answer == "S":
                    # Jogador sai voluntariamente com o que coletou
                    player.alive = False
                    alive_players.remove(player)
                    print(f"\033[32m{player.name} saiu da mina com segurança!\033[0m")
                    print(f"\033[32mCristais obtidos: {', '.join(player.cart)}\033[0m")

            # Se sobrar apenas 1 jogador, ele é removido automaticamente
            if len(alive_players) == 1:
                print(f"\033[33m{alive_players[0].name} foi retirado à força...\033[0m")
                print(f"\033[32mCristais obtidos: {', '.join(alive_players[0].cart)}\033[0m")
                alive_players[0].alive = False
                alive_players.remove(alive_players[0])

        round += 1  # Próxima rodada

    # Reset ao fim do dia
    cristals = set_default()
    alive_players = players[::]
    clean_players_cart(players)

    # TODO: implementar fase de venda
    
