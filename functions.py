
# Este arquivo é  onde realizei os testes da aplicação escapando os possiveis erros de lógica. E onde acabei guardando as funções executadas na "main".

'''
Documentação de erros/entraves:

Primeiro problema: transformar a string em uma lista dos caracteres que compõem a string. Ou seja:
nome = 'Gabriel   Adriano   de   Jesus Reis' se tornar:
Para isso, utilizei:
Método join() e Método split(), a variável nome é dividida de maneira que a ocorrência de um caractere novo os "separa" por uma string vazia.
que é passada como parâmetro do método join() para excluir os espaços.
nome_tratado = "".join(nome.split())
# saída (nome_tratado): GabrielAdrianodeJesusReis
e a variável lista_de_strings utiliza a função list() para transformar toda a string em uma lista de caracteres únicos:
lista_de_strings = list(nome_tratado)
saída (lista_de_)strings: ['G', 'a', 'b', 'r', 'i', 'e', 'l', 'A', 'd', 'r', 'i', 'a', 'n', 'o', 'd', 'e', 'J', 'e', 's', 'u', 's', 'R', 'e', 'i', 's']
'''

# Cabeçalho de funções 

# função que converte um número decimal para binário sem uso de funções nativas do python

def converter_p_binario(num):
    bits = []
    for i in range(6, -1, -1):  # do bit 6 (MSB) até bit 0 (LSB)
        bits.append('1' if (num >> i) & 1 else '0')
    return ''.join(bits)

def converter_nome_de_ascii_pra_binario(lista_para_binario:list): # funcao que converte valor CARACTERE de ASCII para DECIMAL de ASCII para binario
    letras_em_ascii = []
    for i in range (len(lista_para_binario)):
        valor_em_ascii = ord(lista_para_binario[i]) # convertendo caracteres da lista de strings em ASCII-DECIMAL
        valor_em_ascii_convertido_p_binario = converter_p_binario(valor_em_ascii) # Convertendo de ASCII-DECIMAL PARA BINÁRIO
        letras_em_ascii.append(valor_em_ascii_convertido_p_binario) # ADICIONANDO CADA ITEM EM BINÁRIO NA LISTA 
    return letras_em_ascii # retorna em binário todos caracteres resgatados do nome

def matricula_processada(matricula): # tratamento de erros na variável 'matricula' pela função "matricula_processado"
    s_matricula = str(matricula)
    if not isinstance(matricula, int): # deve ser uma variável do tipo inteiro porque a PARIDADE depender do valor da matrícula
        raise TypeError(f"O argumento 'matricula' deve ser um número inteiro (int), mas foi recebido {type(matricula).__name__}")
    if len(s_matricula) < 0: 
        raise ValueError(f'A matrícula não pode ser negativa')
    if len(s_matricula)!=9:
        raise ValueError(f'A matrícula deve ter exatamente 9 dígitos')
    print(f"Matrícula processada: {matricula}!")
    print()
    return matricula

    
def nome_processado(nome: str): # tratamento de erros na variável 'nome' pela função "nome_processado"
    if not isinstance(nome, str):
        raise TypeError(f"O argumento 'nome' deve ser uma string (str), mas foi recebido {type(nome).__name__}")
    nome_counter = nome.strip()
    if (len("".join(nome.split()))<3):
        raise ValueError(f'O nome deve ter pelo menos 3 caracteres')
    print(f"Nome processado! Olá, {nome.upper()}!")
    print()
    return nome

def tipo_de_paridade(tipo_de_paridade:bool, lista_para_paridade: list): # Adicionando os critérios de PARIDADE da CADEIA DE BITS
    if tipo_de_paridade == True: # significa que é paridade do tipo PAR
        for i in range (len(lista_para_paridade)):
            separar_em_uma_lista_e_contar = lista_para_paridade[i]
            contando_qntd_de_um = separar_em_uma_lista_e_contar.count('1') # contando a quantidade de bits com valor 1 em cada caractere da lista_para_paridade
            if contando_qntd_de_um%2 == 0:
                lista_para_paridade[i] = '0'+lista_para_paridade[i] # ADICIONA 0 CASO A CADEIA DE BITS JÁ TENHA QNTD. PAR DE BITS
                
            else:
                lista_para_paridade[i] = '1'+lista_para_paridade[i] # ADICIONA 1 CASO O VALOR TENHA QNTD. ÍMPAR DE BITS
    else:    # significa a paridade é do tipo ÍMPAR
        for i in range (len(lista_para_paridade)):
            separar_em_uma_lista_e_contar = lista_para_paridade[i]
            contando_qntd_de_um = separar_em_uma_lista_e_contar.count('1')
            if contando_qntd_de_um%2 == 0:
                lista_para_paridade[i] = '1'+lista_para_paridade[i] # ADICIONA 1 CASO O VALOR TENHA QNTD. PAR DE BITS
                
            else:
                lista_para_paridade[i] = '0'+lista_para_paridade[i] # ADICIONA 0 CASO O VALOR TENHA QNTD. ÍMPAR DE BITS
    return lista_para_paridade

def sensitive_info(nome,matricula): # Armazenando os dados do usuário numa estrutura de dicionário que armazena a informação numa tupla, considerando que nome completo e matrícula são dados sensíveis.
    dados = (nome,matricula)
    dictionary = {
        "Nome": dados[0], 
        "Matricula": dados[1],
    }
    return dictionary

def break_function(nome,matricula):
    if nome == '0':
        print("Foi bom estar com você... Finalizando o programa!")
    elif matricula == '0':
        print("Foi bom estar com você... Finalizando o programa!")
