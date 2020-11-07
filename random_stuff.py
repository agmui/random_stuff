
# -----------------------------------------------------------------------------------
# class method and static method
# class method does not depend on the __init__ parameters and can just run with its own parameters
# can modify class state
# very useful in sub-classes bc u can use the same class method in the sub-classes as well

#static method is exactly like class method but cant change anything in the class
class Student:
    count = 0  # this var belongs to the class

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def msg(self):
        print(self.name)

    @classmethod  # this is a class method so it belongs to the entire class not the object
    def object_count(cls):  # it senses every time the class is called and returns count
        return cls.count

    @classmethod
    def student_Age(cls, age):  # does not need __init__ and has its own parameters
        return age

    @staticmethod
    def student_grade():
        return 


s1 = Student("bob")
s2 = Student("jeff")
print(Student.count)
print(Student.object_count())
print(s1.count)
print(s1.object_count())

# -----------------------------------------------------------------------------------

"""class myClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def printVar1(self):
        print(str(self.var1))

    def printVar2(self):
        print(str(self.var2))


text1 = myClass(1, 2)
text2 = myClass(1, 2)
text1.printVar1()"""
# -----------------------------------------------------------------------------------

""""# the oj or how u would normaly do it
n2 = 200
if n2 > 20:
    print(n2)
# the := assings 200 to n2
if (n2 := 200) > 20:
    print(n2)"""
# -----------------------------------------------------------------------------------

"""numbers = [12, 34, 1, 4, 4, 67, 37, 9, 0, 81]

result = []
for number in numbers:
    if number > 5:
        result.append(number)
print(result)  #Prints [12, 34, 67, 37, 9, 81]

#the better way
result = [number for number in numbers if number > 5]
#[function(number) for number in numbers if condition(number)]

l=[0]
print(l[0] for i in range(0))
#for i in range(2): print(i);"""
