from typing import List, NamedTuple, Optional, Set
import random
from enum import Enum

class Coordenada(NamedTuple) :
    linha : int
    coluna : int
    
    def __str__(self):
        tela: str = ""
        for i in range(0, 2):
            tela += str(self.linha) + "," + str(self.coluna) + "\n"
        return tela

class Tipo(str, Enum):
    VAZIO = " "
    PAREDE = "X"
    LARGADA = "I"
    CHEGADA = "F"

class Labirinto:
    def __init__(self, linhas : int = 10, colunas : int = 10, sparseness : float = 0.2, largada : Coordenada = Coordenada(random.randint(0,10),random.randint(0,10)), chegada : Coordenada = Coordenada(random.randint(0,10),random.randint(0,10)) ) :
        self.linhas: int = linhas 
        self.colunas: int = colunas
        self.largada: int = largada 
        self.chegada: int = chegada 
        self.grade:  List[List[Tipo]] = [[Tipo.VAZIO for c in range(colunas)] for r in range(linhas)]
        self.gerador_de_labirinto(linhas, colunas, sparseness)
        self.grade[largada.linha][largada.coluna] = Tipo.LARGADA  
        self.grade[chegada.linha][chegada.coluna] = Tipo.CHEGADA

    def gerador_de_labirinto(self, linhas: int, colunas: int, sparseness: float):
        for linha in range(linhas):
            for coluna in range(colunas):
                if random.uniform(0, 1.0) < sparseness:
                    self.grade[linha][coluna] = Tipo.PAREDE

    def __str__(self) -> str:
        tela: str = ""
        for linha in self.grade:
            tela += "".join([c.value for c in linha]) + "\n"
        return tela
    
    def chegou(self, coordenada: Coordenada) :
        return coordenada == self.chegada

    def sucessores(self, coordenada: Coordenada) :
        possiveis_sucessores: List[Coordenada] = []
        if coordenada.linha + 1 < self.colunas and self.grade[coordenada.coluna + 1][coordenada.coluna] != Tipo.PAREDE:
            possiveis_sucessores.append(Coordenada(coordenada.coluna + 1, coordenada.coluna))
        if coordenada.coluna - 1 >= 0 and self.grade[coordenada.coluna - 1][coordenada.coluna] != Tipo.PAREDE:
            possiveis_sucessores.append(Coordenada(coordenada.coluna - 1, coordenada.coluna))
        if coordenada.coluna + 1 < self.colunas and self.grade[coordenada.coluna][coordenada.coluna + 1] != Tipo.PAREDE:
            possiveis_sucessores.append(Coordenada(coordenada.coluna, coordenada.coluna + 1))
        if coordenada.coluna - 1 >= 0 and self.grade[coordenada.coluna][coordenada.coluna - 1] != Tipo.PAREDE:
            possiveis_sucessores.append(Coordenada(coordenada.coluna, coordenada.coluna - 1))
        return possiveis_sucessores
    
class No:
    def __init__(self, localizacao: Coordenada, pai) :
        self.localizacao: Coordenada = localizacao
        self.pai: Optional[No] = pai

class Pilha(No):
    def __init__(self) :
        self.pilha: List[No] = []

    def pilha_vazia(self) :
        if len(self.pilha) > 0:
            return False
        return True  

    def empilhar(self, objeto: No) :
        self.pilha.append(objeto)

    def desempilhar(self) :
        return self.pilha.pop()  

    def __repr__(self):
        return repr(self.pilha)

def dfs(lab: Labirinto) :
 
    Vetor: List[Coordenada] =[]
    proximo_passo: Pilha[No[Coordenada]] =   Pilha()
    proximo_passo.empilhar(No(lab.largada, None))
    nos_ja_acessados: Set[No] = {lab.largada}
    while not proximo_passo.pilha_vazia() :
        no_atual: No[Coordenada] = proximo_passo.desempilhar()
        localizacao_atual: Coordenada = no_atual.localizacao
        if lab.chegou(localizacao_atual):
            Vetor = no_atual.localizacao
            while no_atual.pai != None:
                Vetor += no_atual.pai.localizacao
            
        for proximo_no in lab.sucessores(localizacao_atual):
            if proximo_no in nos_ja_acessados:
                continue
            nos_ja_acessados.add(proximo_no)
            proximo_passo.empilhar(No(proximo_no, no_atual))
    return Vetor


if __name__ == "__main__":
    lab: Labirinto = Labirinto()
    saida : str = ""
    print(lab)
    #print(lab.largada)
    oi = dfs(lab)
    for i in oi:
        c:  Coordenada = oi
        print(c)