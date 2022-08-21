# -*- coding: utf-8 -*-
"""
Created by dee-ah-nuh

"""
import time
import pandas as pd
import numpy as np
import pygame
import sys


print("AlienInvasion")
time.sleep(3)

message = "A ship that fires bullets"
print(message + "...")
time.sleep(2)

print("     !")
time.sleep(2)

print("     !")
time.sleep(2)

print("     !")
time.sleep(2)

print("     !")

''' a ship that fires bullets '''

''' instructions to gameplay: in AlienInvasion, the player controls a rocket ship
that appears at the bottom of the screen. Player can move the ship left, or right,
 using the arrow keys, and can shoot bullets using the spacebar! If the player,
 removes all aliens from the screen a new fleet will appear and willl move faster,
 than the previous. If an alien hits the players ships or reaches the bottom of
 the screen, the player loses a ship and the game concludes once a player
 loses all three ships'''
 
# =============================================================================
#  creating a pygame window and responding to User input
# =============================================================================
class AlienInvasion:
    
    def __init__(self):
        '''initializing the game , create resources '''
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        '''main loop for the game'''
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            
if __name__ =='__main__':
    ai = AlienInvasion()
    ai.run_game()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
