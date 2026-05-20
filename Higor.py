pokedex = {
    51: {"nome": "Dugtrio", "tipo": "Terra", "id":"51"},
    52: {"nome": "Meowth", "tipo": "Normal", "id":"52"},
    53: {"nome": "Persian", "tipo": "Normal", "id":"53"},
    54: {"nome": "Psyduck", "tipo": "Água", "id":"54"},
    55: {"nome": "Golduck", "tipo": "Água", "id":"55"},
    56: {"nome": "Mankey", "tipo": "Lutador", "id":"56"},
    57: {"nome": "Primeape", "tipo": "Lutador", "id":"57"},
    58: {"nome": "Growlithe", "tipo": "Fogo", "id":"58"},
    59: {"nome": "Arcaine", "tipo": "Fogo", "id":"59"},
    60: {"nome": "Poliwag", "tipo": "Água", "id":"60"},
    61: {"nome": "Poliwhirl", "tipo": "Água", "id":"61"},
    62: {"nome": "Poliwrath", "tipo": "Água/Lutador", "id":"62"},
    63: {"nome": "Abra", "tipo": "Psíquico", "id":"63"},
    64: {"nome": "Kadabra", "tipo": "Psíquico", "id":"64"},
    65: {"nome": "Alakazam", "tipo": "Psíquico", "id":"65"},
    66: {"nome": "Machop", "tipo": "Lutador", "id":"66"},
    67: {"nome": "Machoke", "tipo": "Lutador", "id":"67"},
    68: {"nome": "Machamp", "tipo": "Lutador", "id":"68"},
    69: {"nome": "Bellsprout", "tipo": "Planta/Venenoso", "id":"69"},
    70: {"nome": "Weepinbell", "tipo": "Planta/Venenoso", "id":"70"},
    71: {"nome": "Victreebel", "tipo": "Planta/Venenoso", "id":"71"},
    72: {"nome": "Tentacool", "tipo": "Água/Venenoso", "id":"72"},
    73: {"nome": "Tentacruel", "tipo": "Água/Venenoso", "id":"73"},
    74: {"nome": "Geodude", "tipo": "Pedra/Terra", "id":"74"},
    75: {"nome": "Graveler", "tipo": "Pedra/Terra", "id":"75"},
}

numero = int(input("Digite o número do Pokémon: "))

if numero in pokedex:
    pokemon = pokedex[numero]

    print("\n=== POKÉMON ENCONTRADO ===")
    print(f"Número: {numero}")
    print(f"Nome: {pokemon['nome']}")
    print(f"Tipo: {pokemon['tipo']}")

else:
    print("Pokémon não encontrado.")