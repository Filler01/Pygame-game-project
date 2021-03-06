# debugged: angle, explosion
import pygame, sys, math, time
from pygame.locals import *

pygame.init()

bg = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

ww = pygame.display.Info().current_w
wh = pygame.display.Info().current_h

#pygame.mixer.music.load("engine_1.mp3")
#pygame.mixer.init()

screen = pygame.display.set_mode((ww, wh))#, pygame.FULLSCREEN)
pygame.display.set_caption("MyRace - [Space] to switch day/night")
screen.fill(bg)



night = 1

stretch = []
#stretch.append(pygame.image.load("bla_1.png"))
a = 1
a_counter = 1

while a == 1:    
    try:
        exec("stretch.append(pygame.image.load('track_" + str(a_counter) + ".png'))")
    except:
        a = 0
    a_counter += 1

c_straße = (100, 100, 100, 255)
c_fence  = (255, 5, 5, 255)
c_finish = (255, 255, 5, 255)

counter = 0

player_1 = pygame.Rect(100, 165, 20, 20)
image_1 = pygame.image.load("car_1.png")
player_2 = pygame.Rect(100, 195, 20, 20)
image_2 = pygame.image.load("car_2.png")




explosion = pygame.image.load("explosion.png")

# Variablen: Spieler 1
pressed_1 = "false"
pressed_1_l = "false"
pressed_1_r = "false"
pressed_1_b = "false" # Back - Rückwärts

bew_counter_1 = 0
winkel_1 = 0
destroy_1 = 0
count_destr_1 = 0

# Variablen: Spieler 2
pressed_2 = "false"
pressed_2_l = "false"
pressed_2_r = "false"
pressed_2_b = "false"

bew_counter_2 = 0
winkel_2 = 0
destroy_2 = 0
count_destr_2 = 0

mvsp = 10
winkel_ch = 4 / 8 # change angle

clock = pygame.time.Clock()
fps = 50
time_ = 0

#pygame.mixer.music.play()

##########
x = 1
while x == 1:
    if count_destr_1 == 1:
        player_1.left = 100
        player_1.top = 165

    if count_destr_2 == 1:
        player_2.left = 100
        player_2.top = 195
    #if time == 125: # Sekunden * fps
    #    pygame.mixer.music.play()
    #    time = 0
# Spieler 1
    if count_destr_1 == 0:
        #print(1)
        if pressed_1 == "true" and bew_counter_1 < mvsp:
            bew_counter_1 += 0.25
        if pressed_1_b == "true":
            bew_counter_1 -= 0.25

        if pressed_1_l == "true" and bew_counter_1 > 2:
            #winkel_1 -= winkel_ch
            winkel_1 -= winkel_ch * bew_counter_1
        elif pressed_1_l == "true" and bew_counter_1 < -2:
            winkel_1 -= winkel_ch * bew_counter_1
        
        if pressed_1_r == "true" and bew_counter_1 > 2:
            winkel_1 += winkel_ch * bew_counter_1
        elif pressed_1_r == "true" and bew_counter_1 < -2:
            winkel_1 += winkel_ch * bew_counter_1


        if pressed_1 == "false" and bew_counter_1 > 0:
            bew_counter_1 -= 0.25
        if pressed_1_b == "false" and bew_counter_1 < 0:
            bew_counter_1 += 0.25


        b_1 = math.cos(math.radians(winkel_1)) * bew_counter_1 # Berechnet die Länge der am winkel_1 anliegenden Kathete.
        #fisch.top += b
        #print("b = " + str(b))
        a_1 = math.sin(math.radians(winkel_1)) * bew_counter_1
        player_1.left += round(b_1)
        player_1.top += round(a_1)

        image_1_neu = pygame.transform.rotate(image_1, winkel_1*-1)

    else:
        count_destr_1 -= 1

