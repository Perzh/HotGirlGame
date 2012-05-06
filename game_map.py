# -*- coding: utf-8 -*- 
'''
Created on 20.04.2012

@author: Denis
'''
import pygame
from sprites import Img_sprite

class c_game_map(object):
    '''
    �������� ������������ �������� �����
    '''
    def __init__(self,bg_name,walls_list):
        '''
        Constructor
        '''
        self.group = pygame.sprite.Group()
        wall_img = Img_sprite.__init__(x=1, y=1)
        