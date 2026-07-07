TIPOS = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", 
         "Bug", "Rock", "Ghost", "Dragon", "Steel", "Dark", "Fairy"]
def validar_tipo(tipo):
    if tipo not in TIPOS:
        raise ValueError(f"Tipo inválido: '{tipo}'. Escolha um de: {TIPOS}")
    return tipo
# Validador de tipos, tem que estar a lista e ter no maximo 2 tipos, usando isintance para ser elegante. Além disso ele valida a lista denovo.
def validar_quant_tipos(tipos):
    # Se vier só 1 tipo (string) já transforma em lista
    if isinstance(tipos, str):
        tipos = [tipos] 
    # Verifica formato, se não estiver em lista só para garantir
    if not isinstance(tipos, (list, tuple)):
        raise TypeError("Tipo deve ser string ou lista/tupla")
    # Limitadores de tipos
    if len(tipos) < 1 or len(tipos) > 2:
        raise ValueError("Pokemon deve ter 1 ou 2 tipos")
    # Valida cada tipo da lista
    return [validar_tipo(t) for t in tipos]


class Player:
    def __init__(self, nome, equipe):
        self.nome = nome
        self.equipe = equipe
    def validar_equipe(self):
        # Separado apenas para saber exatamente qual erro que deu.
        if len(self.equipe) > 6:
            raise ValueError("Time inválido tem mas de 6 pokemons")
        elif len(self.equipe) < 1:
            raise ValueError("Seu time precisa ter pelo menos um pokémon")

class Move:
    # o contato seria o fisíco ou especial futuramente vou botar os moves de status ou terreno
    def __init__(self, nome, tipo, contato, dano, alvo, acerto): # Por equanto apenas moves de dano porque eu to com preguiça
        self.nome = nome
        self.tipo = validar_tipo(tipo)
        self.contato = contato
        self.dano = dano
        self.alvo = alvo
        self.acerto = acerto

class Pokemon:
    def __init__(self, poke, nome, hp, cond, tipo, ability, moves, item, stat_hp, stat_atk, stat_deff, stat_spatk, stat_spdeff, stat_speed): 
        self.poke = poke
        self.nome = nome
        self.hp = hp # HP dinamico que atualiza 
        self.cond = cond # cond = condição, ex: queimado 
        self.tipo = validar_quant_tipos(tipo)
        self.ability = ability # por enquanto deixa quieto to com preguiça de codar isso agora, e ability porque é melhor do que escrever habilidade ou abreviar
        self.moves = self.validar_moves(moves)
        self.item = item
        self.stats_base = {
            "hp_base": stat_hp,
            "atk": stat_atk,
            "def": stat_deff,
            "sp_atk": stat_spatk,
            "sp_def": stat_spdeff,
            "speed": stat_speed,
        }
    
    # Validação de moves
    def validar_moves(self, moves):
        if not isinstance(moves, (list, tuple)):
            moves = [moves]
        if len(moves) > 4:
            raise ValueError("Moves inválidos, existem mais de 4 moves")
        elif len(moves) < 1:
            raise ValueError("Moves inválidos, tenha pelo menos 1 move")
        # Verifica se o move é um objeto do move
        for m in moves:
            if not isinstance(m, Move):
                raise TypeError("Todos os moves devem ser objetos Move")
        return moves
    # Validações extras que vão ser usadas em batalha
    def ter_nome(self):
        return self.nome is not None
    def ter_item(self):
        return self.item is not None
    def estar_vivo(self):
        return self.hp > 0
    
