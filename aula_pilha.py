# python

import lista_encadeada as myList

class ListaPilha(myList.LinkedList):
    def insert(self, data):
        node = myList.Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        data = self.head.value
        self.head = self.head.next
        return data

class PilhaEncadeada:
    def __init__(self):
        self._size = 0
        self._my_list = ListaPilha()

    def push(self, data):
        self._my_list.insert(data)
        self._size += 1

    def pop(self):
        if self.size == 0:
            raise "Lista Vazia"
        self._size -= 1
        return self._my_list.pop()

    @property
    def size(self):
        return self._size

    def __len__(self):
        return self.size

    def esta_vazia(self):
        return self.size == 0

    def __repr__(self):
        dadi = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next

class FilaEncadeada:
    entrada = PilhaEncadeada()
    saida = PilhaEncadeada()

    def enfileirar(self, item):
        return self.entrada.push(item)

    def desenfileirar(self):
        if self.entrada.esta_vazia() and self.saida.esta_vazia():
            raise "Fila Vazia"
        if self.saida.esta_vazia() == False:
            return self.saida.pop()
        else:
            while self.entrada.esta_vazia() == False:
                self.saida.push(self.entrada.pop())
                return self.saida.pop()
    def frente(self):
        if self.entrada.esta_vazia() and self.saida.esta_vazia():
            raise "Fila Vazia"
        if self.saida.esta_vazia() == False:
            return self.saida.head.value
        else:
            while self.entrada.esta_vazia() == False:
                self.saida.push(self.entrada.pop())
                return self.saida.head.value
    
    def esta_vazia(self):
        return self.entrada.esta_vazia() and self.saida.esta_vazia()

    
    def __len__(self):
        return self.entrada.size + self.saida.size
    
    def __repr__(self):
        if self.entrada.is_empty() and self.saida.is_empty():
            print("Fila Vazia")
        while self.entrada.is_empty() == False:
            self.saida.push(self.entrada.pop())
            return f"{self.saida}"



def main():
    pilha = PilhaEncadeada()

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
    fila = FilaEncadeada()

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



