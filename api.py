import pygame
from sys import exit
from random import randint, choice

#class for the main character
class Puma(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        puma_walk1 = pygame.image.load('graphics/puma_walk1.png').convert_alpha()
        puma_walk2 = pygame.image.load('graphics/puma_walk2.png').convert_alpha()
        self.puma_walk = [puma_walk1, puma_walk2]
        self.puma_jump = pygame.image.load('graphics/puma_jump.png').convert_alpha()
        self.puma_index = 0


        self.image = self.puma_walk[self.puma_index]
        self.rect = self.image.get_rect(midbottom = (200,300))
        self.grav = 0


        self.jump_sound = pygame.mixer.Sound('graphics/audio_jump.mp3')
        self.jump_sound.set_volume(0.05)
    def puma_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.grav = -22
            self.jump_sound.play()
    def gravidade(self): #gravity
        self.grav += 1
        self.rect.y += self.grav
        if self.rect.bottom >= 300: self.rect.bottom = 300
   
    def animacao(self): #animation
        if self.rect.bottom < 300: self.image = self.puma_jump
        else: self.puma_index += 0.1
        if self.puma_index >= len(self.puma_walk): self.puma_index = 0
        self.image = self.puma_walk[int(self.puma_index)]


    def update(self):
        self.puma_input()
        self.gravidade()
        self.animacao()

#class for the enemies
class Gatos(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
       
        if type == 'tigre': #tigre is one of the enemies
            tigre_frame1 = pygame.image.load('graphics/tigre_walk1.png').convert_alpha()
            tigre_frame2 = pygame.image.load('graphics/tigre_walk2.png').convert_alpha()
            self.frames = [tigre_frame1, tigre_frame2]
            y_pos = 210
        else: #kika is the other enemy. if you have more enemies, you can create more elifs
            kika_frame1 = pygame.image.load('graphics/kika_walk1.png').convert_alpha()
            kika_frame2 = pygame.image.load('graphics/kika_walk2.png').convert_alpha()
            self.frames = [kika_frame1, kika_frame2]
            y_pos = 300
       
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))


    def animacao(self): #animation
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]


    def update(self):
        self.animacao()
        self.rect.x -= 6
        self.apagar()


    def apagar(self): #delete the enemy when it leaves the screen
        if self.rect.x <= -100:
            self.kill()


def gatos_mov(gatos_list) : #function to move the enemies
    if gatos_list:
        for gatos_rect in gatos_list:
            gatos_rect.x -= 5


            if gatos_rect.bottom == 300: screen.blit(kika_surface, gatos_rect)
            else: screen.blit(tigre_surf, gatos_rect)
               
        gatos_list = [gatos for gatos in gatos_list if gatos.x > -100]
        return gatos_list
   
    else: return []
def pontuacao(): #function to calculate the score
    tempo = int(pygame.time.get_ticks()/1000) - tempo_inicial
    pontos_surf = test_font.render(f'Pontos: {tempo}', False, ('white'))
    pontos_rect = pontos_surf.get_rect(center = (400,50))
    screen.blit(pontos_surf, pontos_rect)
    return tempo
def animacao_puma(): #function to animate the main character
    global puma_surf, puma_index


    if puma_rect.bottom < 300:
        puma_surf = puma_jump
    else:
        puma_index += 0.1
        if puma_index >= len(puma_walk): puma_index = 0
        puma_surf = puma_walk[int(puma_index)]
def colisao(puma, gatos): #function to check if the main character collided with an enemy
    if gatos:
        for gatos_rect in gatos:
            if puma.colliderect(gatos_rect): return False
    return True
def colisao_sprite(): #function to check if the main character collided with an enemy
    if pygame.sprite.spritecollide(puma.sprite,gatos_group,False):
        gatos_group.empty()
        return False
    else: return True

#initializing the game, adding music, score, characters, enemies, and the background
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('STARPuma')
clock = pygame.time.Clock()
test_font = pygame.font.Font('graphics/Pixeltype.ttf', 50)
game_act = True
tempo_inicial = 0
pontos = 0
musica = pygame.mixer.Sound('graphics/music.wav')
musica.play()
musica.set_volume(0.1)
puma = pygame.sprite.GroupSingle()
puma.add(Puma())

