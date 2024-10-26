a = (input(''))
b = (input(''))
c = (input(''))

if a == b == c:
  print("Равносторонний треугольник")
elif (a == b) or (a == c) or (b == c):
  print("Равнобедренный треугольник")
else:
  print("Разносторонний треугольник")