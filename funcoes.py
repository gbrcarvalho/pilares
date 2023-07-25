# Trabalhando com funções - def - em Python
# https://www.youtube.com/watch?v=T0j68JbeGJg&list=PLbIBj8vQhvm0ayQsrhEf-7-8JAj-MwmPr&index=19

# Passagem de parametros
def mensagem(msg):
    print('mensagem:', msg)


# Parametros default
def saudacao(msg='Olá', nome='Gabriel'):
    print(msg, nome)


def saudacaoX(msg='Olá', nome='Gabriel'):
    nome = nome.lower()
    nome = nome.replace('a', '4')
    nome = nome.replace('e', '3')
    nome = nome.replace('i', '1')
    nome = nome.replace('o', '0')
    nome = nome.replace('g', '6')
    nome = nome.replace('s', '5')
    nome = nome.replace('t', '7')
    print(msg, nome)


# Retornando Valor
def saudacaoY(msg='Olá', nome='Gabriel'):
    nome = nome.lower()
    nome = nome.replace('a', '4')
    nome = nome.replace('e', '3')
    nome = nome.replace('i', '1')
    nome = nome.replace('o', '0')
    nome = nome.replace('g', '6')
    nome = nome.replace('s', '5')
    nome = nome.replace('t', '7')
    return f'{msg} {nome}'


mensagem('Executando a função mensagem')
saudacao()
saudacao(nome='José', msg='Oi')
saudacaoX()
print(saudacaoY())
