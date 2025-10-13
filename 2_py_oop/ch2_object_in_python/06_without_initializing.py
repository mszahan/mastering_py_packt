class Point:
    def move (self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    
    def reset(self) -> None:
        self.move(0, 0)


p = Point()

p.x = 5

#this will throw and error
# AttributeError: 'Point' object has no attribute 'y'
print(p.y)