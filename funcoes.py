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


def func(a1, a2, a3):
    return 2*a1, 2*a2, 2*a3


v = func(5, 7, 8)
print(v)

# Parte 3 *args e **kwargs


def f1(*args):
    size = len(args)
    for n in range(0, size):
        print(f"{n}: {args[n]}")


def f2(*args, **kwargs):
    print(args)
    print(kwargs)

    idade = kwargs.get('idade')

    if idade:
        print(idade)


# Os args ficam empacotados em uma tupla
# Os kwargs ficam empacotados em um dicionario


f1(1, 'h', 2.6, 'dois ponto seis', (1, 2))

lista = [1, 2, 3, 4, 5]

# Desempacotando uma lista
n1, n2, *n = lista

print(*lista)
print(n1, n2, n)

f2(1, 2, 3, 4, nome='Gabriel', sobrenome='Silva', idade='27')
