# -*- coding: utf-8 -*- 
'''
Created on 20.04.2012

@author: Denis
'''

import pygame
import sys
import os
from pygame import key
from logging.config import ConvertingList
from sprites import Text_sprite
from sprites import Img_sprite
from game_object import Bot

class Replay_player(object):
    '''
    classdocs
    '''        
    def __init__(self,game_name='test.hgg'):
        '''
        Constructor
        '''
        window_w = 550
        window_h = 600
        self.running = True
        self.line_color = (0,0,0)
        self.line_begin = (0,0)
        self.window_init(window_w,window_h)
        clock = pygame.time.Clock() #fps
    
    def window_init(self,window_w,window_h,bg_color=(255,255,255)):
        pygame.init()
        self.w_bg_color = bg_color 
        self.window_w_h = window_w,window_h
        
        self.screen = pygame.display.set_mode(self.window_w_h)
        pygame.display.set_caption('Bubble wars')
        self.screen.fill(self.w_bg_color)
        
        self.img = Img_sprite()
        self.border, self.border_rect = self.img.load_png("border.png")
        self.map, self.map_rect = self.img.load_png("map.png")
        
        self.screen.blit(self.border,(0,0))
        self.screen.blit(self.map,(0,60))
        pygame.display.flip()
                   
    def play(self): 
        '''
        no comments
        ''' 
        #text = Text_sprite(self.screen) 
        while self.running:
            event = pygame.event.poll()          
            if event.type == pygame.QUIT or (event.type == pygame.K_ESCAPE and event.type == pygame.KEYDOWN) :
                pygame.quit()
                sys.exit(0)
                break
            elif event.type == pygame.MOUSEMOTION:
                self.screen.blit(self.map,(0,50))    # Map
                ###
                # player objects
                ###
                
                #text.draw("  "+str(event.pos[0])+" "+str(event.pos[1]) , event.pos)
                #text.render_text("  "+str(event.pos[0])+" "+str(event.pos[1]))
                #self.screen.blit(temp,event.pos) 
                #text.group.draw(self.screen)
                pygame.draw.aaline(self.screen,self.line_color,self.line_begin,event.pos) 
                ###
                # player objects
                ###
                self.screen.blit(self.border,(0,0))  # Border  
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.line_begin = event.pos
                

            pygame.display.flip()
            #clock.tick(30) 
                #pygame.display.update()
    