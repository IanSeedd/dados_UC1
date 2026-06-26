TIPOS = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", 
         "Bug", "Rock", "Ghost", "Dragon", "Steel", "Dark", "Fairy"]
def validar_tipo(tipo):
    if tipo not in TIPOS:
        raise ValueError(f"Tipo inválido: '{tipo}'. Escolha um de: {TIPOS}")
    return tipo
# Validador de tipos, tem que estar a lista e ter no maximo 2 tipos, usando isintance para ser elegante. Além disso ele valida a lista denovo.
def validar_quant_tipos(tipos):
    # Se vier só 1 tipo (string) + já transforma em lista
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
    def __init__(self, nome, tipo, contato, dano, alvo): # Por equanto apenas moves de dano porque eu to com preguiça
        self.nome = nome
        self.tipo = validar_tipo(tipo)
        self.contato = contato
        self.dano = dano
        self.alvo = alvo

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
    
class Batalha:
    def __init__(self, jogador, oponente, trainer=False):
        self.jogador = jogador
        self.oponente = oponente # Treinador ou Pokemon singular
        self.trainer = trainer # Se for True tem time
        # Define o Pokémon do jogador (busca o primeiro vivo)
        self.pkm_player = self._obter_primeiro_vivo(jogador.equipe)
        if self.pkm_player is None:
            raise ValueError(f"O jogador {jogador.nome} não tem nenhum Pokémon vivo para batalhar!") 

        # Define o Pokémon do oponente
        if self.oponente.equipe:
            self.pkm_oponente = self._obter_primeiro_vivo(oponente.equipe)
            if self.pkm_oponente is None:
                raise ValueError(f"O oponente {oponente.nome} não tem nenhum Pokémon vivo para batalhar!") # Só para garantir que não vai dar um erro
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
        
