import pygame
from sys import exit
import random
import math
import pygame.math

WIDTH = 400
HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE = (255, 255, 255)

random_points = [(random.randint(0, WIDTH),random.randint(0, HEIGHT)) for _ in range(100)]

#------------ start
pixel_array = pygame.PixelArray(screen)

for x in range(WIDTH):
   for y in range(HEIGHT):
      
      min_dist = float("inf")
      for p in random_points:
         dist_sqr = (p[0] - x)**2 + (p[1] - y)**2
         if dist_sqr < min_dist:
            min_dist = dist_sqr
      min_dist = math.sqrt(min_dist)
      weight = min(1, min_dist/50)
      
      color =  pygame.Color.lerp(pygame.Color(BLACK), pygame.Color(WHITE), weight)

      pixel_array[x, y] = color

pixel_array.close()
#------------- end


while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()


   pygame.display.update()
