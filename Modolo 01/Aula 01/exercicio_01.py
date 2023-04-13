class Poligono:
  def __init__(self, paramSide, paramNumberOfSide, paramApothem):
    self.atribSide = paramSide
    self.atribNumberOfSide = paramNumberOfSide
    self.atribApothem = paramApothem

  def calculatePerimeter(self):
    perimeter = self.atribSide * self.atribNumberOfSide
    return perimeter


  def calculateArea(self):
    area = (self.calculatePerimeter() * self.atribApothem) / 2
    return area


triangulo = Poligono(5, 3, 5)
quadrado = Poligono(4, 4, 2)
pentagono = Poligono(13, 5, 2)
hexagono = Poligono(7, 6, 3)
heptagono = Poligono(3, 7, 5)
octagono = Poligono(4, 8, 5)
eneagono = Poligono(1, 9, 4)
decagono = Poligono(6, 10, 3)

print(f'Area: {triangulo.calculateArea()} | Perimetro: {triangulo.calculatePerimeter()}')
print(f'Area: {quadrado.calculateArea()} | Perimetro: {quadrado.calculatePerimeter()}')
print(f'Area: {pentagono.calculateArea()} | Perimetro: {pentagono.calculatePerimeter()}')
print(f'Area: {hexagono.calculateArea()} | Perimetro: {hexagono.calculatePerimeter()}')
print(f'Area: {heptagono.calculateArea()} | Perimetro: {heptagono.calculatePerimeter()}')
print(f'Area: {octagono.calculateArea()} | Perimetro: {octagono.calculatePerimeter()}')
print(f'Area: {eneagono.calculateArea()} | Perimetro: {eneagono.calculatePerimeter()}')
print(f'Area: {decagono.calculateArea()} | Perimetro: {decagono.calculatePerimeter()}')