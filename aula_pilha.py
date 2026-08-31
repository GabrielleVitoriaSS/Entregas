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

    def is_empty(self):
        return self.size == 0


class FilaEncadeada:
    entrada = PilhaEncadeada()
    saida = PilhaEncadeada()

    def enfileirar(self, item):
        return entrada.push(item)

    def desenfileirar(self):
        if self.entrada.is_empty() and self.saida.is_empty():
            raise "Fila Vazia"
        if self.saida.is_empty() == False:
            return self.saida.pop()
        else:
            while self.entrada.is_empty() == False:
                self.saida.push(self.entrada.pop())
                return self.saida.pop()


def main():
    # Create a new stack
    stack = PilhaEncadeada()

    # Push elements onto the stack
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")
    stack.push("E")

    # Check the size of the stack
    print("Stack size:", stack.size)

    # Pop elements from the stack
    print("Popped item:", stack.pop())
    print("Popped item:", stack.pop())

    # Check if the stack is empty
    if stack.is_empty():
        print("Stack is empty")
    else:
        print("Stack is not empty")

    # Check the size of the stack again
    print("Stack size:", stack.size)

    # Pop elements from the stack
    print("Popped item:", stack.pop())
    # print("Popped item:", stack.pop())


if __name__ == "__main__":
    main()



