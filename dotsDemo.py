#Heather Stafford
#3/1/18
#dotsDemo.py - how to use loops with graphics

from ggame import *

RADIUS = 25


red = Color(0xFF0000, 1)

dot = CircleAsset(RADIUS, LineStyle(1,red), red)

for i in range(10):
    for j in range(12):
        Sprite(dot,(10 + (2*RADIUS+10)*i,10 + (2*RADIUS+10)*j)) #putting a row of dots

App().run()
