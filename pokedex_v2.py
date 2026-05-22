import os

pokedex = (
    (1, "Bulbasaur", "Planta/Veneno", 0.7, 6.9, 45, "Kanto"),
    (2, "Ivysaur", "Planta/Veneno", 1.0, 13.0, 60, "Kanto"),
    (3, "Venusaur", "Planta/Veneno", 2.0, 100.0, 80, "Kanto"),
    (4, "Charmander", "Fogo", 0.6, 8.5, 39, "Kanto"),
    (5, "Charmeleon", "Fogo", 1.1, 19.0, 58, "Kanto"),
    (6, "Charizard", "Fogo/Voador", 1.7, 90.5, 78, "Kanto"),
    (7, "Squirtle", "Água", 0.5, 9.0, 44, "Kanto"),
    (8, "Wartortle", "Água", 1.0, 22.5, 59, "Kanto"),
    (9, "Blastoise", "Água", 1.6, 85.5, 79, "Kanto"),
    (10, "Caterpie", "Inseto", 0.3, 2.9, 45, "Kanto"),
    (11, "Metapod", "Inseto", 0.7, 9.9, 50, "Kanto"),
    (12, "Butterfree", "Inseto/Voador", 1.1, 32.0, 60, "Kanto"),
    (13, "Weedle", "Inseto/Veneno", 0.3, 3.2, 40, "Kanto"),
    (14, "Kakuna", "Inseto/Veneno", 0.6, 10.0, 45, "Kanto"),
    (15, "Beedrill", "Inseto/Veneno", 1.0, 29.5, 65, "Kanto"),
    (16, "Pidgey", "Normal/Voador", 0.3, 1.8, 40, "Kanto"),
    (17, "Pidgeotto", "Normal/Voador", 1.1, 30.0, 63, "Kanto"),
    (18, "Pidgeot", "Normal/Voador", 1.5, 39.5, 83, "Kanto"),
    (19, "Rattata", "Normal", 0.3, 3.5, 30, "Kanto"),
    (20, "Raticate", "Normal", 0.7, 18.5, 55, "Kanto"),
    (21, "Spearow", "Normal/Voador", 0.3, 2.0, 40, "Kanto"),
    (22, "Fearow", "Normal/Voador", 1.2, 38.0, 65, "Kanto"),
    (23, "Ekans", "Veneno", 2.0, 6.9, 35, "Kanto"),
    (24, "Arbok", "Veneno", 3.5, 65.0, 60, "Kanto"),
    (25, "Pikachu", "Elétrico", 0.4, 6.0, 35, "Kanto"),
    (26, "Raichu", "Elétrico", 0.8, 30.0, 60, "Kanto"),
    (27, "Sandshrew", "Terrestre", 0.6, 12.0, 50, "Kanto"),
    (28, "Sandslash", "Terrestre", 1.0, 29.5, 75, "Kanto"),
    (29, "Nidoran♀", "Veneno", 0.4, 7.0, 55, "Kanto"),
    (30, "Nidorina", "Veneno", 0.8, 20.0, 70, "Kanto"),
    (31, "Nidoqueen", "Veneno/Terrestre", 1.3, 60.0, 90, "Kanto"),
    (32, "Nidoran♂", "Veneno", 0.5, 9.0, 46, "Kanto"),
    (33, "Nidorino", "Veneno", 0.9, 19.5, 61, "Kanto"),
    (34, "Nidoking", "Veneno/Terrestre", 1.4, 62.0, 81, "Kanto"),
    (35, "Clefairy", "Fada", 0.6, 7.5, 70, "Kanto"),
    (36, "Clefable", "Fada", 1.3, 40.0, 95, "Kanto"),
    (37, "Vulpix", "Fogo", 0.6, 9.9, 38, "Kanto"),
    (38, "Ninetales", "Fogo", 1.1, 19.9, 73, "Kanto"),
    (39, "Jigglypuff", "Normal/Fada", 0.5, 5.5, 115, "Kanto"),
    (40, "Wigglytuff", "Normal/Fada", 1.0, 12.0, 140, "Kanto"),
    (41, "Zubat", "Veneno/Voador", 0.8, 7.5, 40, "Kanto"),
    (42, "Golbat", "Veneno/Voador", 1.6, 55.0, 75, "Kanto"),
    (43, "Oddish", "Planta/Veneno", 0.5, 5.4, 45, "Kanto"),
    (44, "Gloom", "Planta/Veneno", 0.8, 8.6, 60, "Kanto"),
    (45, "Vileplume", "Planta/Veneno", 1.2, 18.6, 75, "Kanto"),
    (46, "Paras", "Inseto/Planta", 0.3, 5.4, 35, "Kanto"),
    (47, "Parasect", "Inseto/Planta", 1.0, 29.5, 60, "Kanto"),
    (48, "Venonat", "Inseto/Veneno", 1.0, 30.0, 60, "Kanto"),
    (49, "Venomoth", "Inseto/Veneno", 1.5, 12.5, 70, "Kanto"),
    (50, "Diglett", "Terrestre", 0.2, 0.8, 10, "Kanto"),
    (51, "Dugtrio", "Terrestre", 0.7, 33.3, 35, "Kanto"),
    (52, "Meowth", "Normal", 0.4, 4.2, 40, "Kanto"),
    (53, "Persian", "Normal", 1.0, 32.0, 65, "Kanto"),
    (54, "Psyduck", "Água", 0.8, 19.6, 50, "Kanto"),
    (55, "Golduck", "Água", 1.7, 76.6, 80, "Kanto"),
    (56, "Mankey", "Lutador", 0.5, 28.0, 40, "Kanto"),
    (57, "Primeape", "Lutador", 1.0, 32.0, 65, "Kanto"),
    (58, "Growlithe", "Fogo", 0.7, 19.0, 55, "Kanto"),
    (59, "Arcanine", "Fogo", 1.9, 155.0, 90, "Kanto"),
    (60, "Poliwag", "Água", 0.6, 12.4, 40, "Kanto"),
    (61, "Poliwhirl", "Água", 1.0, 20.0, 65, "Kanto"),
    (62, "Poliwrath", "Água/Lutador", 1.3, 54.0, 90, "Kanto"),
    (63, "Abra", "Psíquico", 0.9, 19.5, 25, "Kanto"),
    (64, "Kadabra", "Psíquico", 1.3, 56.5, 40, "Kanto"),
    (65, "Alakazam", "Psíquico", 1.5, 48.0, 55, "Kanto"),
    (66, "Machop", "Lutador", 0.8, 19.5, 70, "Kanto"),
    (67, "Machoke", "Lutador", 1.5, 70.5, 80, "Kanto"),
    (68, "Machamp", "Lutador", 1.6, 130.0, 90, "Kanto"),
    (69, "Bellsprout", "Planta/Veneno", 0.7, 4.0, 50, "Kanto"),
    (70, "Weepinbell", "Planta/Veneno", 1.0, 6.4, 65, "Kanto"),
    (71, "Victreebel", "Planta/Veneno", 1.7, 15.5, 80, "Kanto"),
    (72, "Tentacool", "Água/Veneno", 0.9, 45.5, 40, "Kanto"),
    (73, "Tentacruel", "Água/Veneno", 1.6, 55.0, 80, "Kanto"),
    (74, "Geodude", "Pedra/Terrestre", 0.4, 20.0, 40, "Kanto"),
    (75, "Graveler", "Pedra/Terrestre", 1.0, 105.0, 55, "Kanto"),
    (76, "Golem", "Pedra/Terrestre", 1.4, 300.0, 80, "Kanto"),
    (77, "Ponyta", "Fogo", 1.0, 30.0, 50, "Kanto"),
    (78, "Rapidash", "Fogo", 1.7, 95.0, 65, "Kanto"),
    (79, "Slowpoke", "Água/Psíquico", 1.2, 36.0, 90, "Kanto"),
    (80, "Slowbro", "Água/Psíquico", 1.6, 78.5, 95, "Kanto"),
    (81, "Magnemite", "Elétrico/Aço", 0.3, 6.0, 25, "Kanto"),
    (82, "Magneton", "Elétrico/Aço", 1.0, 60.0, 50, "Kanto"),
    (83, "Farfetch'd", "Normal/Voador", 0.8, 15.0, 52, "Kanto"),
    (84, "Doduo", "Normal/Voador", 1.4, 39.2, 35, "Kanto"),
    (85, "Dodrio", "Normal/Voador", 1.8, 85.2, 60, "Kanto"),
    (86, "Seel", "Água", 1.1, 90.0, 65, "Kanto"),
    (87, "Dewgong", "Água/Gelo", 1.7, 120.0, 90, "Kanto"),
    (88, "Grimer", "Veneno", 0.9, 30.0, 80, "Kanto"),
    (89, "Muk", "Veneno", 1.2, 30.0, 105, "Kanto"),
    (90, "Shellder", "Água", 0.3, 4.0, 30, "Kanto"),
    (91, "Cloyster", "Água/Gelo", 1.5, 132.5, 50, "Kanto"),
    (92, "Gastly", "Fantasma/Veneno", 1.3, 0.1, 30, "Kanto"),
    (93, "Haunter", "Fantasma/Veneno", 1.6, 0.1, 45, "Kanto"),
    (94, "Gengar", "Fantasma/Veneno", 1.5, 40.5, 60, "Kanto"),
    (95, "Onix", "Pedra/Terrestre", 8.8, 210.0, 35, "Kanto"),
    (96, "Drowzee", "Psíquico", 1.0, 32.4, 60, "Kanto"),
    (97, "Hypno", "Psíquico", 1.6, 75.6, 85, "Kanto"),
    (98, "Krabby", "Água", 0.4, 6.5, 30, "Kanto"),
    (99, "Kingler", "Água", 1.3, 60.0, 55, "Kanto"),
    (100, "Voltorb", "Elétrico", 0.5, 10.4, 40, "Kanto"),
    (101, "Electrode", "Elétrico", 1.2, 66.6, 60, "Kanto"),
    (102, "Exeggcute", "Planta/Psíquico", 0.4, 2.5, 60, "Kanto"),
    (103, "Exeggutor", "Planta/Psíquico", 2.0, 120.0, 95, "Kanto"),
    (104, "Cubone", "Terrestre", 0.4, 6.5, 50, "Kanto"),
    (105, "Marowak", "Terrestre", 1.0, 45.0, 60, "Kanto"),
    (106, "Hitmonlee", "Lutador", 1.5, 49.8, 50, "Kanto"),
    (107, "Hitmonchan", "Lutador", 1.4, 50.2, 50, "Kanto"),
    (108, "Lickitung", "Normal", 1.2, 65.5, 90, "Kanto"),
    (109, "Koffing", "Veneno", 0.6, 1.0, 40, "Kanto"),
    (110, "Weezing", "Veneno", 1.2, 9.5, 65, "Kanto"),
    (111, "Rhyhorn", "Terrestre/Pedra", 1.0, 115.0, 80, "Kanto"),
    (112, "Rhydon", "Terrestre/Pedra", 1.9, 120.0, 105, "Kanto"),
    (113, "Chansey", "Normal", 1.1, 34.6, 250, "Kanto"),
    (114, "Tangela", "Planta", 1.0, 35.0, 65, "Kanto"),
    (115, "Kangaskhan", "Normal", 2.2, 80.0, 105, "Kanto"),
    (116, "Horsea", "Água", 0.4, 8.0, 30, "Kanto"),
    (117, "Seadra", "Água", 1.2, 25.0, 55, "Kanto"),
    (118, "Goldeen", "Água", 0.6, 15.0, 45, "Kanto"),
    (119, "Seaking", "Água", 1.3, 39.0, 80, "Kanto"),
    (120, "Staryu", "Água", 0.8, 34.5, 30, "Kanto"),
    (121, "Starmie", "Água/Psíquico", 1.1, 80.0, 60, "Kanto"),
    (122, "Mr. Mime", "Psíquico/Fada", 1.3, 54.5, 40, "Kanto"),
    (123, "Scyther", "Inseto/Voador", 1.5, 56.0, 70, "Kanto"),
    (124, "Jynx", "Gelo/Psíquico", 1.4, 40.6, 65, "Kanto"),
    (125, "Electabuzz", "Elétrico", 1.1, 30.0, 65, "Kanto"),
    (126, "Magmar", "Fogo", 1.3, 44.5, 65, "Kanto"),
    (127, "Pinsir", "Inseto", 1.5, 55.0, 65, "Kanto"),
    (128, "Tauros", "Normal", 1.4, 88.4, 75, "Kanto"),
    (129, "Magikarp", "Água", 0.9, 10.0, 20, "Kanto"),
    (130, "Gyarados", "Água/Voador", 6.5, 235.0, 95, "Kanto"),
    (131, "Lapras", "Água/Gelo", 2.5, 220.0, 130, "Kanto"),
    (132, "Ditto", "Normal", 0.3, 4.0, 48, "Kanto"),
    (133, "Eevee", "Normal", 0.3, 6.5, 55, "Kanto"),
    (134, "Vaporeon", "Água", 1.0, 29.0, 130, "Kanto"),
    (135, "Jolteon", "Elétrico", 0.8, 24.5, 65, "Kanto"),
    (136, "Flareon", "Fogo", 0.9, 25.0, 65, "Kanto"),
    (137, "Porygon", "Normal", 0.8, 36.5, 65, "Kanto"),
    (138, "Omanyte", "Pedra/Água", 0.4, 7.5, 35, "Kanto"),
    (139, "Omastar", "Pedra/Água", 1.0, 35.0, 70, "Kanto"),
    (140, "Kabuto", "Pedra/Água", 0.5, 11.5, 30, "Kanto"),
    (141, "Kabutops", "Pedra/Água", 1.3, 40.5, 60, "Kanto"),
    (142, "Aerodactyl", "Pedra/Voador", 1.8, 59.0, 80, "Kanto"),
    (143, "Snorlax", "Normal", 2.1, 460.0, 160, "Kanto"),
    (144, "Articuno", "Gelo/Voador", 1.7, 55.4, 90, "Kanto"),
    (145, "Zapdos", "Elétrico/Voador", 1.6, 52.6, 90, "Kanto"),
    (146, "Moltres", "Fogo/Voador", 2.0, 60.0, 90, "Kanto"),
    (147, "Dratini", "Dragão", 1.8, 3.3, 41, "Kanto"),
    (148, "Dragonair", "Dragão", 4.0, 16.5, 61, "Kanto"),
    (149, "Dragonite", "Dragão/Voador", 2.2, 210.0, 91, "Kanto"),
    (150, "Mewtwo", "Psíquico", 2.0, 122.0, 106, "Kanto"),
    (151, "Mew", "Psíquico", 0.4, 4.0, 100, "Kanto")
)

