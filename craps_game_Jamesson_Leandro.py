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

print('--------------------------------------------------------------------------------------------------------------------------------------')
print('Bem vindo(a) ao grande Cassino James. Se prepare para uma jornada no nosso Craps game e esteja dispoto(a) a apostar suas fichas, hein?')
print('--------------------------------------------------------------------------------------------------------------------------------------')

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
        resposta1 = input('Sua resposta: ')
        print('')

        if resposta1 == 'não':
            print('Tudo bem, agradecemos a sua participação. Volte sempre!')
            jogo_valendo = False
        elif resposta1 == 'sim':
            print('Boa decisão. Começaremos com a 1° fase chamada "Come Out". Você tem quatro escolhas de apostas:')
            print('')
            print('1. Pass Line Bet - para escolhê-la, digite "line bet"')
            print('2. Field - para escolhê-la, digite "field"')
            print('3. Any Craps - para escolhê-la, digite "craps"')
            print('4. Twelve - para escolhê-la, digite "twelve"')
            resposta2 = input('Sua escolha: ')
            print('')
            print('Agora, precisamos que você digite o número de fichas que apostará.')
            aposta_jogador = int(input('Sua aposta: '))
            print('')

            if aposta_jogador > fichas_em_maos:
                print('Você não tem essa quantidade de fichas. Terá de passar pelo processo inicial novamente.')
                print('')
            else:                  
                if resposta2 == 'twelve':    # Entrando na Twelve
                    print('Você escolheu Twelve. Os dados serão lançados. Se os dados somarem 12, você é sortudo, se não, perde sua aposta')
                    dado_1 = random.randint(1, 6)
                    dado_2 = random.randint(1, 6)
                    soma_dados = dado_1 + dado_2
                    print('')

                    if soma_dados == 12:
                        print('Woooow, você ganhou!!! A soma dos dados deu {0}!'.format(soma_dados))
                        print('')
                        fichas_em_maos = fichas_em_maos + 30*aposta_jogador
                        valor_ganho = 30*aposta_jogador
                        print('Você ganhou {0} fichas. Agora, você tem {1} fichas'.format(valor_ganho, fichas_em_maos))
                        print('')
                    else:
                        print('Uma pena, você perdeu sua aposta. A soma dos dados deu {0}!'.format(soma_dados))
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
                        print('Woooow, você ganhou!!! A soma dos dados deu {0}!'.format(soma_dados))
                        print('')
                        fichas_em_maos = fichas_em_maos + 7*aposta_jogador
                        valor_ganho = 7*aposta_jogador
                        print('Você ganhou {0} fichas. Agora, você tem {1} fichas'.format(valor_ganho, fichas_em_maos))
                        print('')
                    else:
                        print('Uma pena, você perdeu sua aposta. A soma dos dados deu {0}!'.format(soma_dados))
                        print('')
                        fichas_em_maos = fichas_em_maos - aposta_jogador
                        print('Agora, você tem {0} fichas'.format(fichas_em_maos))
                        print('')
                
                elif resposta2 == 'field':   # Entrando em Field
                    print('Você escolheu Field. Se os dados somarem 5, 6, 7 ou 8, você perde TUDO. Se somarem 3, 4, 9, 10 ou 11, você ganha o mesmo valor da aposta.')
                    print('Se tirar 2, ganha o dobro da aposta. E por último, se tirar 12, ganha o tripo!')
                    dado_1 = random.randint(1, 6)
                    dado_2 = random.randint(1, 6)
                    soma_dados = dado_1 + dado_2
                    print('')
                    
                    if soma_dados == 5 or soma_dados == 6 or soma_dados == 7 or soma_dados == 8:
                        print('Não foi dessa vez, você perdeu absolutamente tudo! A soma dos dados deu {0}!'.format(soma_dados))
                        print('')
                        fichas_em_maos = 0
                    elif soma_dados == 3 or soma_dados == 4 or soma_dados == 9 or soma_dados == 10 or soma_dados == 11:
                        print('Você ganhou o equivalente à sua aposta! A soma dos dados deu {0}'.format(soma_dados))
                        print('')
                        fichas_em_maos = fichas_em_maos + aposta_jogador
                        print('Você agora tem {0} fichas'.format(fichas_em_maos))
                        print('')
                    elif soma_dados == 2:
                        print('Você ganhou o dobro da sua aposta! A soma dos dados deu 2!')
                        print('')
                        fichas_em_maos = fichas_em_maos + 2*aposta_jogador
                        print('Você agora tem {0} fichas'.format(fichas_em_maos))
                        print('')
                    else:   # Isto é, tira 12
                        print('Você ganhou o triplo da sua aposta! A soma dos dados deu 12!')
                        print('')
                        fichas_em_maos = fichas_em_maos + 3*aposta_jogador
                        print('Você agora tem {0} fichas'.format(fichas_em_maos))
                        print('')
                
                elif resposta2 == 'line bet':
                    print('Você escolheu Pass Line Bet. Se os dados somarem 7 ou 11, você ganha a aposta')
                    print('Se os dados somarem 2, 3 ou 12 - craps - você perde.')
                    print('Se a soma der 4, 5, 6, 8, 9 ou 10, você pulará para a fase "Points".')
                    dado_1 = random.randint(1, 6)
                    dado_2 = random.randint(1, 6)
                    soma_dados = dado_1 + dado_2
                    print('')

                    if soma_dados == 7 or soma_dados == 11:
                        print('Muito bem, você ganhou essa! A soma dos dados deu {0}!'.format(soma_dados))
                        print('')
                        fichas_em_maos = fichas_em_maos + aposta_jogador
                        print('Agora você tem {0} fichas'.format(fichas_em_maos))
                        print('')
                    elif soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
                        print('CRAPS! Você perdeu sua aposta. A soma dos dados deu {0} :('.format(soma_dados))
                        print('')
                        fichas_em_maos = fichas_em_maos - aposta_jogador
                        print('Agora você tem {0} fichas'.format(fichas_em_maos))
                        print('')
                    else:
                        print('Você caiu na 2° fase do jogo! Seja muito bem vindo à fase "Points"!!!')  # Entrada na fase Points
                        print('O último sorteio de dados se tornou o Point.')
                        print('Você poderá escolher as apostas da fase anterior, exceto a Pass Line Bet, ou marcar o Point.')
                        print('No Point, se a nova soma dos dados resultar em 7... Uma pena, terá sido sua última rodada no jogo :(')
                        print('Além disso, você só sairá dessa fase tirando o Point ou o 7... ou perdendo as fichas nas outras apostas.')
                        print('')
                        points_valendo = True
                        Point = soma_dados

                        while points_valendo:            # Aqui inicia o ciclo da fase Points até que o jogador ganhe ou perca no Points ou fique sem fichas nas outras apostas

                            if fichas_em_maos == 0:
                                print('Suas fichas acabaram!')
                                print('Sentimos muito, mas você perdeu tudo. Agradecemos a sua participação!')
                                points_valendo = False
                                jogo_valendo = False
                            else:                                    
                                print('Você deve escolher alguma das três apostas ou ficar jogando "points" até que ganhe sua aposta ou perca tudo.')
                                print('1. Field - para escolhê-la, digite "field"')
                                print('2. Any Craps - para escolhê-la, digite "craps"')
                                print('3. Twelve - para escolhê-la, digite "twelve"')
                                print('4. Digite "points" para tentar marcar o Point')
                                resposta3 = input('Sua escolha: ')
                                print('')
                                dado_1 = random.randint(1, 6)
                                dado_2 = random.randint(1, 6)
                                nova_soma_dados = dado_1 + dado_2

                                if resposta3 == 'field':
                                    print('Você escolheu Field. Vejamos a sua sorte...')
                                    print('')
                                    
                                    if nova_soma_dados == 5 or nova_soma_dados == 6 or nova_soma_dados == 7 or nova_soma_dados == 8:
                                        print('É o fim da linha para você, lamentamos. A soma dos dados deu {0} :('.format(nova_soma_dados))
                                        points_valendo = False
                                        print('')
                                    elif nova_soma_dados == 3 or nova_soma_dados == 4 or nova_soma_dados == 9 or nova_soma_dados == 10 or nova_soma_dados == 11:
                                        print('Parabéns, você ganhou o valor da sua aposta! A soma dos dados deu {0}!'.format(nova_soma_dados))
                                        print('')
                                        fichas_em_maos = fichas_em_maos + aposta_jogador
                                        print('Agora você tem {0} fichas'.format(fichas_em_maos))
                                        print('')
                                    elif nova_soma_dados == 2:
                                        print('Parabéns, você ganhou o dobro da sua aposta! A soma dos dados deu {0}!'.format(nova_soma_dados))
                                        print('')
                                        fichas_em_maos = fichas_em_maos + 2*aposta_jogador
                                        print('Agora você tem {0} fichas'.format(fichas_em_maos))
                                        print('')
                                    elif nova_soma_dados == 12:
                                        print('Bingo! Os dados somaram 12 e você leva o triplo da aposta! A soma dos dados deu {0}!'.format(nova_soma_dados))
                                        print('')
                                        fichas_em_maos = fichas_em_maos + 3*aposta_jogador
                                        print('Agora você tem {0} fichas'.format(fichas_em_maos))
                                        print('')

                                elif resposta3 == 'craps':
                                    print('Você escolheu Any Craps. Se seus dados somarem 2, 3 ou 12, parabéns. Se não, você perde.')
                                    print('')
                                    
                                    if nova_soma_dados == 2 or nova_soma_dados == 3 or nova_soma_dados == 12:
                                        print('Woooow, você ganhou!!! A soma dos dados deu {0}!'.format(nova_soma_dados))
                                        print('')
                                        fichas_em_maos = fichas_em_maos + 7*aposta_jogador
                                        valor_ganho = 7*aposta_jogador
                                        print('Você ganhou {0} fichas. Agora, você tem {1} fichas'.format(valor_ganho, fichas_em_maos))
                                        print('')
                                    else:
                                        print('Uma pena, você perdeu sua aposta. A soma dos dados deu {0}!'.format(nova_soma_dados))
                                        print('')
                                        fichas_em_maos = fichas_em_maos - aposta_jogador
                                        print('Agora, você tem {0} fichas'.format(fichas_em_maos))
                                        print('')

                                elif resposta3 == 'twelve':
                                    print('Você escolheu Twelve. Os dados serão lançados. Se os dados somarem 12, você é sortudo, se não, perde sua aposta')
                                    print('')

                                    if nova_soma_dados == 12:
                                        print('Woooow, você ganhou!!! A soma dos dados deu 12!')
                                        print('')
                                        fichas_em_maos = fichas_em_maos + 30*aposta_jogador
                                        valor_ganho = 30*aposta_jogador
                                        print('Você ganhou {0} fichas. Agora, você tem {1} fichas'.format(valor_ganho, fichas_em_maos))
                                        print('')
                                    else:
                                        print('Uma pena, você perdeu sua aposta. A soma dos dados deu {0}!'.format(nova_soma_dados))
                                        fichas_em_maos = fichas_em_maos - aposta_jogador
                                        print('Agora, você tem {0} fichas'.format(fichas_em_maos))
                                        print('')

                                elif resposta3 == 'points':
                                    print('Você escolheu arriscar sua sorte no Points. Lembre-se: se sair um 7, fim de jogo...')
                                    print('')

                                    if nova_soma_dados == Point:
                                        print('Na mosca, o Point era {0}! Você ganhou a sua aposta e começará uma nova rodada na fase "Come Out".'.format(nova_soma_dados))
                                        print('')
                                        fichas_em_maos = fichas_em_maos + aposta_jogador
                                        print('Agora você tem {0} fichas.'.format(fichas_em_maos))
                                        points_valendo = False
                                        print('')
                                    elif nova_soma_dados == 7:
                                        print('Esse foi o maior azar da sua noite, seus dados somaram 7!')
                                        print('')
                                        fichas_em_maos = 0
                                        points_valendo = False
                                    else:
                                        print('Parece que não deu em nada, você não ganhou nem perdeu... Por enquanto.')
                                        print('')
                                            