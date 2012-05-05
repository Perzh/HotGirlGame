# -*- coding: utf-8 -*- 
'''
Created on 20.04.2012

@author: Denis
'''
from compiler.ast import Add
from sprites import Img_sprite
import sys
import os
from pygame import key
from logging.config import ConvertingList
from pygame.tests.base_test import pygame_quit
import pygame
            
class Spell(object):
    """
    
    """
    def __init__(self,level=1,load=0,speed=1,):
        self.speed = speed
        self.quant = level
        self.load = load
        self.power = self.level*self.load
        self.delta_s = 0
    
    def load_apg(self):
        if self.delta_s >= self.speed:
            self.load += self.speed
            self.delta_s = 0
        else:
            self.delta_s += 1
            
    def level_apg(self,add=0):
        self.level += add
        
    def speed_upg(self,add=0):
            self.speed += add
        
    def power_apg(self):
        self.power = self.quant*self.load

class Crashable_obj():
    """
    """
    def __init__(self,helth=0):
        self.helth = helth
        self.max_helth = helth
        self.armor = Armor()
    
    def crah_helth(self,damage):
        self.helth -= int(damage*self.armor.hardness)
                 
class Armor():
    """
    """
    def __init__(self,hardness=0,quant = 0):
        Crashable_obj()
        self.hardness = hardness
        self.quant = quant
    
    def set_hardness(self,hardness=0):
        self.armor.hardness = hardness
    
    def crash_armor(self,damage):
        self.armor.quant -= damage  - int(damage*self.armor.hardness)  
    
    def set_armor_quant(self,quant):
        self.armor.quant = quant

class Gun(object):
    """
    Оружие юнитов бота
    """
    
    
    def __init__(self, img=None, damage=0):
        """
        Текстуры, урон
        """
        self.img = img
        self.damage = damage
  
    def damage_apg(self,x):
        self.e_damage += x
        
        self.w_damage += x
    
    def damage_set(self,x):
        self.damage = x
                   
    def get_damage(self):
        return self.damage
    
    def get_img(self):
        return self.img
    
class Warrior_Gun(Gun):
    """
    """
    b_wg_d = 5
    def __init__(self,img,damage=b_wg_d):
        Gun(img, damage)
        
class Engineer_gun(Gun):
    """
    """
    b_eg_d = 1
    
    def __init__(self,img,damage="b_w"):
        Gun(img, damage)
                         
class Unit(Crashable_obj):
    """
    """
    base_h = 100
    base_ac = 0
    base_ah = 10
    base_s = 10  #speed
    base_l = 25
    
    def __init__(self,
                 name,
                 img,
                 gun_img,
                 helth=base_h,
                 armor_hardness=base_ah,
                 armor_quant=base_ac,
                 speed=base_s,
                 look=base_l,
                 (x,y)=(0,0)):
        """
        unit
        """
        Crashable_obj.__init__(helth)
        self.name = name
        self.armor.set_armor_quant(armor_quant)
        self.armor.set_hardness(armor_hardness)
        self.img = img
        self.speed = speed
        self.look = look
    
    def apg_helth(self):
        pass
    def apg_speed(self):
        pass
    def apg_look(self):
        pass
    
    def armor_recover(self,x=0):
        self.armor.quant +=x

    def helth_recover(self,x=0):
        self.health += x
        
    def helth_set(self,x):
        self.helth = x
        
    def armor_set(self,x):
        self.img.armor.quant = x
    
    def move_xy(self,x=0,y=0):
        self.move_vector(x,y)
    
    def set_xy(self,x=1,y=1):
        self.img.set_pos(x,y)
    
    def get_unit_img(self):
        return self.img
              
class Warrior_Unit(Unit):
    """
    """
    def __init__(self,
                 name,
                 img,
                 gun_img,
                 helth=Unit.base_h,
                 armor_hardness=Unit.base_ah,
                 armor_quant=Unit.base_ac,
                 speed=Unit.base_s,
                 look=Unit.base_l,
                 (x,y)=(0,0)):
        Unit(name, img, gun_img, helth, armor_hardness, armor_quant, speed, look, (x, y))
        self.gun = Warrior_Gun(gun_img)

class Engineer_Unit(Unit): 
    """
    Юнит занимающийся сборкой ресурсов и разведкой
    
    атакует но слабее чем воин
    выше дальность обзора
    ниже здоровье
    """  
    b_h = 0.75
    b_ah = 0.96
    b_s = 1.25
    b_l = 1.15
     
    def __init__(self,
                 name,
                 img,
                 gun_img,
                 helth=Unit.base_h,
                 armor_hardness=Unit.base_ah,
                 armor_quant=Unit.base_ac,
                 speed=Unit.base_s,
                 look=Unit.base_l,
                 (x,y)=(0,0)):
        Unit.__init__(self,name, img, helth, armor_hardness, armor_quant, speed, look)
        self.helth = Unit.base_h*0.75
        self.armor.hardness = Unit.base_ah*0.96 
        self.speed = Unit.base_s*1.25
        self.look = Unit.base_l*1.5

class Building(Crashable_obj):
    """
    """
    
    base_h = 10000 # здоровье 
    base_ac = 0 # кол-во брони
    base_ah = 50    # 
    base_s = 0  #speed
    base_l = 50 # дальность обзора
    
    def __init__(self,name,img,helth=base_h,armor_hardness=base_ah,armor_quant=base_ac,speed=base_s,look=base_l,(x,y)=(0,0)):
       Crashable_obj(helth=Building.base_h)
       self.img = img
                   
class Bot():
    """
    
    """
    player_quant = 0
    
    def __init__(self, name="Anonim_"+str(player_quant), units_helth=Unit.base_h,units_speed=Unit.base_s):
        pygame.init()
        gold_quant = 0
        self.name = name
        bot_code = Bot.player_quant
        Bot.player_quant += 1
        img = Img_sprite()
        self.img_dict = img.get_img_dict_for_code(bot_code)
        self.buildings = [] # список зданий
        self.war_units = [] # список войнов
        self.engin_units = []   # список рабочих
        self.units = {"warrior":self.war_units,"engin":self.engin_units}
        self.gold = gold_quant
        self.war_skill = Spell()
        self.hum_skill = Spell()
    
    
    def cr_war_unit(self,name):
        x = Warrior_Unit(name, self.img_dict["w"])
        self.war_units.append(x)
        #return x

    
    def cr_engin_unit(self,name):
        x = Engineer_Unit(name, self.img_dict["e"])
        self.engin_units.append(x)
        # return x
    
    def cr_buliding_unit(self,name):
        x = Building(name, self.img_dict["b"])
        self.engin_units.append(x)
        pass      


            
if __name__=="__main__":
    q=Bot()       