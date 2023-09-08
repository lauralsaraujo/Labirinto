from queue import deque

class No:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pai = None

class Labirinto:
    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.linhas = len(labirinto)
        self.colunas = len(labirinto[0])
        self.no_inicio = self.encontrar_no(2)
        self.no_fim = self.encontrar_no(3)

    def __getitem__(self, index):
        return self.labirinto[index]

    def encontrar_no(self, valor):
        for x in range(self.linhas):
            for y in range(self.colunas):
                if self.labirinto[x][y] == valor:
                    return No(x, y)
        return None

    def chegou_no_fim(self, x, y):
        return 0 <= x < self.linhas and 0 <= y < self.colunas and self.labirinto[x][y] != 0

    def sucessores(self, no):
        x, y = no.x, no.y
        passos_possiveis = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        passos_validos = []

        for passo_x, passo_y in passos_possiveis:
            if self.chegou_no_fim(passo_x, passo_y):
                passos_validos.append(No(passo_x, passo_y))

        return passos_validos

    def DFS(self):
        pilha = []
        visitados = set()

        pilha.append(self.no_inicio)
        visitados.add((self.no_inicio.x, self.no_inicio.y))

        while pilha:
            no_atual = pilha.pop()

            if no_atual.x == self.no_fim.x and no_atual.y == self.no_fim.y:
                caminho = []
                while no_atual:
                    caminho.insert(0, (no_atual.x, no_atual.y))
                    no_atual = no_atual.pai
                return caminho

            for no_vizinho in self.sucessores(no_atual):
                if (no_vizinho.x, no_vizinho.y) not in visitados:
                    no_vizinho.pai = no_atual
                    pilha.append(no_vizinho)
                    visitados.add((no_vizinho.x, no_vizinho.y))

    def BFS(self):
        fila = deque()
        visitados = set()

        fila.append(self.no_inicio)
        visitados.add((self.no_inicio.x, self.no_inicio.y))

        while fila:
            no_atual = fila.popleft()

            if no_atual.x == self.no_fim.x and no_atual.y == self.no_fim.y:
                caminho = []
                while no_atual:
                    caminho.insert(0, (no_atual.x, no_atual.y))
                    no_atual = no_atual.pai
                return caminho

            for no_vizinho in self.sucessores(no_atual):
                if (no_vizinho.x, no_vizinho.y) not in visitados:
                    no_vizinho.pai = no_atual
                    fila.append(no_vizinho)
                    visitados.add((no_vizinho.x, no_vizinho.y))

    def modificar_labirinto_com_caminho(self, caminho):
        for x, y in caminho:
            if self.labirinto[x][y] == 1:
                self.labirinto[x][y] = 7

    def imprimir_labirinto(self):
        for linha in self.labirinto:
            print(" ".join(map(str, linha)))

def read_labirinto_do_arquivo_txt(arquivo_txt):
    with open(arquivo_txt, 'r') as arquivo:
        lines = arquivo.readlines()

    matrix = [list(map(int, line.strip().split())) for line in lines]

    return matrix

if __name__ == "__main__":

    print("Escolha o labirinto (0-3):")
    numero_do_arquivo = input()
    arquivo_txt = 'labirintos/lab0' + str(numero_do_arquivo) +'.txt' 
    matriz = read_labirinto_do_arquivo_txt(arquivo_txt)

    labirinto = Labirinto(matriz)
    print('\nQual método deseja usar? Digite 1 para DFS e 2 para BFS')
    escolha =input()
    if escolha == 1:
        caminho = labirinto.DFS()
    else:
        caminho = labirinto.BFS()

    labirinto.imprimir_labirinto()
    print("\n\n")
    if caminho:
        labirinto.modificar_labirinto_com_caminho(caminho)
        labirinto.imprimir_labirinto()
        coordenadas_caminho = "Caminho encontrado: "
        for x, y in caminho:
            coordenadas_caminho += f"({x}, {y}) -> "
        coordenadas_caminho = coordenadas_caminho[:-4]
        print("\n", coordenadas_caminho)
    else:
        print("Nenhum caminho encontrado")