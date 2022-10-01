from shapes import *
from functions import *

class Cell:
   # 1st char = name, 2nd = number of rotations, 3rd = number of reflections
   s = { "s1" : ["p00"], # List of all the shapes possible, indexed by the number of cells
      "s2" : ["s00", "s10"], 
      "s3" : ["l00", "l10", 
         "c00", "c10", "c20", "c30"], 
      "s4" : ["O00", 
         "J00", "J10", "J20", "J30", "J01", "J11", "J21", "J31", 
         "i00", "i10", 
         "z00", "z10", "z01", "z11", 
         "t00", "t10", "t20", "t30"], 
      "s5" : ["L00", "L10", "L20", "L30", "L01", "L11", "L21", "L31", 
         "T00", "T10", "T20", "T30", 
         "N00", "N10", "N20", "N30", "N01", "N11", "N21", "N31", 
         "Z00", "Z10", "Z01", "Z11", 
         "I00", "I10", 
         "P00", "P10", "P20", "P30", "P01", "P11", "P21", "P31", 
         "W00", "W10", "W20", "W30", 
         "F00", "F10", "F20", "F30","F01", "F11", "F21", "F31", 
         "X00", 
         "Y00", "Y10", "Y20", "Y30", "Y01", "Y11", "Y21", "Y31"]}
   
   def __init__(self, co: list, val: int): # Initialisaiton
      self.co = co # Coordinates
      self.val = val # Value
      self.numGroup = None # Number of group
      self.lpos = [z + 1 for z in range(self.val)] # List of possible positions
      self.lform = list(Cell.s["s" + str(self.val)]) # List of possible forms
      self.selForm = None # Selected form
      self.selPos = None # Selected position
      self.coefx = None # Coefficient of x
      self.coefy = None # Coefficient of y
   
   def give(self): # Give a new form and/or position
      if self.selForm == None:
         self.selForm = select(extract(self.lform))
      elif len(self.lpos) == 0:
         if len(self.lform) == 0:
            return False
         else:
            self.selForm = select(extract(self.lform))
            self.lpos = [z + 1 for z in range(self.val)]
      self.selPos = extract(self.lpos)
      
      z = 0 # Determination of the position of the selected form corresponding to the number
      for y in range(len(self.selForm)):
         for x in range(len(self.selForm[0])):
            if self.selForm[y][x] == 1:
               z += 1
               if z == self.selPos:
                  coForme = [y, x] # Coordinates of the point inside the form
      
      self.coefx = self.co[1] - coForme[1]
      self.coefy = self.co[0] - coForme[0]
      
      return True
   
   def getSelForm(self):
      return self.selForm
   
   def getCoefx(self):
      return self.coefx
   
   def getCoefy(self):
      return self.coefy
   
   def getNum(self):
      return self.numGroup
   
   def setNum(self, num: int):
      self.numGroup = num