#bibliotecas
from time import sleep
import emoji
import pygame
import os
import threading


# Definição de cores para facilitar a leitura do código
cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_azul = "\033[94m"
cor_reset = "\033[0m"
overline = "\u0332"

    # Função para limpar o terminal
def limpar_terminal():
    os.system('cls')


    # Função para tocar música
def tocar_musica(arquivo, duracao=None):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.event.wait()


    # Função para tocar música em uma thread separada
def tocar_musica_thread(arquivo, duracao=None):
    thread_musica = threading.Thread(target=tocar_musica, args=(arquivo, duracao))
    thread_musica.start()


# Lista de arquivos de áudio
file_alternativa1 = r'c:\Users\06569212184\Desktop\sucesso.mp3'
file_alternativa2 = r'c:\Users\06569212184\Desktop\falha.mp3'
file_alternativa3 = r'c:\Users\06569212184\Downloads\Ghost_fantasma.mp3'
file_alternativa4 = r'c:\Users\06569212184\Downloads\Trilha_sonora.mp3'


# Função para perguntar ao jogador se deseja jogar novamente
def jogar_novamente():
    resposta = input("Quer jogar novamente? (s/n): ").lower().strip()[0]
    return resposta == 's'


# Loop principal do jogo
while True:
    limpar_terminal()
    tocar_musica_thread(file_alternativa4, duracao=21)  # Ajuste a duração conforme necessário
    sleep(2)
    print('Este jogo foi desenvolvido por Michell')
    sleep(2)
    print('')
    print('')
    print('')
    print('Carregando...')
    sleep(3)
    print('')
    print('')
    print(emoji.emojize('você acordou tarde :disappointed_face: e se não acelerar voce irá se atrasar!'))
    print('')
    sleep(2)
    print('em direção ao trabalho, dirigindo seu carro, você encontra três caminhos diferentes!')
    print('')
    sleep(2)
    print(f'você tem três opções: seguir em {cor_vermelha}frente, {cor_reset}virar à {cor_verde}direita{cor_reset} ou virar à {cor_azul}esquerda{cor_reset}')
    print('')
    sleep(2)
    print(emoji.emojize(':right_arrow:  seguindo em frente é o caminho mais curto para chegar ao seu trabalho, mas talvez,\n'
                      'você não seja a única pessoa que saiba disso.'))
    print('')
    sleep(3)
    print(emoji.emojize(':right_arrow:  indo pela direita é o caminho mais longo de todos, mas as pessoas normalmente evitam ir por este caminho\n'
                      '(dizem que esta rota é amaldiçoada) :ghost:'))
    print('')
    sleep(3)
    print(emoji.emojize(':right_arrow:  o caminho da esquerda é uma incógnita'))
    print('')
    sleep(3)
    print('sabendo disso, decida!')
    print('')
    sleep(1)
    d1 = int(input(f'Digite 1 para ir à {cor_verde}direita{cor_reset}, 2 para seguir em {cor_vermelha}frente{cor_reset} ou 3 para virar à {cor_azul}esquerda{cor_reset}: '))
    print('processando...')
    sleep(2)
    if d1 == 1:
        print('')
        print(emoji.emojize('        :vertical_traffic_light:'))
        print(overline * 43)
        print(emoji.emojize('-----:ghost:---:racing_car: ---------------------'))
        print(overline * 43)
        tocar_musica_thread(file_alternativa3)
        sleep(1)
        print('')
        print('carregando...')
        sleep(4)
        print('')
        print(emoji.emojize('virando a direita, você viu um fantasma, mas  conseguiu chegar ao seu trabalho a tempo!'))
    elif d1 == 2:
        print('')
        print(emoji.emojize('        :vertical_traffic_light:'))
        print(overline * 47)
        print(emoji.emojize('-:racing_car:--:racing_car:--:racing_car:--:racing_car:--:racing_car: --:racing_car:--:racing_car:--:racing_car:--:racing_car:--:racing_car:--:racing_car:--:racing_car:--:racing_car:--:racing_car:--:racing_car:-'))
        print(overline * 47)
        tocar_musica_thread(file_alternativa2)
        sleep(1)
        print('')
        print('carregando...')
        sleep(4)
        print('')
        print(emoji.emojize('seguindo em frente infelizmente você pegou trânsito! :sad_but_relieved_face:'))
        print('você acabou chegando atrasado e tomando bronca!')
    else:
        print('')
        print(emoji.emojize('        :vertical_traffic_light:'))
        print(overline * 47)
        print(emoji.emojize('---------:racing_car: -----------------------------------'))
        print(overline * 47)
        tocar_musica_thread(file_alternativa1)
        sleep(1)
        print('')
        print('carregando...')
        sleep(4)
        print('')
        print(emoji.emojize('virando a esquerda você conseguiu chegar ao seu trabalho a tempo!'))

    print("-=" * 27, 'fim', "-=" * 27)

    if not jogar_novamente():
        break
    else:
        sleep(1)
