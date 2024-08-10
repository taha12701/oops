# # class student:

# #   def __init__(self,name):
# #     self.name=name

# # s1=student("Taha")    #Public class
# # del s1.name
# # print(s1.name)


# class account:
#   def __init__(self,acc_no, acc_pass):
#     self.acc_no=acc_no
#     self.__acc_pass=acc_pass            #to make it private we use "__"
  

#   def reset_pass(self):
#     print(self.__acc_pass)


# acc1=account(12345,"abcde")
# # print(acc1.acc_pass)
# print(acc1.reset_pass())



# class student:
#   __name="Taha"

#   def __hello(self):
#     print("Hello User!!!")               

#   def welcome(self):
#     self.__hello()

# s1=student()
# print(s1.welcome())

class student:
  def __init__(self, name, passw):
    self.name=name
    self.__passw=passw

  def hello(self):
    print("The password is : ", self.__passw )

s1=student("Taha",12345)
# print(s1.__passw)
print(s1.hello())