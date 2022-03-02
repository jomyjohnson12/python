class Rectangle:
  def getData(self,length,breadth):
     self.length=length
     self.breadth=breadth
  def area(self):
     a=self.length*self.breadth
     print("Area of rectangle with length",self.length,"and breadth",self.breadth,"is",a)
  def perimeter(self):
     p=2*(self.length+self.breadth)
     print("perimter of rectangle with length ",self.length,"and breadth",self.breadth, "is",p)
ch=0
l=int(input("Enter length of a reactangle:"))
b=int(input("Enter Breadth of a rectangele:"))
obj=Rectangle()
obj.getData(l,b)
while ch!=3:
    print("1.Area")
    print("2.Perimeter")
    print("3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:obj.area()
    if ch==2:obj.perimeter()
else: print("End of the program")
    
