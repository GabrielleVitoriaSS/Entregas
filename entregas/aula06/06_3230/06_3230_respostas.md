Questão 1.

push(item) - O(1) porque apenas cria o novo nó e atualiza os ponteiros diretamente, em tempo constante. 
pop() - O(1) porque apenas atualiza o valor da cabeça e retorna o dado da cabeça antiga, em tempo constante.
topo() - O(1) porque apenas acessa o valor da cabeça.
esta_vazia() - O(1) porque apenas verifica o valor de size e o compara com o valor 0.
len() - O(1) porque verifica o valor de size que guarda o valor de um incremento.
repr() - O(N) porque verifica todos os nós no laço while e depois apenas retorna o resultado.


Questão 2.

enfileirar(item) - O(1) porque utiliza o método push da classe PilhaEncadeada que é executada em tempo constante.
desenfileirar() - O(1) no caso amortizado porque a transferencia entre as pilhas de entrada e saída é O(N), mas a remoção posterior ocorre em tempo constante.
frente() - O(1) no caso amortizado porque a transferencia entre as pilhas de entrada e saída é O(N), mas o retorno do valor (caso médio) é constante.
esta_vazia() - O(1) porque apenas verifica o valor de size e o compara com o valor 0.
len() - O(1) porque verifica o valor de size que guarda o valor de um incremento.
repr() - O(N) porque ele verifica todos os nós das duas pilhas e depois monta a representação final.
