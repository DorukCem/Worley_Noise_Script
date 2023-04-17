import pygame
from sys import exit
import random
import math
import pygame.math

WIDTH = 400
HEIGHT = 400
DEPTH = 50

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE = (255, 255, 255)

random_points = [(random.randint(0, WIDTH),random.randint(0, HEIGHT), random.randint(0, DEPTH)) for _ in range(20)]

#------------ start
pixel_array = pygame.PixelArray(screen)

for x in range(WIDTH):
   for y in range(HEIGHT):
      distances = []
      for p in random_points:
         dist = ((p[0] - x)**2 + (p[1] - y)**2 + p[2]**2)**(1/2)
         distances.append(dist)

      distances.sort()
      
      r = min(1, distances[0]/130) * 255
      g = min(1, distances[1]/130) * 255
      b = min(1, distances[2]/130) * 255

      color = (r,g,b)

      pixel_array[x, y] = color

pixel_array.close()
#------------- end


while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()


   pygame.display.update()