# Spieler 2
    if count_destr_2 == 0:
        if pressed_2 == "true" and bew_counter_2 < mvsp:
            bew_counter_2 += 0.25
        if pressed_2_b == "true":
            bew_counter_2 -= 0.25

        if pressed_2_l == "true" and bew_counter_2 > 2:
            #winkel_2 -= winkel_ch
            winkel_2 -= winkel_ch * bew_counter_2
        elif pressed_2_l == "true" and bew_counter_2 < -2:
            winkel_2 = winkel_ch * bew_counter_2
        
        if pressed_2_r == "true" and bew_counter_2 > 2:
            winkel_2 += winkel_ch * bew_counter_2
        elif pressed_2_r == "true" and bew_counter_2 < -2:
            winkel_2 += winkel_ch * bew_counter_2


        if pressed_2 == "false" and bew_counter_2 > 0:
            bew_counter_2 -= 0.25
        if pressed_2_b == "false" and bew_counter_2 < 0:
            bew_counter_2 += 0.25    

        b_2 = math.cos(math.radians(winkel_2)) * bew_counter_2 # Berechnet die Länge der am winkel_1 anliegenden Kathete.
        #fisch.top += b
        #print("b = " + str(b))
        a_2 = math.sin(math.radians(winkel_2)) * bew_counter_2
        player_2.left += round(b_2)
        player_2.top += round(a_2)

        image_2_neu = pygame.transform.rotate(image_2, winkel_2*-1)

    else:
        count_destr_2 -=1

    for event in pygame.event.get():
        if event.type == QUIT:
            #pygame.quit()
            x = 0
            #sys.exit()
            

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                x = 0
                
            if event.key == K_RETURN:
                counter += 1
                player_1.left = 100
                player_1.top = 165
                winkel_1 = 0

                player_2.left = 100
                player_2.top = 195
                winkel_2 = 0
                
                if counter >= len(stretch):
                    counter = 0                    

            if event.key == K_SPACE:
                night *= -1
                
                
            if event.key == K_UP:
                pressed_1 = "true"
            if event.key == K_LEFT:
                pressed_1_l = "true"
            if event.key == K_RIGHT:
                pressed_1_r = "true"
            if event.key == K_DOWN:
                pressed_1_b = "true"

            if event.key == K_w:
                pressed_2 = "true"
            if event.key == K_a:
                pressed_2_l = "true"
            if event.key == K_d:
                pressed_2_r = "true"
            if event.key == K_s:
                pressed_2_b = "true"

            #if event.key == K_RETURN:
            #    player_1.left = stp[0]
            #    player_1.top = stp[1]

            #    bew_counter_1 = 0
            #    winkel_1 = 0

        if event.type == KEYUP:
            if event.key == K_UP:
                pressed_1 = "false"
            if event.key == K_LEFT:
                pressed_1_l = "false"
            if event.key == K_RIGHT:
                pressed_1_r = "false"
            if event.key == K_DOWN:
                pressed_1_b = "false"

            if event.key == K_w:
                pressed_2 = "false"
            if event.key == K_a:
                pressed_2_l = "false"
            if event.key == K_d:
                pressed_2_r = "false"
            if event.key == K_s:
                pressed_2_b = "false"

    screen.fill((0, 0, 0))
    screen.blit(stretch[counter], (0, 0))

    if count_destr_1 == 0:
        try:
            if not screen.get_at((player_1.left + 10, player_1.top + 10)) == c_straße:
            #    print(screen.get_at(((player_1.left + 10, player_1.top + 10))))
            #    print("Crash")
                if bew_counter_1 > 3:
                    bew_counter_1 = 2
                if bew_counter_1 < -3:
                    bew_counter_1 = -2
                    #print("Spieler 1\n")

            if screen.get_at((player_1.left + 10, player_1.top + 10)) == c_fence:
                destroy_1 = 1

            if screen.get_at((player_1.left + 10, player_1.top + 10)) == c_finish:
                destroy_1 = 1
                #counter += 1
            
        except:
            destroy_1 = 1

        if destroy_1 == 0:
            screen.blit(image_1_neu, player_1)

    else:
        screen.blit(explosion, player_1)


# Spieler 2 Kollisionserkennung
    if count_destr_2 == 0:
        try:
            if not screen.get_at((player_2.left + 10, player_2.top + 10)) == c_straße:
                if bew_counter_2 > 3: # Erzeugt Ruckel-Effekt
                    bew_counter_2 = 2
                if bew_counter_2 < -3:
                    bew_counter_2 = -2
                    #print("Spieler 2\n")
                    #print(screen.get_at((player_2.left + 10, player_2.top + 10)))

            if screen.get_at((player_2.left + 10, player_2.top + 10)) == c_fence:
                destroy_2 = 1

            if screen.get_at((player_2.left + 10, player_2.top + 10)) == c_finish:
                destroy_2 = 1
                #counter += 1

        except:
            destroy_2 = 1
    
        if destroy_2 == 0:
            screen.blit(image_2_neu, player_2)

    else:
        screen.blit(explosion, player_2)



    if destroy_1 == 1:
        screen.blit(explosion, player_1)
        pygame.display.update()
        destroy_1 = 0
        winkel_1 = 0
        #time.sleep(0.5)
        count_destr_1 = 25
        

    if destroy_2 == 1:
        screen.blit(explosion, player_2)
        pygame.display.update()
        destroy_2 = 0
        winkel_2 = 0
        #time.sleep(0.5)
        count_destr_2 = 25
    
    pygame.display.update()

    #time_ += 1
    clock.tick(fps)

pygame.quit()
#
