from my import welcomescreen,maingame,isCollide,getrandompipe,main
import pytest
import pygame
from pygame.locals import *

pygame.init()

def test_welcomescreen():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key== K_SPACE:
            welcomescreen() == None
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            with pytest.raises(SystemExit):
                welcomescreen()

def test_randompipe():
    assert getrandompipe() != None

def test_iscollide():
    assert isCollide(36 ,-3, [{'x': 321, 'y': -104}, {'x': 465.5, 'y': -183}], [{'x': 321, 'y': 365}, {'x': 465.5, 'y': 286}]) == True
    assert isCollide(36, 430, [{'x': 321, 'y': -104}, {'x': 465.5, 'y': -183}], [{'x': 321, 'y': 365}, {'x': 465.5, 'y': 286}]) == True
    assert isCollide(36, 255, [{'x': 77, 'y': -206.99999999999997}, {'x': 221.5, 'y': -104.99999999999997}] ,[{'x': 77, 'y': 263.33333333333337}, {'x': 221.5, 'y': 365.33333333333337}])== True
    assert isCollide(36,255,[{'x': 321, 'y': -104}, {'x': 465.5, 'y': -183}], [{'x': 321, 'y': 365}, {'x': 465.5, 'y': 286}]) == False
    
def test_maingame():
    if isCollide(36, -3, [{'x': 321, 'y': -104}, {'x': 465.5, 'y': -183}], [{'x': 321, 'y': 365}, {'x': 465.5, 'y': 286}]):
        maingame() == None
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            with pytest.raises(SystemExit):
                maingame()

