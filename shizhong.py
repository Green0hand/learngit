import pygame
from pygame.locals import *
import time
from pygame.color import THECOLORS
import math

#print(clock)
#Get current time
pygame.init()
SCREEN_LENGTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT), 0, 32)
screen.fill((255, 255, 255))
r_color = [0, 0, 255]
h_color = THECOLORS['green']
m_color = THECOLORS['yellow']
s_color = THECOLORS['red']
r_center = [int(SCREEN_LENGTH/2), int(SCREEN_HEIGHT/2)]
r_radius = int(SCREEN_HEIGHT/2)
m_length = int((SCREEN_HEIGHT/2)*0.9)
s_length = int((SCREEN_HEIGHT/2)*0.85)
h_length = int((SCREEN_HEIGHT/2)*0.6)

tw_pos = [r_center[0], r_center[1] - SCREEN_HEIGHT/2 + 3]
th_pos = [r_center[0] + SCREEN_HEIGHT/2 - 3, r_center[1]]
si_pos = [r_center[0], r_center[1] + SCREEN_HEIGHT/2 - 3]
ni_pos = [r_center[0] - SCREEN_LENGTH/2 + 3, r_center[1]]

non_fill = 1
fill = 0
def refresh():
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, r_color, r_center, r_radius, non_fill)
    pygame.draw.circle(screen, r_color, r_center, 4, fill)
    font_size = 5
    font_color = THECOLORS['black']
    font = pygame.font.SysFont('Courier', font_size)

    tw_text = font.render('12', 15, font_color)
    th_text = font.render('3', 15, font_color)
    si_text = font.render('6', 15, font_color)
    ni_text = font.render('9', 15, font_color)

    screen.blit(tw_text, tw_pos)
    screen.blit(th_text, th_pos)
    screen.blit(si_text, si_pos)
    screen.blit(ni_text, ni_pos)

def point(start_point, l_length, theta):
    end_point = [0, 0]
    end_point[0] = int(start_point[0] + float(l_length*math.sin(theta)))
    end_point[1] = int(start_point[1] + float(l_length*math.cos(theta)))
    return end_point

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    refresh()
    now = time.ctime()
    clock = now[11:19]
    hour = float(now[11:13])
    if hour > 12:
        hour = hour - 12

    minute = float(now[14:16])
    second = float(now[17:19])
    hour = hour + minute/60
    minute = minute + second/60
    #print(str(hour) + '\n' + str(minute) + '\n' + str(second))

    hour_angle = math.pi - (hour/12)*2*math.pi
    minute_angle = math.pi - (minute/60)*2*math.pi
    second_angle = math.pi - (second/60)*2*math.pi
    #print()

    time.sleep(1)

    #print(hour + '\n' + minute + '\n' + second)
    #time.sleep(5)
    pygame.draw.line(screen, h_color, r_center, point(r_center, h_length, hour_angle))
    pygame.draw.line(screen, m_color, r_center, point(r_center, m_length, minute_angle))
    pygame.draw.line(screen, s_color, r_center, point(r_center, s_length, second_angle))
    pygame.display.update()
