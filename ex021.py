# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): pass
