'''
Created on 22.04.2012

@author: Denis
'''

class c_settings(object):
    '''
    classdocs
    '''
    class c_color():
                    
        def __init__(self):
            '''
            Constructor
            '''
            white   = (255,255,255)
            black   = (0,0,0)
            green   = (0,255,0)
            blue    = (0,0,255)
            red     = (255,0,0)
            grey    = (122,122,122)
            color = {white,black,green,blue,red}
            
        def get_color(name):
            '''
            Returned the RGB code of color, or black code if that color not found
            '''
            if name in color:
                return color[name]
            else:
                return 0,0,0
        
        def add_color(name,value):
            color[name]=value