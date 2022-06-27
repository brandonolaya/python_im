class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(self.x, self.y)
    def distance(self, another_cordinate):
        print(self.x, self.y)
        print(another_cordinate.x, another_cordinate.y)
        x_distance = (self.x - another_cordinate.x)**2
        y_distance = (self.y - another_cordinate.y)**2

        return (x_distance + y_distance)**0.5

if __name__ == '__main__':
    coord_1 = Coordinate(5 , 15)
    coord_2 = Coordinate(1,15)
    
    print(coord_1.distance(coord_2))