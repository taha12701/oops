# class Student:                       #class attributes
#   college="Punjab College"
#   name="Taha"

#   def __init__(self,mname,mmarks):       #constructors
#     self.name=mname
#     self.marks=mmarks

#   def welcome(self):                 #methods
#     print("Welcome Students", self.name)

#   def get_marks(self):              #methods
#     return s1.marks

# s1=Student("Babar",98)
# s1.welcome()
# print(s1.get_marks())


# class Student():
#   def __init__(self,mname,sub1,sub2,sub3):
#     self.name=mname
#     self.sub1=sub1
#     self.sub2=sub2
#     self.sub3=sub3

#   def cal_Avg(self):
#     avg=(s1.sub1 + s1.sub2 + s1.sub3)/3
#     return avg


# s1=Student("Taha",98,90,89)

# print(s1.cal_Avg())


#static methods

# class Student():

#   @staticmethod
#   def print():
#     print("Hello World")

#   def __init__(self,mname,sub1,sub2,sub3):
#     self.name=mname
#     self.sub1=sub1
#     self.sub2=sub2
#     self.sub3=sub3

#   def cal_Avg(self):
#     avg=(s1.sub1 + s1.sub2 + s1.sub3)/3
#     return avg


# s1=Student("Taha",98,90,89)
# s1.print()

# print(s1.cal_Avg())

#Abstraction #encapsulation


class bank():
  def __init__(self,bal,acc):
    self.bal=bal
    self.acc=acc

  def debit(self,debit):
    self.bal += debit
    print("The amount after debit is  ", s1.bal)
    
  def credit(self,credit):
    self.bal -= credit
    print("The amount after credit is  ", s1.bal)

  def get_bal(self):
    return s1.bal
  
  @staticmethod
  def print():
    print("Hello Guys")
  
s1=bank(63000,1234)
print("The account name is : ",s1.acc)
print("The balance is : ",s1.bal)
s1.debit(3400)
s1.credit(5000)