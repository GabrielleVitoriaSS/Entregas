Questão 1.

Classe Pessoa
Subclasse herda nome e idade: Funcionario (adiciona salario e carga_horaria)

Classe Funcionario
Subclasses herdam salario, carga_horaria e, pela classe Pessoa, herdam nome e idade: Garçom (adiciona anotar_pedido), Chefe de cozinha (adiciona preparar), Gerente (adiciona demitir)

Classe Restaurante
Subclasse herda nome, endereco e telefone: Pizzaria (adiciona rodizio)

Classe Iguaria
Subclasses herdam nome e preco: Bolo (adiciona formato) e Pizza (adiciona borda_recheada) 

Questão 2. 

Adicionaria um atributo iguarias = list[Iguaria] em Restaurante, para que o restaurante receba instâncias de Iguaria e guarde suas opções de comida. Para manipular essa lista de iguarias, é adequado adicionar o método adicionar_iguaria(iguaria: Iguaria), remover_iguaria(iguaria: Iguaria) e o método de representação __repr__() para mostrar a lista de iguarias do restaurante. 

A relação é modelada como uma Associação com multiplicidade 1: 1..* (a cada uma instância de Restaurante são manipuladas 1 ou mais instâncias de Iguaria).

Questão 3. 

argumento1 - iguaria: Iguaria
O argumento adequado é uma instância da classe Iguaria já que para o método anotar_pedido o garçom necessita do nome e do preco.

argumento2 - iguaria: Iguaria
O argumento adequado é uma instância da classe Iguaria já que para o método preparar o chefe de cozinha necessita dos atributos borda_recheada (para pizza) e formato (para o bolo), além do nome. Como pizza e bolo herdam de Iguaria, podemos aplicar polimorfismo para manipular os atributos das subclasses.

argumento3 - funcionario: Funcionario
É importante identificar, através da classe Funcionario, a Pessoa que se quer demitir, evitando problemas com funcionários com nomes iguais. Por isso, é adequado utilizar uma instância da classe Funcionario como parâmetro do método demitir.