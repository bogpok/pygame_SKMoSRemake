import os
import pygame as pg
import json 

def load_image(name, colorkey=None, scale=1, data_dir = ''):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    
    image = pg.transform.scale(image, size)

    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()


def load_json(filename):    
    f = open(filename)    
    data = json.load(f)
    f.close()
    return data