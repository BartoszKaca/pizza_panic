import pygame, sys
import random

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
#opis okna
pygame.display.set_caption('pizza panic - K.Pietrasik')
#wymiary okna
screen = pygame.display.set_mode((1280,720))
#muzyka
theme = pygame.mixer.music.load("assets/theme.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(1)
#czcionki
font = pygame.font.SysFont(None, 20)
title = pygame.font.SysFont(None, 60,True)

#wypisywanie tekstu
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False
#klasa sera
class Cheese(pygame.sprite.Sprite):
    def __init__(self, x, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/pizza.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y =100
        self.speed = speed
    def update(self):
        #spadanie
        self.rect.center = [self.x, self.y]
        self.y+=self.speed
#klasa Pizzy
class Pizza(pygame.sprite.Sprite):
    def __init__(self, x, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/pizza1.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y =100
        self.speed = speed
    def update(self):
        self.rect.center = [self.x, self.y]
        self.y+= 1
#klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, steering):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/kucharz1.png')
        self.rect = self.image.get_rect()
        self.text = steering
        self.x = 680
        self.y = 680
    def update(self):
        #sterowanie myszka
        if self.text == 1:
            self.x,y =pygame.mouse.get_pos()
            self.rect.center = [self.x, self.y]
        #sterowanie klawiatura
        if self.text == 0:
            pygame.key.set_repeat(1,2)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.time.wait(1000)
                        main_menu()
                    if event.key == K_RIGHT:
                        if self.x <1260:
                            self.x += 2
                    if event.key == K_LEFT:
                        if self.x > 20:
                            self.x -=2
            self.rect.center = [self.x, self.y]
#menu glowne
def main_menu():
    click = False
    screen.fill((0, 0, 0))
    bg = pygame.image.load('assets/background.jpg')
    while True:
        screen.blit(bg, (0,0))
        draw_text('Menu Główne', title, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(450, 300, 250, 200)
        mute = pygame.Rect(1000, 500, 200, 200)
        if mute.collidepoint((mx, my)):
            if click:
                if pygame.mixer.music.get_volume() == 1.0:
                    pygame.mixer.music.set_volume(0)
                else:
                    pygame.mixer.music.set_volume(1)
        m1 = pygame.image.load('assets/mute.png')
        screen.blit(m1, (1000, 500))
        button_1 = pygame.Rect(100, 300, 250, 200)
        button_2 = pygame.Rect(900, 300, 250, 200)
        if button_1.collidepoint((mx, my)):
            if click:
                steering_chose()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        b1 = pygame.image.load('assets/start.png')
        b2 = pygame.image.load('assets/exit.png')
        screen.blit(b1, (100, 300))
        screen.blit(b2, (900, 300))
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
#menu pośmiertne
def death_menu(poziom):
    click = False
    x = pygame.mixer.music.get_pos()
    pygame.mixer.music.load("assets/dead.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.queue('assets/theme.mp3', loops= -1)
    screen.fill((0, 0, 0))
    bg = pygame.image.load('assets/background.jpg')
    while True:
        screen.blit(bg, (0,0))
        draw_text('Zginąłeś :(', title, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(450, 300, 250, 200)
        mute = pygame.Rect(1000, 500, 200, 200)
        if mute.collidepoint((mx, my)):
            if click:
                if pygame.mixer.music.get_volume() == 1.0:
                    pygame.mixer.music.set_volume(0)
                else:
                    pygame.mixer.music.set_volume(1)
        m1 = pygame.image.load('assets/mute.png')
        screen.blit(m1, (1000, 500))
        button_1 = pygame.Rect(100, 300, 250, 200)
        button_2 = pygame.Rect(900, 300, 250, 200)
        if button_1.collidepoint((mx, my)):
            if click:
                steering_chose()
        if button_2.collidepoint((mx, my)):
            if click:
                main_menu()
        b1 = pygame.image.load('assets/start.png')
        b2 = pygame.image.load('assets/exit.png')
        screen.blit(b1, (100, 300))
        screen.blit(b2, (900, 300))
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
#główna pętla gry
def game(steering):
    running = True
    score = 0
    poziom = 1
    x = 0
    player = Player(steering)
    player_group = pygame.sprite.Group()
    player_group.add(player)
    pizza_group = pygame.sprite.Group()
    cheese_group = pygame.sprite.Group()
    screen.fill((0, 0, 0))
    wall = pygame.image.load('assets/wall.jpg')
    while running:
        screen.blit(wall, (0, 0))
        pizza_group.update()
        pizza_group.draw(screen)
        cheese_group.update()
        cheese_group.draw(screen)
        player_group.update()
        player_group.draw(screen)
        if poziom == 5:
            running = False
            win()
        #sprawdzanie trafienia
        for sprite in cheese_group.sprites():
            if sprite.y > 700:
                sprite.kill()
            if sprite.y > 600 and sprite.x - player.x <50 and sprite.x - player.x > -50:
                death_menu(poziom)
        for sprite in pizza_group.sprites():
            if sprite.y > 700:
                death_menu(poziom)
            if sprite.y > 600 and sprite.x - player.x <50 and sprite.x - player.x > -50:
                sprite.kill()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    main_menu()
        if x <= 0:
            if random.randrange(0,2):
                pizza = Pizza(random.randrange(20,1250), poziom)
                pizza_group.add(pizza)
            else:
                cheese = Cheese(random.randrange(20,1250), poziom)
                cheese_group.add(cheese)
            x = 120
            print(poziom)
        else:
            score+=1
            x-= poziom
        poziom = int(score/1000) +1
        draw_text('Poziom: '+str(poziom), title, (255, 255, 255), screen, 70, 110)
        pygame.display.update()
        mainClock.tick(60)

#wybór sterowania
def steering_chose():
    click = False
    screen.fill((0, 0, 0))
    bg = pygame.image.load('assets/background.jpg')
    while True:
        screen.blit(bg, (0,0))
        draw_text('Wybierz sterowanie:', title, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(450, 300, 250, 200)
        mute = pygame.Rect(1000, 500, 200, 200)
        if mute.collidepoint((mx, my)):
            if click:
                if pygame.mixer.music.get_volume() == 1.0:
                    pygame.mixer.music.set_volume(0)
                else:
                    pygame.mixer.music.set_volume(1)
        m1 = pygame.image.load('assets/mute.png')
        screen.blit(m1, (1000, 500))
        button_1 = pygame.Rect(100, 300, 250, 200)
        button_2 = pygame.Rect(900, 300, 250, 200)
        if button_1.collidepoint((mx, my)):
            if click:
                game(0)
        if button_2.collidepoint((mx, my)):
            if click:
                game(1)
        b1 = pygame.image.load('assets/klawiatura.png')
        b2 = pygame.image.load('assets/mysz.png')
        screen.blit(b1, (100,300))
        screen.blit(b2, (900,300))
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
#ekran zwycięstwa
def win():
    click = False
    screen.fill((0, 0, 0))
    bg = pygame.image.load('assets/background.jpg')
    while True:
        screen.blit(bg, (0, 0))
        draw_text('Gratulacje! Wygrałeś!', title, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(450, 300, 250, 200)
        mute = pygame.Rect(1000, 500, 200, 200)
        if mute.collidepoint((mx, my)):
            if click:
                if pygame.mixer.music.get_volume() == 1.0:
                    pygame.mixer.music.set_volume(0)
                else:
                    pygame.mixer.music.set_volume(1)
        m1 = pygame.image.load('assets/mute.png')
        screen.blit(m1,(1000,500))
        if button_1.collidepoint((mx, my)):
            if click:
                main_menu()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        b1 = pygame.image.load('assets/exit.png')
        screen.blit(b1, (450, 300))
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
main_menu()
