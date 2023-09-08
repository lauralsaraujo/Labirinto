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

if __name__ == "__main__":
    matriz = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 3],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
    ]

    labirinto = Labirinto(matriz)
    caminho = labirinto.DFS()
    labirinto.imprimir_labirinto()
    print("\n\n\n")
    if caminho:
        labirinto.modificar_labirinto_com_caminho(caminho)
        labirinto.imprimir_labirinto()
        print("\nCaminho encontrado:")
        for x, y in caminho:
            print(f"({x}, {y})")
    else:
        print("Nenhum caminho encontrado")
