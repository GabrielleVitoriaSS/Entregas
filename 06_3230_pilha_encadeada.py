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
            raise IndexError("Lista Vazia")
        self._size -= 1
        return self._my_list.pop()

    def topo(self):
        if self.size == 0:
            raise IndexError("Lista Vazia")
        return self._my_list.head.value

    @property
    def size(self):
        return self._size

    def __len__(self):
        return self.size

    def esta_vazia(self):
        return self.size == 0

    def __repr__(self):
        values = []
        current = self._my_list.head
        while current:
            values.append(str(current.value))
            current = current.next
        return f"Pilha Encadeada: [{', '.join(values)}]"

