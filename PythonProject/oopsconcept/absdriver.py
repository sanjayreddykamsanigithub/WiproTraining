from oopsconcept.rectangle import Rectangle
from oopsconcept.square import Square

sqobj = Square(10)

print(f'Area: {sqobj.calculate_area()} \tPerimeter : {sqobj.calculate_perimeter()}')

rectobj = Rectangle(10, 5)

print(f'Area: {rectobj.calculate_area()} \tPerimeter : {rectobj.calculate_perimeter()}')