emojis = {
    "aço": "🔩 ", "água": "💧 ", "dragão": "🐲 ", "elétrico": "⚡ ", 
    "fada": "🧚 ", "fantasma ": "👻 ", "fogo": "🔥 ", "gelo": "❄️ ", 
    "inseto": "🐛 ", "lutador": "🥊 ", "normal": "⚪ ", "pedra": "🪨 ", 
    "planta": "🍃 ", "psíquico": "🔮 ", "terrestre": "⛰️  ", "veneno": "☠️  ", 
    "voador": "🕊️  "
}

favoritos = []

def buscar_pokemon(entrada):
    for p in pokedex:
        if str(p[0]) == entrada or p[1].lower() == entrada:
            return p
    return None

def mostrar_pokemon(p):
    os.system('cls')
    largura = 30
    
    print("\n" + "═" * largura)
    print("✨ POKÉDEX ✨".center(largura))
    print("═" * largura)
    print(f"#{p[0]:03d} - {p[1]}".center(largura))
    print("─" * largura)
    print(f"🏷️  Tipo: {p[2]}")
    print(f"❤️  HP: {p[5]}")
    print(f"📏 Altura: {p[3]} m")
    print(f"⚖️  Peso: {p[4]} kg")
    print(f"🗺️  Região: {p[6]}")
    print("═" * largura)
    print("\n" + "[ Aperte Enter para voltar ]".center(largura))
    input()
    os.system('cls')

