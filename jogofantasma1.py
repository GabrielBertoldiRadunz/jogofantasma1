import os
import pygame
import random
import time
archive= open("archive.txt","w")
archive.close()
archive= open("archive.txt","a")
nome = input('\n Qual o seu nome? ')
email = input('\n Qual seu email? ')
archive.write(' ' + nome + '\n ' + email)
archive.close()
time.sleep(4)

pygame.init()
icone = pygame.image.load("assets/icon.png")
pygame.display.set_caption("Fuja do Fantasma")
pygame.display.set_icon(icone)
largura = 796
altura = 598
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/fundo.jpg")
crianca = pygame.image.load("assets/crianca.png")
fantasma = pygame.image.load("assets/fantasma.png")
preto = (0, 0, 0)
branco = (255, 255, 255)
def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()
def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf",50)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()
def dead(desvios):
    pygame.mixer.music.stop()
    message_display("Você escapou do fantasma com "+str(desvios)+" desvios")

def escrevendoPlacar(desvios):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios:"+str(desvios), True, branco)
    display.blit(texto, (0, 0))
    
def jogo():
    pygame.mixer.music.load('assets/cacafantasma.mp3')
    pygame.mixer.music.play(-1) 
    criancaPosicaoX = largura * 0.45
    criancaPosicaoY = altura * 0.62
    criancaLargura = 232
    movimentoX = 0
    fantasmaPosicaoX = largura * 0.45
    fantasmaPosicaoY = -220
    fantasmaLargura = 60
    fantasmaAltura = 60
    fantasmaVelocidade = 5

    desvios = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit() 
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                movimentoX = 0

        display.fill(branco)  
        display.blit(fundo, (0, 0)) 
        criancaPosicaoX = criancaPosicaoX + movimentoX
        if criancaPosicaoX < 0:
            criancaPosicaoX = 0
        elif criancaPosicaoX > 680:
            criancaPosicaoX = 680
        display.blit(crianca, (criancaPosicaoX, criancaPosicaoY))
        display.blit(fantasma, (fantasmaPosicaoX, fantasmaPosicaoY))
        fantasmaPosicaoY = fantasmaPosicaoY + fantasmaVelocidade
        if fantasmaPosicaoY > altura:
            fantasmaPosicaoY = -220
            fantasmaVelocidade += 1
            fantasmaPosicaoX = random.randrange(0, largura-50)
            desvios = desvios + 1
        escrevendoPlacar(desvios)
        if criancaPosicaoY < fantasmaPosicaoY + fantasmaAltura:
            if criancaPosicaoX < fantasmaPosicaoX and criancaPosicaoX+criancaLargura > fantasmaPosicaoX or fantasmaPosicaoX+fantasmaLargura > criancaPosicaoX and fantasmaPosicaoX+fantasmaLargura < criancaPosicaoX+criancaLargura:
                dead(desvios)
        pygame.display.update()
        fps.tick(60)
jogo()
print("Volte sempre....")
