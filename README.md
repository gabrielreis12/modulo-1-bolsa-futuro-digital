# OBJETIVOS

- Resgatar o valor ASCII do caractere utilizando a função ord().
- Converter o retorno da função ord() para sua representação binária de 7 bits (utilizando um laço for).
- Calcular um bit de paridade com base na quantidade de bits com valor 1 na cadeia de 7 bits (utilizando iteração).
- Devolver uma saída com o nome da pessoa considerando os critérios de paridade escolhidos com base na tabela ASCII.

# MOTIVAÇÃO

- Utilizar conceitos da disciplina de Sistemas Lógicos (ENGC26) para treinar fundamentos da linguagem Python:
  - Fundamentos: tuplas, dicionários, funções com/sem retorno, tratamento de exceção, manipulação de strings, laços de repetição, estruturas condicionais, conversão de tipos e uso de operadores aritméticos, relacionais, de atribuição e lógicos.
- Testar o uso de repositórios para aprimorar o versionamento de código com Git.


# Definição de Paridade:

Em cadeias de bits, a Paridade é utilizada para identificar erros. Portanto, para um protocolo de informações, haverá uma paridade esperada para as cadeias de bits. Ou seja, por exemplo, nessas cadeias de 8 bits:
  - '00100011' 
  - '00110000'

Digamos que o tipo de PARIDADE do primeiro exemplo ('0100011') seja ÍMPAR, nesse caso, o bit de paridade, que sempre vem no início da cadeia de bits, será 0. Caso o tipo de PARIDADE fosse PAR, o bit de paridade seria 1 para que a quantidade de bits da cadeia de 8 bits fosse par.

No segundo exemplo ('00110000'), sendo a paridade PAR, o bit de paridade deve ser 0, do contrário, a paridade seria ÍMPAR e o bit de paridade no início cadeia seria '1', tornando-a: '10110000'.

O tipo de PARIDADE determinada ajuda a indicar que houve algum erro na transmissão da informação. No contexto dos caracteres da tabela ASCII, que são compostos de binários de 7 bits, o bit de paridade será adicionado com um peso a mais que o MSB da cadeia, formando uma cadeia de 8 bits.

Em cenários reais, esse tipo de verificação auxilia como indicativo da confiabilidade da informação transmitida. Esse código é uma maneira de abstrair esse conceito com técnicas de programação, tratamento de erros e aplicação de software para soluções cotidianas.

# FUNCIONALIDADE

- Conversor de caracteres ASCII que mostra como ficará o nome completo em ASCII de acordo com a paridade (determinada pelo número de matrícula):


- Para número de matrícula par: PARIDADE PAR.
- Para número de matrícula ímpar: PARIDADE ÍMPAR.