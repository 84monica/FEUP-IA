#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
# Modules
import pygame
import sys

sys.path.append('interface')

import director
import scene_home
import scene_ai_uniform
import scene_ai_heuristic
import scene_human
import scene_bfs

import scene_iterative
import scene_greedy
 
def main():
    dir = director.Director()
    #scene = scene_bfs.SceneBFS(dir)
    scene = scene_home.SceneHome(dir)
    #scene = scene_greedy.SceneGreedy(dir)
    #scene = scene_human.SceneHuman(dir)
    dir.change_scene(scene)
    dir.loop()
 
if __name__ == '__main__':
    pygame.init()
    main()