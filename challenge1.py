class Point:

    def __init__(self,x,y,z):
        self.x = x=1
        self.y = y=3
        self.z = z=5

    def sqSum(self):
        return(self.x**2+self.y**2+self.z**2)
a=Point(1,3,5)
print(a.sqSum())