def filtrar_por_tipo():
    global pokedex
    os.system('cls')
    largura = 54

    print("\n" + "═" * largura)
    print("🏷️  FILTRAR POR TIPO  🏷️".center(largura))
    print("═" * largura)
    print("  🔩 Aço          🔥 Fogo         🍃 Planta")
    print("  💧 Água         ❄️  Gelo         🔮 Psíquico")
    print("  🐲 Dragão       🐛 Inseto       ⛰️  Terrestre")
    print("  ⚡ Elétrico     🥊 Lutador      ☠️  Veneno")
    print("  🧚 Fada         ⚪ Normal       🕊️  Voador")
    print("  👻 Fantasma     🪨  Pedra")
    print("═" * largura)

    tipo = input("\nDigite o tipo: ").strip().lower()

    os.system('cls')
    print("\n" + "═" * largura)
    print(f"🔍 POKÉMON DO TIPO: {tipo.upper()} 🔍".center(largura))
    print("═" * largura)

    encontrou = False
    for p in pokedex:
        if tipo in p[2].lower():
            encontrou = True
            partes_tipo = p[2].split("/")
            t1 = partes_tipo[0].strip()
            e1 = emojis.get(t1.lower(), '')
            tipo_um = f"{e1}{t1}"
            
            if len(partes_tipo) == 2:
                t2 = partes_tipo[1].strip()
                e2 = emojis.get(t2.lower(), '')
                tipo_formatado = f"{tipo_um:<14} | {e2}{t2}"
            else:
                tipo_formatado = tipo_um
            
            print(f"  🔹 #{p[0]:03d}  {p[1]:<12}  {tipo_formatado}")

    if not encontrou:
        print(f"Nenhum Pokémon do tipo '{tipo}' encontrado.".center(largura))

    print("─" * largura)
    print("\n" + "[ Aperte Enter para voltar ]".center(largura))
    input()
    os.system('cls')

