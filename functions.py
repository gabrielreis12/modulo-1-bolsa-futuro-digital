
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

# função que converte um número decimal para binário sem funções nativas do python
def converter_p_binario(num):
    valor_em_binario = []
    contador = num*2
    for i in range(0,7): # considerando que sao apenas 7 bits para codificar em ASCII só serão preenchidos 7 posições [0,1,2,3,4,6,7] ainda será adicionado o bit de paridade
        if contador%2==0:
            valor_em_binario.append('0')
        else:
            valor_em_binario.append('1')
        contador //=2 # decrementando o contador pela sua metade que nem em divisões sucessivas 
    binario = "".join(valor_em_binario)
    return binario #valor do binario como string

def converter_nome_de_ascii_pra_binario(lista_para_binario:list): # funcao que converte valor CARACTERE de ASCII para DECIMAL de ASCII para binario
    letras_em_ascii = []
    for i in range (len(lista_para_binario)):
        valor_em_ascii = ord(lista_para_binario[i]) # convertendo caracteres da lista de strings em ASCII
        valor_em_ascii_convertido_p_binario = converter_p_binario(valor_em_ascii) # de DECIMAL PARA BINÁRIO
        letras_em_ascii.append(valor_em_ascii_convertido_p_binario) # ADICIONANDO CADA ITEM EM BINÁRIO NA LISTA D MANEIRA CRESCENTE
    return letras_em_ascii # retorna em binário cada caractere retirado do nome

def tipo_de_paridade(tipo_de_paridade:bool, lista_para_paridade: list):
    if tipo_de_paridade == True: # significa que é paridade do tipo PAR
        for i in range (len(lista_para_paridade)):
            separar_em_uma_lista_e_contar = lista_para_paridade[i]
            contando_qntd_de_um = separar_em_uma_lista_e_contar.count('1')
            if contando_qntd_de_um%2 == 0:
                lista_para_paridade[i] = '0'+lista_para_paridade[i] # ADICIONA 0 CASO O VALOR JÁ TENHA QNTD. PAR DE BITS
                print(lista_para_paridade[i])
            else:
                lista_para_paridade[i] = '1'+lista_para_paridade[i] # ADICIONA 1 CASO O VALOR TENHA QNTD. ÍMPAR DE BITS
                print(lista_para_paridade[i])
    else:    # significa a paridade é do tipo ÍMPAR
        for i in range (len(lista_para_paridade)):
            separar_em_uma_lista_e_contar = lista_para_paridade[i]
            contando_qntd_de_um = separar_em_uma_lista_e_contar.count('1')
            if contando_qntd_de_um%2 == 0:
                lista_para_paridade[i] = '1'+lista_para_paridade[i] # ADICIONA 1 CASO O VALOR TENHA QNTD. PAR DE BITS
                print(lista_para_paridade[i])
            else:
                lista_para_paridade[i] = '0'+lista_para_paridade[i] # ADICIONA 0 CASO O VALOR TENHA QNTD. ÍMPAR DE BITS
                print(lista_para_paridade[i])
    return lista_para_paridade