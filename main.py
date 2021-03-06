import pygame
import random

pygame.init()

class DrawInformation:
  BLACK = 0, 0, 0
  WHITE = 255, 255, 255
  GREEN = 0, 255, 0
  RED = 255, 0, 0
  GREY = 128, 128, 128
  BACKGROUND_COLOR = WHITE

  def __init__(self, width, height, toSort):
    self.width = width
    self.height = height

    # The drawing window is made into an attribute of the class
    self.window = pygame.display.set_mode((width, height))