import copy # Vai ser usado para copiar o pokemon do dicionario (no caso de pokemon selvagem)
class Batalha:
    def __init__(self, jogador, oponente, trainer=False):
        self.turnos = 0
        self.jogador = jogador
        self.oponente = oponente # Treinador ou Pokemon singular
        self.trainer = trainer # Se for True tem time
        # Define o Pokémon do jogador (busca o primeiro vivo)
        self.pkm_player = self._obter_primeiro_vivo(jogador.equipe)
        if self.pkm_player is None:
            raise ValueError(f"O jogador {jogador.nome} não tem nenhum Pokémon vivo para batalhar!") 

        # Define o Pokémon do oponente e o tipo de oponente 
        if self.trainer:
            self.pkm_oponente = self._obter_primeiro_vivo(oponente.equipe)
            if self.pkm_oponente is None:
                raise ValueError(f"O oponente {trainer.nome} não tem nenhum Pokémon vivo para batalhar!") # Só para garantir que não vai dar um erro
        else:
            # Por enquanto não funciona já que não tem um dicionario com pokemons 
            if not oponente.estar_vivo():
                raise ValueError("O Pokémon selvagem já está desmaiado!")
            self.pkm_oponente = oponente

    # Private porque não sei se usarei isso em outra classe
    def _obter_primeiro_vivo(self, equipe):
        for pkm in equipe:
            if pkm.estar_vivo():
                return pkm
        return None  # Retorna None se todo mundo estiver morto, depois vou fazer um gameover caso isso seja none
    # Condição de vitória, é deselegante mas serve. Não consegui pensar em nada melhor, mesmo sabendo que tem 3 funções de checar se tem algum pokemon vivo.....
    def _time_vivo(self, treinador_ou_pkm):
        # Se for uma batalha de treinador, checa a equipe inteira
        if hasattr(treinador_ou_pkm, 'equipe'):
            return any(pkm.estar_vivo() for pkm in treinador_ou_pkm.equipe)
        # Se for um Pokémon selvagem isolado, checa apenas o HP dele
        return treinador_ou_pkm.estar_vivo()
    def _mostrar_equipe(self, jogador):
        print(f"\n====== EQUIPE DE {jogador.nome.upper()} ======")
        for i, pkm in enumerate(jogador.equipe, start=1):
            # Visual bonito baseado na vida do PKM
            if pkm.estar_vivo():
                status_hp = f"HP: {pkm.hp}"
            else:
                status_hp = "[DESMAIADO]"
            # Mostra a posição, o nome e o hp do pokemon
            print(f"[{i}] {pkm.nome:<12} | {status_hp}")
        print("======================================")
    def _troca_jogador(self):
        while True:
            # 1. Mostra o painel com todo o time
            self._mostrar_equipe(self.jogador)
            try:
                escolha = int(input("Escolha o número do Pokémon que vai entrar: ")) - 1            
                # Se o player selecionou a troca sem querer e quer voltar
                if self.pkm_player.estar_vivo() == True and escolha == -1: # 0 porque a escolha subtrai 1
                    return False # Retoma false pra saber que não teve troca
                if escolha < 0 or escolha >= len(self.jogador.equipe):
                    print("Escolha inválida! Digite um número da lista.")
                    continue 
                pkm_escolhido = self.jogador.equipe[escolha]
                # O pokemon escolhido não pode ser o ativo
                if pkm_escolhido == self.pkm_player:
                    print(f"{pkm_escolhido.nome} já é o seu Pokémon ativo em campo!")
                    continue               
                # Valida se o escolhido está vivo
                if not pkm_escolhido.estar_vivo():
                    print(f"{pkm_escolhido.nome} está desmaiado! Escolha outro.")
                    continue
                self.pkm_player = pkm_escolhido
                print(f"\nVai, {self.pkm_player.nome}!")
                break  
            except ValueError:
                print("Por favor, digite um número válido.")
    def _calculo_dano(self, atacante, defensor, move):
        import random
        # Verifica o tipo de ataque, antigamente minha ideia era usar um str mas o bool é mais facil pro contato
        if move.contato:
            atk = atacante.stats_base["atk"]
            deff = defensor.stats_base["def"]
        else:
            atk = atacante.stats_base["sp_atk"]
            deff = defensor.stats_base["sp_def"]
        if deff == 0: deff = 1 # Pra não dar erro 
        dano_base = (atk / deff) * move.dano
        stab = 1.5 if move.tipo in atacante.tipo else 1.0 # in para verificar a lista já que podem existir dois tipos
        random_multi = random.uniform(0.85, 1.0)
        dano_final = dano_base * stab * random_multi 
        return max(1, int(dano_final)) # Garante que dê pelo menos 1 de dano se a conta der muito baixa, e arredonda para int assim funciona melhor
    def _ataque(self, atacante, defensor, move):
        import random
        print(f"\n{atacante.nome} usou {move.nome}!")
        if random.randint(1, 100) > move.acerto: # Calculo de acerto simplês desconsidenrando os modificadores igual a todos as outras partes
            if atacante.ter_nome(): # Depois eu melhoro o ter_nome()
                print(f"{atacante.nome} errou o ataque!") 
            else:
                print(f"{atacante.poke} errou o ataque!") 
            return
        dano = self._calculo_dano(atacante, defensor, move)
        defensor.hp -= dano 
        if defensor.hp < 0: 
            defensor.hp = 0 # Se ficar menor que 0 seria feio
        if defensor.ter_nome():
            print(f"{defensor.nome} sofreu {dano} do ataque!")
        else:
            print(f"{defensor.poke} sofreu {dano} do ataque!")  

    def comecar_batalha(self):
        if self.oponente.nome:
            print(f"Você foi desafiado, {self.oponente.nome} quer batalhar!")
        else:
            print(f"Você encontrou um {self.pkm_oponente} selvagem!")
        while self._time_vivo(self.jogador) and self._time_vivo(self.oponente):
            if not self.pkm_player.estar_vivo():
                if self.pkm_player.nome:
                    print(f"\n{self.pkm_player.nome} desmaiou e não pode mais lutar!")
                else:
                    print(f"\n{self.pkm_player.poke} desmaiou e não pode mais lutar!")
                self._troca_jogador() 
            if not self.pkm_oponente.estar_vivo():
                import random
                opcoes = [
                    pkm for pkm in self.oponente.equipe
                    if  pkm.estar_vivo() and pkm != self.pkm_oponente
                ]
                if not opcoes: break # Acaba a batalha se o bot não tiver time
                pkm_escolhido = random.choice(opcoes)
                self.pkm_oponente = pkm_escolhido
                print(f"\nVai {self.pkm_oponente.nome}!")
            batalha_continua = self.executar_turno()
            if not batalha_continua: # Se der False, no caso de uma fuga quebra antes das condições.
                break
        self.finalizar_batalha() # Ainda tenho que criar a função anunciando o vencedor e etc....
    def finalizar_batalha(self): # Depois eu modifico isso, por equanto vai ser só o placeholder
        print("\n======== FIM DA BATALHA ========")
        if self._time_vivo(self.jogador) and not self._time_vivo(self.oponente):
            print(f"Parabéns! {self.jogador.nome} venceu a batalha!")
        elif not self._time_vivo(self.jogador) and self._time_vivo(self.oponente):
            print(f"Game Over! {self.jogador.nome} foi derrotado...")
        else:
            print("A batalha terminou.")
    def _menu(self):
        while True:
            print(f"\n╔══════════════════════════════════════════════════════╗")
            print(f"║ {self.pkm_player.nome:<15} HP: {self.pkm_player.hp:<6} vs   {self.pkm_oponente.nome:<14} HP: {self.pkm_oponente.hp:<4} ║")
            print(f"╚══════════════════════════════════════════════════════╝")
            print("┌───────────────────────────┐")
            print("│ 1. LUTAR      2. TIME     │")
            print("│ 3. MOCHILA    4. FUGIR    │")
            print("└───────────────────────────┘")
            escolha = input("O que você vai fazer? ").strip() # Strip apenas pela elegancia 
            if escolha == "1":
                move = self._menu_moves()
                if move is not None:
                    return ("atacar", move)
            elif escolha == "2":
                if self._troca_jogador(): 
                    return ("trocar", None)
                    # Se retornou False(no caso o "voltar") o while True repete    
            elif escolha == "3":
                print("\n[Mochila ainda não implementada! To com preguiça...]")    
            elif escolha == "4":
                if not self.trainer:
                    print(f"Você fugiu da batalha com sucesso!") # por enquanto a fuga vai ser 100% garantida.
                    return ("fugir", None)
                else:
                    print("Você não pode fugir de batalhas contra treinadores!")
            else:
                print("Opção inválida!")
    def _menu_moves(self):
        while True:
            print("\n┌──────────────────────────────────────────────┐")
            print("│ MOVES:                             │")
            moves = self.pkm_player.moves
            # Loop de 2 em 2 para fazer as duas colunas
            for i in range(0, len(moves), 2):
                # Move da esquerda (sempre existe no loop)
                m_esq = moves[i]
                txt_esq = f"[{i+1}] {m_esq.nome} (D:{m_esq.dano}|A:{m_esq.acerto}%)"
                # Move da direita (só gera texto se ele existir na lista)
                if i + 1 < len(moves):
                    m_dir = moves[i+1]
                    txt_dir = f"[{i+2}] {m_dir.nome} (D:{m_dir.dano}|A:{m_dir.acerto}%)"
                else:
                    txt_dir = "" # Fica vazio se o Pokémon tiver golpes ímpares (ex: 1 ou 3 moves)
                # O :<26 formata o texto para ocupar exatamente 26 espaços
                print(f"│ {txt_esq:<26} {txt_dir:<26} │")   
            print("│ [0] VOLTAR                                   │")
            print("└──────────────────────────────────────────────┘")
            try:
                escolha = int(input("Escolha um movimento: "))
                if escolha == 0:
                    return None  # Indica que o jogador quer voltar ao menu principal      
                if 1 <= escolha <= len(moves):
                    return moves[escolha - 1]
                else:
                    print("Número inválido!")
            except ValueError:
                print("Por favor, digite um número válido.")
    def executar_turno(self):
        self.turnos += 1
        print(f"\n======== TURNO {self.turnos} ========")
        acao_player = self._menu() # A saida é em forma de tupla ()
        acao_tipo = acao_player[0]
        acao_detalhe = acao_player[1] # Se for move porque a trocas já acontecem dentro das funções
        if acao_tipo == "fugir":
            print("Fugiu com sucesso!")
            return False
        # Decisão do NPC, depois do fugir porque se o usuário foge não importa.
        acao_bot = self.npc()
        bot_tipo = acao_bot[0]
        bot_detalhe = acao_bot[1]
        # Player Trocou
        if acao_tipo == "trocar":
            if bot_tipo == "atacar":
                self._ataque(self.pkm_oponente, self.pkm_player, bot_detalhe)
        # Bot Trocou
        elif bot_tipo == "trocar":
            if acao_tipo == "atacar":
                self._ataque(self.pkm_player, self.pkm_oponente, acao_detalhe)
        # Os dois atacando
        elif acao_tipo == "atacar" and bot_tipo == "atacar":
            vel_player = self.pkm_player.stats_base["speed"]
            vel_bot = self.pkm_oponente.stats_base["speed"]
            if vel_player >= vel_bot:
                self._ataque(self.pkm_player, self.pkm_oponente, acao_detalhe)
                # Verifica se o oponente morreu antes do movimento dele
                if self.pkm_oponente.estar_vivo():
                    self._ataque(self.pkm_oponente, self.pkm_player, bot_detalhe)
            else:
                self._ataque(self.pkm_oponente, self.pkm_player, bot_detalhe)
                if self.pkm_player.estar_vivo():
                    self._ataque(self.pkm_player, self.pkm_oponente, acao_detalhe)
        return True # Caso os dois troquem nada acontece

    def npc(self):
        import random # Sim ele vai ser "burro"
        acao_bot = random.randint(1, 2)
        if not self.trainer:
            acao_bot = 1
        if acao_bot == 1:
            moves = self.pkm_oponente.moves 
            move = random.choice(moves)
            return ("atacar", move)
        else:
            opcoes = [
                pkm for pkm in self.oponente.equipe
                if  pkm.estar_vivo() and pkm != self.pkm_oponente
            ]
            # Caso não tenha opções obriga o bot a atacar
            if not opcoes:
                moves = self.pkm_oponente.moves
                move = random.choice(moves)
                return ("atacar", move)
            pkm_escolhido = random.choice(opcoes)
            self.pkm_oponente = pkm_escolhido
            print(f"\n{self.oponente.nome} recolheu o Pokémon e enviou {self.pkm_oponente.nome}!")
            return ("trocar", None)


