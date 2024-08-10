class car():
  ceo="Anonymous"
  @staticmethod
  def start():
    print("The car has started....")

  @staticmethod
  def stop():
    print("The car has stopped....")


class ToyotaCar(car):

  def __init__(self,name):
    self.name=name
   

s1=ToyotaCar("Fortuner")
print(s1.start())

print(s1.stop())