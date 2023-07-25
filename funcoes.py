# Trabalhando com funções - def - em Python
# https://www.youtube.com/watch?v=T0j68JbeGJg&list=PLbIBj8vQhvm0ayQsrhEf-7-8JAj-MwmPr&index=19
# Parte 1 - def

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

# Passagem de parametros fora de ordem na chamada da funçao
saudacao(nome='José', msg='Oi')
saudacaoX()
print("saudacaoY:", saudacaoY())

# Parte 2 - def e return

x = input("Digite dois numeros: ")
x = x.split(' ')
x = [float(n) for n in x]

print(x)


def divisao(n1, n2):
    if n2 != 0:
        return n1 / n2
    return


a = divisao
divide = a(x[0], x[1])

print(f"a = {a}\
      \nid(a) = {id(a)}\
      \nid(divisao) = {id(divisao)}\
      \ntipo(a) = {type(a)}\
      \ntipo(divisao) = {type(divisao)}")

if divide:
    print(divide)
else:
    print("Divisão por zero!")


# Parte 3 *args e **kwargs
