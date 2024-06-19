'''class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)'''


'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Jeonghan", 28)

print(p1.name)
print(p1.age)

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person1("RM", 31)

print(p1)'''

'''class Greetings():
    print("Bonjour Monsieur!")

g=Greetings()
print(g)'''

'''class Person:
  def __init__(vivi, name, age):
    vivi.name = name
    vivi.age = age

p1 = Person("Jeonghan", 28)
print(p1.name)
print(p1.age)'''

class Person1: #parent class
  def __init__(self, fname, lname, age):
    self.firstname = fname
    self.lastname = lname
    self.age = age

  def printname(self):
    print(self.firstname, self.lastname,self.age)

class Student(Person1): #child class
  pass

x = Student("Namjoon", "Kim",20)
x.printname()

class Person:
  def __init__(sel, name, age, city):
    sel.name = name
    sel.age = age
    sel.city = city

  def myfunc(sel):
    print("Hello my name is " + sel.name)

p1 = Person("Loid", 30, "Osaka")
p1.myfunc()


