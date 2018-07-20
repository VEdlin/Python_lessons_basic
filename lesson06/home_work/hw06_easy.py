# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        def side_len(point1,point2):
            return math.sqrt((point2[0] - point1[0])**2+(point2[1] - point1[1])**2)
        self.AB = abs(round(side_len(self.b,self.a), 2))
        self.AC = abs(round(side_len(self.c,self.a), 2))
        self.BC = abs(round(side_len(self.c,self.b), 2))
# попытка реализовать таблицу синусов        self.SIN_TABLE = [math.sin(math.radians(x)) for x in range(0, 181)]
# попытка реализовать таблицу косинусов      self.COS_TABLE = [math.cos(math.radians(x)) for x in range(0, 181)]
        
    def height(self):
#упрощенная конструкция. Не очень работает с тупоугольными треугольниками.
#лучше делать через acos, но, к сожалению, он здесь дает результат с очень большой погрешностью 
        return round(((2*self.area())/self.AB), 2)

    def prmtr(self):
        return self.AB + self.AC + self.BC

    def area(self):
        return abs(0.5 * ((self.a[0]-self.c[0])*(self.b[1]-self.c[1]) -\
                              (self.b[0]-self.c[0])*(self.a[1]-self.c[1])))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        def side_len(point1,point2):
            return math.sqrt((point2[0] - point1[0])**2+(point2[1] - point1[1])**2)
        self.AB = abs(round(side_len(self.b,self.a), 2))
        self.BC = abs(round(side_len(self.c,self.b), 2))
        self.CD = abs(round(side_len(self.d,self.c), 2))
        self.DA = abs(round(side_len(self.a,self.d), 2))
        self.diag_AC = abs(round(side_len(self.c,self.a), 2))
        self.diag_BD = abs(round(side_len(self.d,self.b), 2))

    def prmtr(self):
        return self.AB + self.BC + self.CD + self.DA

    def area(self):
        return ((self.DA+self.BC)/2) * \
               (math.sqrt(self.AB**2 - \
                          (((self.DA-self.BC)**2 + self.AB**2 - self.CD**2) / (2*(self.DA - self.BC)))**2))

    def isisosceles(self):
        if self.diag_AC == self.diag_BD:
            return True
        return False
