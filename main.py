#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
# Modules
import pygame
import sys

sys.path.append('/home/joao/Desktop/IA/FEUP-IA/interface')

import director
import scene_home
 
def main():
    dir = director.Director()
    scene = scene_home.SceneHome(dir)
    dir.change_scene(scene)
    dir.loop()
 
if __name__ == '__main__':
    pygame.init()
    main()