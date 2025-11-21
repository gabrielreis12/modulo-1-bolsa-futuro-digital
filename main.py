# Autor: Gabriel Reis (https://github.com/gabrielreis12)
# Conversor de Caracteres ASCII

import functions

TRACOS = 70 

while True:

    #IA: validação de como usar len para contar string e nao inteiro

    paridade_matricula = False
    VALORES_PARIDADE = ['PAR', 'ÍMPAR']
    string_paridade = None
    def matricula_processada(matricula):
        s_matricula = str(matricula)
        if not isinstance(matricula, int):
            raise TypeError(f"O argumento 'matricula' deve ser um número inteiro (int), mas foi recebido {type(matricula).__name__}")
        if len(s_matricula) < 0: 
            raise ValueError(f'A matrícula não pode ser negativa')
        if len(s_matricula)!=9:
            raise ValueError(f'A matrícula deve ter exatamente 9 dígitos')
        print(f"Matrícula processada: {matricula}")
        return matricula

    def nome_processado(nome: str):
        if not isinstance(nome, str):
            raise TypeError(f"O argumento 'nome' deve ser uma string (str), mas foi recebido {type(nome).__name__}")
        nome = nome.strip()
        if (len(nome)<3):
            raise ValueError(f'O nome deve ter pelo menos 3 caracteres')
        print(f"Nome processado! Olá, {nome.upper()}")
        return nome

    # apresentação do programa no terminal e solicitação das entradas:

    print(TRACOS*'-')
    print('Codificação em ASCII - Disciplina ENGC26:')
    print(TRACOS*'-')


    # programa acontecendo:

    try:
        # 225601191
        # Gabriel Adriano de Jesus Reis
        nome = input("DIGITE O SEU NOME: ").strip()
        matricula_raw = input("DIGITE O NÚMERO DA SUA MATRÍCULA (ex.: 225601191): ").strip()
        matricula = int(matricula_raw)  # conversão dentro do try

        matricula_processada(matricula)
        nome = nome_processado(nome)

        # definir paridade pela matrícula
        if (matricula % 2 == 0):
            paridade_matricula = True
            string_paridade = VALORES_PARIDADE[0]
        else:
            paridade_matricula = False
            string_paridade = VALORES_PARIDADE[1]

        nome_tratado = "".join(nome.split())
        lista_de_strings = list(nome_tratado)

        binarios_chr = teste.converter_nome_de_ascii_pra_binario(lista_de_strings)
        resultado = teste.tipo_de_paridade(paridade_matricula, binarios_chr)

        print(f'Seu nome em binário, no formato {string_paridade} é: ')
        for i in range (len(lista_de_strings)):
            print(f'Para a letra {lista_de_strings[i]} com a paridade {string_paridade}, o código é: {resultado[i]}')

    except TypeError as e:
        print(f"\nErro capturado: {e}")
    except ValueError as e:
        print(f"\nErro capturado: {e}")