def listar_pokemon():
    global pokedex
    pagina, por_pagina, largura = 0, 10, 54

    while True:
        os.system('cls')
        print("\n" + "═" * largura)
        print(f"📗 LISTA POKÉMON (Pág. {pagina + 1}) 📗".center(largura))
        print("═" * largura)

        for p in pokedex[pagina*por_pagina : (pagina+1)*por_pagina]:
            partes_tipo = p[2].split("/")
            t1 = partes_tipo[0].strip()
            e1 = emojis.get(t1.lower(), '')
            tipo_um = f"{e1}{t1}"
            
            if len(partes_tipo) == 2:
                t2 = partes_tipo[1].strip()
                e2 = emojis.get(t2.lower(), '')
                tipo_formatado = f"{tipo_um:<14} | {e2}{t2}"
            else:
                tipo_formatado = tipo_um
            
            print(f"  🔹 #{p[0]:03d}  {p[1]:<12}  {tipo_formatado}")

        print("─" * largura)
        print(" ◀ [V] Voltar  │  ❌ [S] Sair  │  ▶ [P] Próxima".center(largura))
        print("═" * largura)

        escolha = input("\nEscolha: ").strip().lower()
        if escolha == "p" and (pagina+1)*por_pagina < len(pokedex): 
            pagina += 1
        elif escolha == "v" and pagina > 0: 
            pagina -= 1
        elif escolha == "s": 
            os.system('cls')
            break

