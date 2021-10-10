import pygame
import random
import os
import time
import neat
import visualize
import pickle
pygame.font.init()

WIN_WIDTH, WIN_HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy-Bird, Neat AI")

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pip.png")).convert_alpha())
bg_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")).convert_alpha())
bird_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird.png")).convert_alpha())
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")).convert_alpha())

gen = 0

class Bird:
  
  def __init__(self, x, y):
    self.x, self.y = x, y
    self.tilt = 0
    self.vel = 0
    self.img_count = 0
    self.img = self.IMGS(0)

  def jump(self):
    self.vel = -10.5
    self.tick_count = 0
    self.height = self.y
    
  def move(self):
    