# Moves: nome, tipo, contato, dano, alvo, acerto
# Fisícos:
earthquake = Move(nome="Earthquake", tipo="Ground", contato=True, dano=100, alvo="", acerto=100)
waterfall = Move("Waterfall", "Water", True, 80, "", 100)
close_combat = Move("Close Combat", "Fighting", True, 120, "inimigo", 100)
brave_bird = Move("Brave Bird", "Flying", True, 120, "inimigo", 100)
flare_blitz = Move("Flare Blitz", "Fire", True, 120, "inimigo", 100)
stone_edge = Move("Stone Edge", "Rock", True, 100, "inimigo", 80)
ice_punch = Move("Ice Punch", "Ice", True, 75, "inimigo", 100)
water_liquidation = Move("Liquidation", "Water", True, 85, "inimigo", 100)
gunk_shot = Move("Gunk Shot", "Poison", True, 120, "inimigo", 80)
crunch = Move("Crunch", "Dark", True, 80, "inimigo", 100)
outrage = Move("Outrage", "Dragon", True, 120, "inimigo", 100)
iron_head = Move("Iron Head", "Steel", True, 80, "inimigo", 100)
u_turn = Move("U-turn", "Bug", True, 70, "inimigo", 100)
water_shuriken = Move("Water Shuriken", "Water", True, 75, "", 80)
# Especiais:
draco_meteor = Move("Draco Meteor", "Dragon", False, 130, "inimigo", 90)
surf = Move("Surf", "Water", False, 90, "inimigo", 100)
hydro_pump = Move("Hydro Pump", "Water", False, 110, "inimigo", 80)
ice_beam = Move("Ice Beam", "Ice", False, 90, "inimigo", 100)
flamethrower = Move("Flamethrower", "Fire", False, 90, "inimigo", 100)
fire_blast = Move("Fire Blast", "Fire", False, 110, "inimigo", 85)
thunderbolt = Move("Thunderbolt", "Electric", False, 90, "inimigo", 100)
energy_ball = Move("Energy Ball", "Grass", False, 90, "inimigo", 100)
psychic_move = Move("Psychic", "Psychic", False, 90, "inimigo", 100)
shadow_ball = Move("Shadow Ball", "Ghost", False, 80, "inimigo", 100)
sludge_bomb = Move("Sludge Bomb", "Poison", False, 90, "inimigo", 100)
bug_buzz = Move("Bug Buzz", "Bug", False, 90, "inimigo", 100)
flash_cannon = Move("Flash Cannon", "Steel", False, 80, "inimigo", 100)
moonblast = Move("Moonblast", "Fairy", False, 95, "inimigo", 100)
dark_pulse = Move("Dark Pulse", "Dark", False, 80, "inimigo", 100)
air_slash = Move("Air Slash", "Flying", False, 75, "inimigo", 95)
focus_blast = Move("Focus Blast", "Fighting", False, 120, "inimigo", 70)
# --- Moves específicos da equipe da Cynthia ---
dragon_claw = Move("Dragon Claw", "Dragon", True, 80, "inimigo", 100)
brick_break = Move("Brick Break", "Fighting", True, 75, "inimigo", 100)
aqua_jet = Move("Aqua Jet", "Water", True, 40, "inimigo", 100)
silver_wind = Move("Silver Wind", "Bug", False, 60, "inimigo", 100)
aurora_beam = Move("Aurora Beam", "Ice", False, 65, "inimigo", 100)
mirror_coat = Move("Mirror Coat", "Psychic", False, 1, "inimigo", 100) # Placeholder de dano

