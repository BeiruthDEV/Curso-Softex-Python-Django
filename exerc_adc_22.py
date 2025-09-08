jogadores = {"Alice": 10, "Bruno": 15, "Carla": 20}
jogadores["Alice"] += 5
nome = input("Novo jogador: ")
pontos = int(input("Pontuação: "))
jogadores[nome] = pontos
print(jogadores)