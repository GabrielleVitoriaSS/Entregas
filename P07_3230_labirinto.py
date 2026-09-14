
import random


def generate_maze(m, n, room=0, wall=1, cheese='.'):

    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y):
        pilha = [(x,y)]
        maze[2 * x + 1][2 * y + 1] = room

        random.shuffle(directions)
        while len(pilha) > 0:
            xp, yp = pilha[-1]
            random.shuffle(directions)

            vizinho = False

            for dx, dy in directions:
                nx, ny = xp + dx, yp + dy
                if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                    maze[2 * xp + 1 + dx][2 * yp + 1 + dy] = room
                    maze[2 * nx + 1][2 * ny + 1] = room
                    pilha.append((nx, ny))
                    vizinho = True
                    break

            if not vizinho:
                pilha.pop()

    # Inicia a DFS no canto superior-esquerdo da grade lógica
    dfs(0, 0)

    # Posiciona o queijo em uma sala aleatória (rejeita paredes)
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))

def labirinto(maze, m, n, queijo = '.'):
    visitados = set()
    pilha = [(0,0)]
    origem = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    p_queijo = None

    while len(pilha) > 0:
        xp, yp = pilha.pop()
        if maze[2*xp+1][2*yp+1] == queijo:
            p_queijo = (xp, yp)
            break
        if (xp, yp) in visitados:
            continue
        visitados.add((xp, yp))
        for dx, dy in directions:
            nx, ny = xp + dx, yp + dy
            if 0 <= nx < m and 0 <= ny < n and maze[2 * xp + 1 + dx][2 * yp + 1 + dy] != 1 and (nx, ny) not in visitados:
                pilha.append((nx, ny))
                origem[(nx, ny)] = (xp, yp)

    if p_queijo is not None:
        caminho = []
        corrente = p_queijo
        while corrente != (0, 0):
            caminho.append(corrente)
            corrente = origem[corrente]
        caminho.append((0, 0))

        for i in range(len(caminho) - 1):
            cx, cy = caminho[i]
            x, y = 2*cx + 1, 2*cy + 1
            if maze[x][y] != queijo:
                maze[x][y] = '|'

            nx, ny = caminho[i+1]
            dx, dy = x + nx - cx, y + ny - cy
            maze[dx][dy] = '|'
        maze[1][1] = '|'
    return maze
 

# Example usage:
if __name__ == '__main__':
    m, n = 10, 14  # Grid size
    random.seed(10110)
    maze = generate_maze(m, n)
    labirinto_maze = labirinto(maze, m, n)
    print_maze(labirinto_maze)



