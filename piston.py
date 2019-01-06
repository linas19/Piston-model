import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import cmath
from cmath import sqrt
from math import exp, expm1
from matplotlib.patches import Arc
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
#Define parameters of piston (L - length of the connecting rod; a - crank radius; theta - crank angle)
L = 120
a = 50
color = ""
theta = (2*math.pi/360)*360

#Define parameters of cylinder
cylinderRadius = 50
cylinderHeight = 185
pistonDiameter = cylinderRadius * 2
pistonH = 20
y = math.pow(L, 2) - math.pow(a, 2) * math.pow(math.sin(theta),2)
pistHeight = a * math.cos(theta) + cmath.sqrt(y)
actualPistHeight = float(pistHeight.real)
# print(y)

#Calculate Volume of Piston Cylinder
Volume = (3.14 * (cylinderRadius) * (cylinderRadius) * (cylinderHeight - actualPistHeight - 10))
#Calculate surface area of cylinder head
surfaceAreaCylinderHead = math.pi * (cylinderRadius) * (cylinderRadius)
print(surfaceAreaCylinderHead)
#Calculate surface area of cylinder wall
surfaceCylinderWall = math.pi * cylinderRadius * (cylinderHeight - actualPistHeight - 10)
#Calculate total surface area of cylinder 
surfaceTotal = surfaceAreaCylinderHead + surfaceCylinderWall

if actualPistHeight < 80:
	color = "red"
else:
	color = "blue"

#Draw cylinder
plt.plot([-cylinderRadius,-cylinderRadius],[50,cylinderHeight],'r')
plt.plot([cylinderRadius,cylinderRadius],[50,cylinderHeight],'r')
plt.plot([-cylinderRadius,cylinderRadius],[cylinderHeight,cylinderHeight],'r')
r1 = patches.Rectangle((-cylinderRadius,actualPistHeight-10), pistonDiameter, pistonH, alpha=0.50)
r2 = patches.Rectangle((-cylinderRadius,actualPistHeight + pistonH -10), pistonDiameter, (cylinderHeight - actualPistHeight - pistonH + 10), color=color, alpha=0.50)
#Define parameters on screen
plt.annotate('Volume: ' + str(int(Volume)), xy=(2, 1), xytext=(180, 200))
plt.annotate('Piston height: ' + str(int(actualPistHeight)), xy=(2, 1), xytext=(180, 220))
plt.annotate('Surface area: ' + str(int(surfaceTotal)), xy=(2, 1), xytext=(180, 240))

#Define axis
plt.axis([-150, 300, -150, 300])
ax.add_patch(r1)
ax.add_patch(r2)

#Draw connecting rod
plt.plot([a * math.sin(theta), 0], [a * math.cos(theta), actualPistHeight], 'red')
#Draw crank radius
plt.plot([0, a * math.sin(theta)], [0, a * math.cos(theta)], 'green')

plt.show()
