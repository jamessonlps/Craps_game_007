# Exercício Problema 1 - Design de Software
# Aluno: Jamesson Leandro Paiva Santos
# Turma: B
# Curso: Engenharia de Computação

# Programando uma versão simplificada de um jogo de Craps
# ----------------------------------------------------------------------

# Considerações iniciais

jogo_valendo = True  # Valida quando o jogo irá ou não acabar
fichas_em_maos = 30  # O jogador começa com 30 fichas

# Importando biblioteca random
import random

print('Bem vindo(a) ao grande Cassino James. Se prepare para uma jornada no nosso Craps game e esteja dispoto(a) a apostar suas fichas, hein?')
print('')

print('Você começará esse jogo com 30 fichas, mas tente sair daqui com pelo menos 200 delas, ou vai sair sem nada...')
print('')

print('Muito bem, sem mais delongas, embarque na nossa primeira fase: "COME OUT"!!')
print('')

while jogo_valendo:

    if fichas_em_maos == 0:
        print('Suas fichas acabaram!')
        print('Sentimos muito, mas você perdeu tudo. Agradecemos a sua participação!')
        jogo_valendo = False
    else:
        print('Para ter certeza: quer prosseguir ou desistir? Para continuar, digite "sim"; caso contrário, "não".')
        resposta1 = input()
        print('')

        if resposta1 == 'não':
            print('Tudo bem, agradecemos a sua participação. Volte sempre!')
            jogo_valendo = False
        elif resposta1 == 'sim':
            print('Boa decisão. Começaremos com a 1° fase chamada "Come Out". Você tem quatro escolhas de apostas:')
            print('1. Pass Line Bet - para escolhê-la, digite "line bet"')
            print('2. Field - para escolhê-la, digite "field"')
            print('3. Any Craps - para escolhê-la, digite "craps"')
            print('4. Twelve - para escolhê-la, digite "twelve"')
            print('')
            resposta2 = input('Sua escolha: ')
            print('')
            print('Agora, precisamos que você digite o número de fichas que apostará.')
            aposta_jogador = int(input('Sua aposta: '))
            print('')

                if aposta_jogador > fichas_em_maos:
                    print('Você não tem essa quantidade de fichas. Terá de passar pelo processo inicial novamente.')
                else:
                    
                    if resposta2 == 'twelve':    # Entrando na Twelve
                        print('Você escolheu Twelve. Os dados serão lançados. Se os dados somarem 12, você é sortudo, se não, perde sua aposta')
                        dado_1 = random.randint(1, 6)
                        dado_2 = random.randint(1, 6)
                        soma_dados = dado_1 + dado_2
                        print('')

                        if soma_dados == 12:
                            print('Woooow, você ganhou!!!)
                            fichas_em_maos = fichas_em_maos + 30*aposta_jogador
                            valor_ganho = 30*aposta_jogador
                            print('Você ganhou {0} fichas. Agora, você tem {1} fichas'.format(valor_ganho, fichas_em_maos))
                            print('')
                        else:
                            print('Uma pena, você perdeu sua aposta.')
                            print('')
                            fichas_em_maos = fichas_em_maos - aposta_jogador
                            print('Agora, você tem {0} fichas'.format(fichas_em_maos))
                            print('')
                    
                    elif resposta2 == 'craps':  # Entrando em Any Craps
                        print('Você escolheu Any Craps. Se seus dados somarem 2, 3 ou 12, parabéns. Se não, você perde.')
                        dado_1 = random.randint(1, 6)
                        dado_2 = random.randint(1, 6)
                        soma_dados = dado_1 + dado_2
                        print('')

                        if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
                            print('Woooow, você ganhou!!!)
                            fichas_em_maos = fichas_em_maos + 7*aposta_jogador
                            valor_ganho = 7*aposta_jogador
                            print('Você ganhou {0} fichas. Agora, você tem {1} fichas'.format(valor_ganho, fichas_em_maos))
                            print('')
                        else:
                            print('Uma pena, você perdeu sua aposta.')
                            print('')
                            fichas_em_maos = fichas_em_maos - aposta_jogador
                            print('Agora, você tem {0} fichas'.format(fichas_em_maos))
                            print('')
                    
                    elif resposta2 == 'field':   # Entrando em Field
                        print('Você escolheu Field. Se os dados somarem 5, 6, 7 ou 8, você perde tudo. Se somarem 3, 4, 9, 10 ou 11, você ganha o mesmo valor da aposta.')
                        print('Se tirar 2, ganha o dobro da aposta. E por último, se tirar 12, ganha o tripo!')
                        dado_1 = random.randint(1, 6)
                        dado_2 = random.randint(1, 6)
                        soma_dados = dado_1 + dado_2
                        print('')
                        
                        if soma_dados == 5 or soma_dados == 6 or soma_dados == 7 or soma_dados == 8:
                            print('Uma pena, você perdeu sua aposta')    # Perde a aposta ou perde tudo??