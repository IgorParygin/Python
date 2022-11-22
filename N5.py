# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

def coordinates(x):
    xy = ['x', 'y']
    a = []
    for i in range(x):
        a.append(int(input(f'Введите координату {xy[i]}: ')))
    return a
def distance(a, b):
    dist = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    return dist


print('Введите координаты точки А')
pointA = coordinates(2)
print('Введите координаты точки В')
pointB = coordinates(2)

print(f'Расстояние между точками: {distance(pointA, pointB)}')