#creating the enemies
gatos_group = pygame.sprite.Group()


sky_surface = pygame.image.load('graphics/Sky1.jpg').convert()
ground = pygame.image.load('graphics/ground1.jpg').convert()


pontos_surf = test_font.render('STARPuma', False, (64,64,64))
pontos_rect = pontos_surf.get_rect(center = (400, 50))


kika_frame1 = pygame.image.load('graphics/kika_walk1.png').convert_alpha()
kika_frame2 = pygame.image.load('graphics/kika_walk2.png').convert_alpha()
kika_frames = [kika_frame1, kika_frame2]
kika_frame_index = 0
kika_surface = kika_frames[kika_frame_index]




tigre_frame1 = pygame.image.load('graphics/tigre_walk1.png').convert_alpha()
tigre_frame2 = pygame.image.load('graphics/tigre_walk2.png').convert_alpha()
tigre_frames = [tigre_frame1, tigre_frame2]
tigre_frame_index = 0
tigre_surf = tigre_frames[tigre_frame_index]
gatos_rect_list = []


puma_walk1 = pygame.image.load('graphics/puma_walk1.png').convert_alpha()
puma_walk2 = pygame.image.load('graphics/puma_walk2.png').convert_alpha()
puma_walk = [puma_walk1, puma_walk2]
puma_jump = pygame.image.load('graphics/puma_jump.png').convert_alpha()
puma_index = 0


puma_surf = puma_walk[puma_index]
puma_rect = puma_surf.get_rect(midbottom = (80,300))
puma_grav = 0


puma_stand = pygame.image.load('graphics/puma_jump.png').convert_alpha()
puma_stand_rect = puma_stand.get_rect(center = (400,200))


gatos_timer = pygame.USEREVENT + 1
pygame.time.set_timer(gatos_timer, 1500)


kika_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(kika_animation_timer, 500)
tigre_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(tigre_animation_timer, 200)


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_act:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if puma_rect.collidepoint(event.pos) and puma_rect.bottom >=300:
                    puma_grav = -22  




            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and puma_rect.bottom >=300:
                    puma_grav = -22
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_act = True
                tempo_inicial = int(pygame.time.get_ticks()/1000)
        if game_act:
            if event.type == gatos_timer:
                gatos_group.add(Gatos(choice(['tigre', 'tigre', 'kika', 'kika'])))


            if event.type == kika_animation_timer:
                if kika_frame_index == 0: kika_frame_index = 1
            else: kika_frame_index = 0
            kika_surface = kika_frames[kika_frame_index]


            if event.type == tigre_animation_timer:
                if tigre_frame_index == 0: fly_frame_index = 1
            else: fly_frame_index = 0
            tigre_surf = tigre_frames[tigre_frame_index]
    if game_act:
        screen.blit(ground, (0,300))
        screen.blit(sky_surface, (0,0))


        pontos = pontuacao()
       
        pygame.draw.rect(screen, '#23395d', pontos_rect)
        pontuacao()


        #puma


        puma.draw(screen)
        puma.update()
        gatos_group.draw(screen)
        gatos_group.update()
        game_act = colisao_sprite()
    else:
        screen.fill('#152238')
        screen.blit(puma_stand, puma_stand_rect)
        gatos_rect_list.clear()
        puma_rect.midbottom = (80,300)
        puma_grav = 0


        pontos_texto = test_font.render(f'Pontos: {pontos}', False, ('white'))
        pontos_texto_rect = pontos_texto.get_rect(center = (400, 330))
        screen.blit(pontos_texto, pontos_texto_rect)
        game_texto = test_font.render('Clica para recomecar', False, ('white'))
        game_texto_rect = game_texto.get_rect(center = (400, 90))
        screen.blit(game_texto, game_texto_rect)
       
    pygame.display.update()
    clock.tick(60)