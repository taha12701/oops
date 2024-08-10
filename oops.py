# #creating class
# class Student:
#   name="Taha"


# #creating objects
# s1=Student()
# print(s1.name)

# class cars:
#   def __init__(self):
#     print("Printing new cars in database")
#   name="Mercedes"
#   model=2023

# c1=cars()
# print(c1.name)
# print(c1.model)


class Student:
  def __init__(self,fullName,marks):
    self.name=fullName
    self.marks=marks
    print("Adding new data in database.....")

s1=Student("Taha",94)
print(s1.name,s1.marks)