def favoritar_pokemon():
    entrada = input("\nDigite o ID ou nome do Pokémon: ").strip().lower()

    for p in pokedex:
        if str(p[0]) == entrada or p[1].lower() == entrada:
            if p in favoritos:
                print("⚠️ Esse Pokémon já está nos favoritos!")
                return

            favoritos.append(p)
            os.system('cls')
            print(f"⭐ {p[1]} adicionado aos favoritos!")
            return

    print("❌ Pokémon não encontrado!")

def mostrar_favoritos():
    global favoritos
    os.system('cls')
    largura = 54

    print("\n" + "═" * largura)
    print("❤️  FAVORITOS  ❤️".center(largura))
    print("═" * largura)

    if not favoritos:
        print("Nenhum Pokémon favoritado ainda.".center(largura))
        print("═" * largura)
        print("\n" + "[ Aperte Enter para voltar ]".center(largura))
        input()
        return

    for p in favoritos:
        partes_tipo = p[2].split("/")
        t1 = partes_tipo[0].strip()
        e1 = emojis.get(t1.lower(), '')
        tipo_um = f"{e1}{t1}"
        
        if len(partes_tipo) == 2:
            t2 = partes_tipo[1].strip()
            e2 = emojis.get(t2.lower(), '')
            tipo_formatado = f"{tipo_um:<14} | {e2}{t2}"
        else:
            tipo_formatado = tipo_um
        
        print(f"  🔹 #{p[0]:03d}  {p[1]:<12}  {tipo_formatado}")

    print("─" * largura)
    print("\n" + "[ Aperte Enter para voltar ]".center(largura))
    input()
    os.system('cls')

def menu():
    while True:
        print("\n-------- POKEDEX ---------")
        print(" ")
        print("1 - 🔍 Buscar Pokémon")
        print("2 - 📗 Listar Pokémon")
        print("3 - 🏷️  Filtrar por tipo")
        print("4 - ⭐ Favoritar Pokémon")
        print("5 - ❤️  Ver favoritos")
        print("6 - ❌ Sair")

        opcao = input("\nEscolha: ").strip()

        if opcao == "1":
            entrada = input("Nome ou ID: ").strip().lower()
            resultado = buscar_pokemon(entrada)
            if resultado:
                mostrar_pokemon(resultado)
            else:
                print("❌ Não encontrado!")

        elif opcao == "2":
            listar_pokemon()

        elif opcao == "3":
            filtrar_por_tipo()

        elif opcao == "4":
            favoritar_pokemon()

        elif opcao == "5":
            mostrar_favoritos()
        
        elif opcao == "6":
            print("Encerrando Pokédex...")
            break
        else:
            print("Opção inválida!")

menu()