# --- Pokémon da Cynthia ---
spiritomb = Pokemon(
    poke="Spiritomb", nome="Spiritomb", hp=100, cond="Nenhum", tipo=["Ghost", "Dark"],
    ability="Pressure", moves=[shadow_ball, dark_pulse, psychic_move, silver_wind], item=None,
    stat_hp=50, stat_atk=92, stat_deff=108, stat_spatk=92, stat_spdeff=108, stat_speed=35
)
roserade = Pokemon(
    poke="Roserade", nome="Roserade", hp=100, cond="Nenhum", tipo=["Grass", "Poison"],
    ability="Natural Cure", moves=[energy_ball, sludge_bomb, shadow_ball, extra_sensory := Move("Extrasensory", "Psychic", False, 80, "inimigo", 100)], item=None,
    stat_hp=60, stat_atk=70, stat_deff=65, stat_spatk=125, stat_spdeff=105, stat_speed=90
)
gastrodon = Pokemon(
    poke="Gastrodon", nome="Gastrodon", hp=100, cond="Nenhum", tipo=["Water", "Ground"],
    ability="Sticky Hold", moves=[surf, earthquake, ice_beam, sludge_bomb], item=None,
    stat_hp=111, stat_atk=83, stat_deff=68, stat_spatk=92, stat_spdeff=82, stat_speed=39
)
lucario = Pokemon(
    poke="Lucario", nome="Lucario", hp=100, cond="Nenhum", tipo=["Fighting", "Steel"],
    ability="Inner Focus", moves=[close_combat, iron_head, extreme_speed := Move("Extreme Speed", "Normal", True, 80, "inimigo", 100), stone_edge], item=None,
    stat_hp=70, stat_atk=110, stat_deff=70, stat_spatk=115, stat_spdeff=70, stat_speed=90
)
milotic = Pokemon(
    poke="Milotic", nome="Milotic", hp=100, cond="Nenhum", tipo="Water",
    ability="Marvel Scale", moves=[surf, ice_beam, mirror_coat, aqua_jet], item=None,
    stat_hp=95, stat_atk=60, stat_deff=79, stat_spatk=100, stat_spdeff=125, stat_speed=81
)
garchomp = Pokemon(
    poke="Garchomp", nome="Garchomp", hp=100, cond="Nenhum", tipo=["Dragon", "Ground"],
    ability="Sand Veil", moves=[dragon_claw, earthquake, crunch, brick_break], item=None,
    stat_hp=108, stat_atk=130, stat_deff=95, stat_spatk=80, stat_spdeff=85, stat_speed=102
)

