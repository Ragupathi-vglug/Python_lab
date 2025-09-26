class Complex:
    def __init__(self,real=0.0,image=0.0):
            self.real=real
            self.image=image
    def __add__(self,c2):
          c3=Complex()
          c3.real=self.real+c2.real
          c3.image=self.image+c2.image
          return c3
    def __sub__(self,c2):
          c3=Complex()
          c3.real=self.real-c2.real
          c3.image=self.image-c2.image
          return c3
    def display(self):
          print(self.real,"+i",self.image)

c1=Complex(10,20)
c2=Complex(5,15)
c3=Complex()
c4=Complex()
c3=c1+c2
c4=c1-c2

print("c1 = ",end="")
c1.display()
print("c2 = ",end="")
c2.display()

print("\nAddition of Complex Number C1 and C2 is :",end="")
c3.display()
print("\nSubtraction of Complex Number C1 and C2 is :",end="")
c4.display()