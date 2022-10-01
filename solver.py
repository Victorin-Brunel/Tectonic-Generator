from cell2 import *
from functions import *

def numOfSol(tab, formTab):
   all = []
   c = True
   state = True
   nbSol = 0
   while len(all) > 0 or c:
      c = False
      if state:
         a = next2(tab)
         if a != None:
            current = a
            all.append(Cell2(current)) # Creation of a new element
         state = False
      current = all[-1].getCo()
      
      if all[-1].give():
         n = all[-1].getNum()
         tab[current[0]][current[1]] = n
         if testNear(current, tab) and testForm(current, tab, formTab):
            state = True
         else:
            tab[current[0]][current[1]] = 0
      else:
         tab[current[0]][current[1]] = 0
         all.pop()
      
      if not isFin(tab, 0):
         nbSol += 1

   return nbSol == 1