# Meus Pokes:
swampert = Pokemon(
    poke="Swampert", nome="Mumu", hp=100, cond="Nenhum", tipo=["Water", "Ground"],
    ability="Torrent", moves=[earthquake, waterfall, brick_break, ice_punch], item=None,
    stat_hp=100, stat_atk=110, stat_deff=90, stat_spatk=85, stat_spdeff=90, stat_speed=60
)
krookodile = Pokemon(
    poke="Krookodile", nome="Sapato", hp=100, cond="Nenhum", tipo=["Ground", "Dark"],
    ability="Moxie", moves=[earthquake, crunch, stone_edge, close_combat], item=None,
    stat_hp=95, stat_atk=117, stat_deff=80, stat_spatk=65, stat_spdeff=70, stat_speed=92
)
greninja = Pokemon(
    poke="Greninja", nome="Greninja", hp=100, cond="Nenhum", tipo=["Water", "Dark"],
    ability="Torrent", moves=[water_shuriken, u_turn, gunk_shot, ice_punch], item=None,
    stat_hp=72, stat_atk=95, stat_deff=67, stat_spatk=103, stat_spdeff=71, stat_speed=122
)
mewtwo = Pokemon(
    poke="Mewtwo", nome="Mewtwo", hp=100, cond="Nenhum", tipo="Psychic",
    ability="Pressure", moves=[psychic_move, energy_ball, thunderbolt, moonblast], item=None,
    stat_hp=106, stat_atk=110, stat_deff=90, stat_spatk=154, stat_spdeff=90, stat_speed=130
)

# Jogadores:
player = Player(nome="Seed", equipe=[swampert, krookodile, greninja, mewtwo])
cynthia = Player(nome="Cynthia", equipe=[spiritomb, roserade, gastrodon, lucario, milotic, garchomp])

batalha = Batalha(player, cynthia, True)
batalha.comecar_batalha()

# Verifica se o HP ta em % porque parece não estar, e não tem um calculo real de hp(tipo calculando o hp total baseando-se no hp stats)
# Fazer itens funcionais, uma classe complexa já que cada item tem uma função diferente. Primeiro precisa ver se o item é de uso unico ou por turno(leftovers e berries).
# Mega pedras são condições especiais em bool, da pra guardar as informações das megas no item assim seria mais facil do que guardar em um objeto pokemon (recomendo deixar pra depois)
# Itens de status podem ter um str explicando oq fazem e depois usar filtros que procuram por palavras especificas, também tem que modificar e botar em pratica o "alvo"