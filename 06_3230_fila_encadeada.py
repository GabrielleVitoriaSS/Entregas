# python

import lista_encadeada as myList
import importlib

PE = importlib.import_module("06_3230_pilha_encadeada")

class FilaEncadeada:
    entrada = PE.PilhaEncadeada()
    saida = PE.PilhaEncadeada()

    def enfileirar(self, item):
        return self.entrada.push(item)

    def desenfileirar(self):
        if self.entrada.esta_vazia() and self.saida.esta_vazia():
            raise IndexError("Fila Vazia")
        if self.saida.esta_vazia() == False:
            return self.saida.pop()
        else:
            while self.entrada.esta_vazia() == False:
                self.saida.push(self.entrada.pop())
            return self.saida.pop()
    def frente(self):
        if self.entrada.esta_vazia() and self.saida.esta_vazia():
            raise IndexError("Fila Vazia")
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
        if self.entrada.esta_vazia() and self.saida.esta_vazia():
            return "Fila Vazia"
        fila = []

        temp_saida = PE.PilhaEncadeada()
        temp_entrada = PE.PilhaEncadeada()
        
        while self.saida.esta_vazia() == False:
            elem = self.saida.pop()
            fila.append(str(elem))
            temp_saida.push(elem)

        while temp_saida.esta_vazia() == False:
            self.saida.push(temp_saida.pop())

        while self.entrada.esta_vazia() == False:
            temp_entrada.push(self.entrada.pop())

        while temp_entrada.esta_vazia() == False:
            elem = temp_entrada.pop()
            fila.append(str(elem))
            self.entrada.push(elem)
            
        return f"Fila Encadeada: [{', '.join(fila)}]"

