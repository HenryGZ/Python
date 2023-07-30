from operator import truediv
from re import X
import pygame
pygame.init()

#posição x e y do elemento da tabela
x = 400
y = 300
#pixels que a imagem movimenta a cada comando
velocidade = 7
#imagens 
fundo = pygame.image.load('fundo.jpg')
nave = pygame.image.load('nave.png')
#definir tamanho da janela
janela = pygame.display.set_mode((800,600))
#nome que aparece na janela
pygame.display.set_caption("Jogo 1")

#looping para não fechar a janela
janela_aberta = True
while janela_aberta :
    #atualiza a tela a cada 10 ms
    pygame.time.delay(8)
    #verifica se o evento de fechr a a janela foi acionado
    #se sim ele atualiza a variável bool e fecha o while
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    
        #evento de movimento
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    #atualiza a janela a cada comando
    janela.blit(fundo,(0,0))
    #dentro do while, do corpo do jogo se deve adicionar as coisas
    #criando objeto:
    janela.blit(nave,(x,y))
    pygame.display.update()
pygame.quit()