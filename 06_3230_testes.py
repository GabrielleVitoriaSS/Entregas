import 06_3230_pilha_encadeada as PE 

def main():
    pilha = PE.PilhaEncadeada()

    pilha.push("A")
    pilha.push("B")
    pilha.push("C")
    pilha.push("D")
    pilha.push("E")

    print(pilha.__repr__())
    print("Tamanho da Pilha:", pilha.size)

    print(f"Remove elemento o elemento {pilha.pop()} da pilha")
    print(f"Remove elemento o elemento {pilha.pop()} da pilha")

    if pilha.esta_vazia():
        print("Pilha está vazia")
    else:
        print("Pilha não está vazia")

    print("Tamanho da Pilha:", pilha.size)

    print(f"Remove elemento o elemento {pilha.pop()} da pilha")

def main_2():
    fila = PE.FilaEncadeada()

    fila.enfileirar("A")
    fila.enfileirar("B")
    fila.enfileirar("C")
    fila.enfileirar("D")
    fila.enfileirar("E")

    print("Tamanho da Fila:", fila.__len__())

    print(f"Remove elemento o elemento {fila.desenfileirar()} da fila")
    print(f"Remove elemento o elemento {fila.desenfileirar()} da fila")

    if fila.esta_vazia():
        print("Fila está vazia")
    else:
        print("Fila não está vazia")


if __name__ == "__main__":
    main()
    main_2()






