def fact(n):
    n = int(input("Z czego silnia wariacie: "))
    m= copy.copy(n)
    wynik = 0
    while m!=0:
        if wynik == 0:
            wynik = n
            m=m-1
        else:
            wynik=wynik*m
            m=m-1
    return wynik

import copy, pygame, sys
pygame.init()
size = width, height = 735,730
screen = pygame.display.set_mode(size)
bg = pygame.image.load("jakasilnia.jpg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(bg, (0,0))
    pygame.display.flip()