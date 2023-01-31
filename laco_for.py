"""
FAÇA UM PROGRAMA QUE PEDE O N DE DETALHES DE ESGOTO E PRINT NA TELA A LISTA DE N DETALHES DE ESGOTO
EXEMPLO
N = 3

DE-1
DE-2
DE-3

"""

#sintaxe do laço for e listas e range
    # range >>> range(50, 60, 2)
    # transformar range em lista >>> list(range(n))

    # listas >>> lista_de_coisas = ['coisa1','coisa2','coisa3']

    # for coisa in lista_de_coisas:

# N_DE = int(input('Digite a quantidade de Detalhes de Esgoto:'))
# lista_DE = list(range(N_DE))

# for DE in lista_DE:
#     print('DE-'+ str(DE+1))

# print(lista_DE)

"""
Condicional

if condicao:
    asdf
    asfd
    asdf
    asdf

==  >>> comparação de igualdade
!=  >>> comparação de diferença
or  >>> ou
and >>> e
>   >>> maior que
<   >>> menor que
>=  >>> idem
<=  >>> idem

"""

valor = int(input('Digite um valor: '))

if valor == 0:
    print('Isso é zero')  
else:
    print('Isso é um ' + str(valor))

input()


