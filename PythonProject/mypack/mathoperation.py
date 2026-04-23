from basic_programs.basicshapes import areaofsquare, perimeterofsquare, areaofrect
from mypack.circle import areaofcircle, perimeterofcircle

radius = int(input('Enter Radius '))

print('Area : ', areaofcircle(rad=radius))
print('Peri : ', perimeterofcircle(rad=radius))

si = int(input('Enter side of sq '))
print('Area : ', areaofsquare(side=si))
print('Peri : ', perimeterofsquare(side=si))

l = int(input('Enter length '))
b = int(input('Enter breadth '))
print('Area : ', areaofrect(l,b))


