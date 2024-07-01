from random import randint

cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'azul': '\033[34m',
         'limpa': '\033[m'}

print('JOGO: PAR OU ÍMPAR')

vitorias = 0

while True:
    jogador = int(input('\nDigite um valor de 0 - 10: '))
    escolha = input('Par ou ímpar [P/I]? ').upper().strip()

    comp = randint(0, 9)
    soma = comp + jogador

    print(f'''
Você: {jogador}
Computador: {comp}
    ''')

    if soma % 2 == 0:
        print('A soma deu PAR')
        if escolha == 'P':
            print(f'Você {cores["verde"]}GANHOU{cores["limpa"]}')
            vitorias += 1
        else:
            print(f'Você {cores["vermelho"]}PERDEU{cores["limpa"]}')
            break
    else:
        print('A soma deu ÍMPAR')
        if escolha == 'I':
            print(f'Você {cores["verde"]}GANHOU{cores["limpa"]}')
            vitorias += 1
        else:
            print(f'Você {cores["vermelho"]}PERDEU{cores["limpa"]}')
            break

print('-' * 40)
print(f'''Vitórias consecutivas: {vitorias}

{cores["azul"]}FIM DE JOGO{cores["limpa"]}''')

