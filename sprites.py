# -*- coding: utf-8 -*- 
'''
Created on 21.04.2012

@author: Denis
'''
import os
import pygame
from pygame.examples.mask import Sprite
from pygame import rect


class mSprite(pygame.sprite.DirtySprite):
    '''
    text, img and std obj
    '''    
    
    def __init__(self,x,y,rect = {"left":0, "top":0, "width":0, "height":0}):
        '''
        Please don't use x<=0 or y<=0 else you will will die in 7 days.
        ''' 
        pygame.sprite.DirtySprite.__init__(self)
        if (x<=1 or y<=1) :
            if x<=0:
                pass#x=10
            if y<=0 :
                pass#y=10
        self.x = x                           
        self.y = y                       
        self.rect = pygame.Rect(rect["left"],rect["top"],rect["width"],rect["height"])
        self.rect.centerx=x
        self.rect.centery=x
        
    def move_x(self, x):
        """
        Смещение по ОХ на х единиц.
        """
        self.x = self.x + x
        self._move()
    
    def move_y(self, y):
        """
        Смещение по ОY на y единиц.
        """
        self.y = self.y + y
        self._move()
        
    def move_vector(self,x,y):
        """
        Смещение по XY. 
        """
        self.x = self.x + x
        self.y = self.y + y
            
    def set_x(self, x):
        """
        Смена х.
        """
        self.x = x
        self.move()
    
    def set_y(self, y):
        """
        Смена у.
        """
        self.y = y
        self.move()
        
    def set_pos(self,(x,y)):
        """
        Смена х-у.
        """
        self.set_x(x)
        self.set_y(y)
        
    def get_pos(self):
        return self.x,self.y 
       
    def move(self):
        """
        Перемещение центра объекта в т. х-у.
        """
        self.rect.center = (self.x,self.y)
                
class Text_sprite(mSprite):
    '''
    Hier, t'en souviens-tu? c'etait la chasse-neige,
    Les tenebres, la nuit, tout le bruyant cortege
    Des demons de l'hiver qui frappait nos vitraux,
    La lune se perdait comme une large opale
    Au ciel noir, et ta main soutenait ton front pale.
    Mais ce matin... allons; approche des carreaux...
                                        A.S. Pouchkine
    '''
    # group = pygame.sprite.Group()
    def __init__(self,player_window, font_type=None, size=12, color=(255,0,0),pos=(10,10)):
        mSprite(9,9)
        self.font_type = font_type
        self.font_size = size
        self.font_color = color
        self.text_img = None
        
    def draw(self,text='',pos=(0,0)):
        '''
        Rendering and print the string on the screen
        '''
        mSprite.set_pos(self,pos)
        self.render_text(text) 
        
    def render_text(self,text):
        self.font = pygame.font.Font(self.font_type, self.font_size)
        self.text_img = self.font.render(text, True, self.font_color)
        return  self.text_img
                   
    def set_new(self,text):
        self.text=text
        
    def set__font_color(self,(r,g,b)):
        self.font_color((r,g,b)) 
        
    def set_font_type (self,x):
        self.font_type(x)
           
    def set_font_size(self,size):
        if size>0:
            self.font_size=size
        
    def get_pos(self):
        return self.pos  
          
    def get__font_color(self):
        return self.font_color 
    
    def get_font_type (self):
        return self.font_type 
      
    def get_font_size(self):
        return self.font_size
             
class Img_sprite(mSprite):
    '''
    Peace! Labor! May!
    '''
    #group = pygame.sprite.Group()
    p_1 = ["w_1.png","e_1.png","b_1.png","as_1.png","hs_1.png","eg_1.png","wg_1.png"]
    p_2 = ["w_2.png","e_2.png","b_2.png","as_2.png","hs_2.png","eg_2.png","wg_2.png"]
    p_3 = ["w_3.png","e_3.png","b_3.png","as_3.png","hs_3.png","eg_3.png","wg_3.png"]
    p_4 = ["w_4.png","e_4.png","b_4.png","as_4.png","hs_4.png","eg_4.png","wg_4.png"]
    
    code_list = [p_1,p_2,p_3,p_4]
    download_img = {}
    
    def __init__(self,folder='img',x=1,y=1):
        '''
        '''          
        mSprite(x, y)
        self.in_folder = folder
        
    def load_png(self,name):
        """ Load image and return image object"""
        fullname = os.path.join(self.in_folder, name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error, message:
                print 'Cannot load image:', fullname
                raise SystemExit, message
        return image, image.get_rect()
    
    def get_img(self,name):
        if name in self.img_base:
            return self.img_base[name]
        else:
            return self.img_base['temp']
    
    def get_img_dict_for_code(self,bots_code):
        """
        Загрузка всех текстур бота
        
         
        Выбираем список текстур в зависимости от кода.
        Загружеам все текстуры.
        Формируем словарь имен текстур и ссылок на загруженные текстуры.
        Вовращаем словарь. 
        """
        
        dict = Img_sprite.get_img_dict(Img_sprite.code_list[bots_code])
        #for img_name in Img_sprite.code_list[bots_code]: 
        #        img = self.load_png(img_name)
        #        name = img_name[:-6]
        #        dict[name] = img
        Img_sprite.download_img[bots_code]=dict
        return dict
    
    def get_img_dict(self,list=[]):
        dict = {}
        for img_name in list: 
                img = self.load_png(img_name)
                name = img_name[:-6]
                dict[name] = img
        return dict
        
    def add_draw_img(self,sprite):
        self.group.append(sprite)    
        
    def load_bmp(self,name,colorkey):
        """
        Загрузка текстуры в формате .bmp по имени
        Установление прозрачности 
            по значению colorkey
            либо по значению левого верхнего пиксела.
        """
        fullname = os.path.join(self.in_folder, name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print "Cannot load image:", name
            raise SystemExit, message
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image, image.get_rect()
           
    def add_png_img(self,name,extn):
        '''
        Apload and saving in base img from source file by name + extn
        '''
        self.img_base[name] = Img_sprite.load_png(name+extn)
        
##########################################

if __name__=="__main__":
    q=mSprite(0,0)
    q.move()