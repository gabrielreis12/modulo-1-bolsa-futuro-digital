# Autor: Gabriel Reis (https://github.com/gabrielreis12)
# Conversor de Caracteres ASCII com paridade a partir do valor de matrícula.

import functions

TRACOS = 70 

while True:

    #IA: validação de como usar len para contar string e nao inteiro

    paridade_matricula = False
    VALORES_PARIDADE = ['PAR', 'ÍMPAR']
    string_paridade = None

    # Apresentação do programa no terminal e solicitação das entradas:

    print(TRACOS*'-')
    print('Codificação em ASCII - Disciplina ENGC26:')
    print(TRACOS*'-')


    # programa acontecendo:

    try:
        # 225601191
        # Gabriel Adriano de Jesus Reis
        nome = input(f'DIGITE O SEU NOME: (se desejar para o programa digite "0") ').strip()
        functions.break_function(nome,1) # passando 1 como parâmetro para poder rodar a função caso seja solicitado o "break" do sistema
        if nome=='0': break
        matricula_raw = input("DIGITE O NÚMERO DA SUA MATRÍCULA (ex.: 225xxyzyz. x,y e z são números inteiros quaisquer): ((se desejar para o programa digite '0') ").strip()
        functions.break_function(nome,matricula_raw) #
        if matricula_raw =='0': break
        matricula = int(matricula_raw)  # conversão dentro do try

        nome = functions.nome_processado(nome)
        matricula = functions.matricula_processada(matricula)

        dados = functions.sensitive_info(nome,matricula)
        
        # definir paridade pelo valor da matrícula
        if (matricula % 2 == 0):
            paridade_matricula = True
            string_paridade = VALORES_PARIDADE[0]
        else:
            paridade_matricula = False
            string_paridade = VALORES_PARIDADE[1]

        nome_tratado = "".join(nome.split())
        lista_de_strings = list(nome_tratado)

        binarios_chr = functions.converter_nome_de_ascii_pra_binario(lista_de_strings)
        resultado = functions.tipo_de_paridade(paridade_matricula, binarios_chr)

        print(f'Olá, {dados["Nome"]}! Matrícula cadastrada: {dados["Matricula"]}.')
        print()
        print(f'Seu nome em binário, tem paridade {string_paridade} pelo valor da sua matrícula: ')
        print()
        for i in range (len(lista_de_strings)):
            print(f'Para a letra {lista_de_strings[i]} com a paridade {string_paridade}, o código é: {resultado[i]}')

    except TypeError as e:
        print(f"\nErro capturado: {e}")
    except ValueError as e:
        print(f"\nErro capturado: {e}")