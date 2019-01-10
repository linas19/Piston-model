import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import cmath
from cmath import sqrt
from math import exp, expm1
from matplotlib.patches import Arc
import numpy as np
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111)
#Define parameters of piston (L - length of the connecting rod; a - crank radius; theta - crank angle)
L = 120
a = 50
color = ""
crankAngle = 1
theta = (2*math.pi/360)*crankAngle

#Define parameters of cylinder
cylinderRadius = 50
cylinderHeight = 185
pistonDiameter = cylinderRadius * 2
pistonH = 20
y = math.pow(L, 2) - math.pow(a, 2) * math.pow(math.sin(theta),2)
pistHeight = a * math.cos(theta) + cmath.sqrt(y)
actualPistHeight = float(pistHeight.real)

#Calculate Volume of Piston Cylinder
Volume = (math.pi * (cylinderRadius) * (cylinderRadius) * (cylinderHeight - actualPistHeight - 10))
#Calculate surface area of cylinder head
surfaceAreaCylinderHead = math.pi * (cylinderRadius) * (cylinderRadius)
print(surfaceAreaCylinderHead)
#Calculate surface area of cylinder wall
surfaceCylinderWall = math.pi * cylinderRadius * (cylinderHeight - actualPistHeight - 10)
#Calculate total surface area of cylinder 
surfaceTotal = surfaceAreaCylinderHead + surfaceCylinderWall
#Calculate pressure inside the cylinder P=V/(nRT)
# pressure = Volume / ()
#Define coloring limits:
if actualPistHeight < 120 or actualPistHeight > 280:
	color = "red"
else:
	color = "blue"

#Draw cylinder
plt.plot([-cylinderRadius,-cylinderRadius],[50,cylinderHeight],'r')
plt.plot([cylinderRadius,cylinderRadius],[50,cylinderHeight],'r')
plt.plot([-cylinderRadius,cylinderRadius],[cylinderHeight,cylinderHeight],'r')
r1 = patches.Rectangle((-cylinderRadius,actualPistHeight-10), pistonDiameter, pistonH, alpha=0.50)
r2 = patches.Rectangle((-cylinderRadius,actualPistHeight + pistonH -10), pistonDiameter, (cylinderHeight - actualPistHeight - pistonH + 10), color=color, alpha=0.50)
#Define parameters displayed on screen
plt.annotate('Volume: ' + str(int(Volume)), xy=(2, 1), xytext=(180, 200))
plt.annotate('Piston height: ' + str(int(actualPistHeight)), xy=(2, 1), xytext=(180, 220))
plt.annotate('Surface area: ' + str(int(surfaceTotal)), xy=(2, 1), xytext=(180, 240))

#Define axis
plt.axis([-150, 300, -150, 300])
ax.add_patch(r1)
ax.add_patch(r2)

#Draw connecting rod (red)
plt.plot([a * math.sin(theta), 0], [a * math.cos(theta), actualPistHeight], 'red')
#Draw crank radius (green)
plt.plot([0, a * math.sin(theta)], [0, a * math.cos(theta)], 'green')
#Draw C1 (red point)
plt.plot([a * math.sin(theta) / 2],[(actualPistHeight + a * math.cos(theta)) / 2], 'ro')
#Draw C2 (green point)
plt.plot([a * math.sin(theta) / 2], [a * math.cos(theta) / 2], 'go')
#Draw C3 (blue point)
plt.plot([0], [actualPistHeight], 'bo')
#Draw crank angle arc fi (blue)
ax.add_patch(Arc((0, 0), 50, 50, angle = 90 - crankAngle,
             theta1=0, theta2=crankAngle, 
             edgecolor='b'))
#Calculate and draw angle beta (green)
if crankAngle >= 180:
	beta = math.acos((L * L + actualPistHeight * actualPistHeight - a * a) / (2 * actualPistHeight * L)) * (180/math.pi) + 180
else:
	beta = 180 - math.acos((L * L + actualPistHeight * actualPistHeight - a * a) / (2 * actualPistHeight * L)) * (180/math.pi)

print("Beta=" + str(beta))
ax.add_patch(Arc((0, actualPistHeight), 50, 50, angle = 90 - beta,
             theta1=0, theta2=beta, 
             edgecolor='g'))

#Define parameters displayed on screen
plt.annotate('Beta: ' + str(int(beta)), xy=(2, 1), xytext=(180, 260))
plt.annotate('Crank angle: ' + str(int(crankAngle)), xy=(2, 1), xytext=(180, 280))




plt.show()
