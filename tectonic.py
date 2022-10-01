from random import randint, choice
from cell import *
from solver import *
from functions import *

def generate(x, y) -> list:
   
   xMatrice = x
   yMatrice = y
   
   #### Phase 1 : Creation of a matrix of numbers ####
   
   tab = [[0 for i in range(xMatrice)] for j in range(yMatrice)] # Creation of the matrix (empty)
   for i in range(yMatrice):
      for j in range(xMatrice):
         cond = True
         while cond:
            cond = False
            nb = randint(1, 5)
            for k in range(-1, 2):
               for l in range(-1, 2):
                  if i + k >= 0 and i + k < yMatrice and j + l >= 0 and j + l < xMatrice and nb == tab[k + i][l + j]:
                     cond = True
         tab[i][j] = nb
   
   l = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]] # Counting occurrences of numbers in the matrix
   for i in range(yMatrice):
      for j in range(xMatrice):
         a = tab[i][j]
         l[a - 1][1] += 1
   
   for i in range (1, len(l)): # Sort occurrences in ascending order
        j = i
        while l[j][1] > l[j - 1][1] and j > 0:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1
   
   t2 = [[0 for i in range(xMatrice)] for j in range(yMatrice)]
   for k in range(len(l)): # Exchange of the numbers to respect the rule ( nb 1 >= nb 2 >= nb 3 >= nb 4 >= nb 5)
      for i in range(yMatrice):
         for j in range(xMatrice):
            if tab[i][j] == l[k][0]:
               t2[i][j] = k + 1
   tab = list(t2)
   
   #### Phase 2 : Setting up shapes ####
   
   formTab = [[0 for i in range(xMatrice)] for j in range(yMatrice)] # Creation of the form matrix
   all = []
   tailleMatrice = [yMatrice, xMatrice]
   state = True
   while isFin(formTab, 0):
      if state:
         current = next(tab, formTab)
         all.append(Cell(current[1:], current[0])) # Creation of a new element
         state = False
      
      if all[-1].give(): # See if the element is finished
         forme = all[-1].getSelForm() # Retrieving the shape of the element
         tailleForme = len(forme), len(forme[0]) # Retrieving of the size of the form
         coefx = all[-1].getCoefx() # Retrieving of the coefficient in x of the element
         coefy = all[-1].getCoefy() # Retrieving of the coefficient in y of the element
         
         if inGrid(coefx, coefy, tailleForme, tailleMatrice): # Verifications
            if with0(forme, formTab, coefx, coefy):
               if allNums(forme, tab, coefx, coefy):
                  n = len(all)
                  all[-1].setNum(n) # Affectation of the number of the form
                  for y in range(tailleForme[0]):
                     for x in range(tailleForme[1]):
                        if forme[y][x] == 1:
                           formTab[y + coefy][x + coefx] = n
                  state = True
      else:
         all.pop()
         if len(all) == 0:
            return 'Error', tab
         for y in range(len(tab)):
            for x in range(len(tab[0])):
               if all[-1].getNum() == formTab[y][x]:
                  formTab[y][x] = 0
   
   ### Phase 3 : Clearing some cells ###
   
   tabCheck = [[False for i in range(xMatrice)] for j in range(yMatrice)]
   tabNumber = [[(j, i) for i in range(xMatrice)] for j in range(yMatrice)]
   while isFin(tabCheck, False):
      y, x = choice(choice(tabNumber))
      if tabCheck[y][x] == False:
         save = tab[y][x]
         tab[y][x] = 0
         if not numOfSol(tab, formTab):
            tab[y][x] = save
         tabCheck[y][x] = True
   
   return tab, formTab