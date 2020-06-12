import pygame as pg
import pytmx
from pytmx.util_pygame import load_pygame
from settings import *


class TiledMap:
    def __init__(self, filename):
        tm = load_pygame(filename)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camara:
    def __init__(self, width, height):
        self.camara = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entidad):
        return entidad.rect.move(self.camara.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camara.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(ANCHO / 2)
        y = -target.rect.centery + int(ALTO / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - ANCHO), x)  # right
        y = max(-(self.height - ALTO), y)  # bottom
        self.camara = pg.Rect(x, y, self.width, self.height)
