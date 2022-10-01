class Cell2:
   def __init__(self, co: tuple):
      self.pos = [1, 2, 3, 4, 5]
      self.num = 0
      self.co = co

   def give(self):
      if len(self.pos) == 0:
         return False
      else:
         self.num = self.pos[0]
         self.pos = self.pos[1:]
         return True
         
   def getNum(self):
      return self.num
   
   def getCo(self):
      return self.co     