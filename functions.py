from random import choice

def isFin(m, arg):
   '''Check if a matrix (m) has a cell with arg in it'''
   for i in range(len(m)):
      for j in range(len(m[0])):
         if m[i][j] == arg:
            return True
   return False

def next(t, tform):
   '''Find the next cell without any form in it, and with the biggest number'''
   a = [0, None, None]
   for i in range(len(t)):
      for j in range(len(t[0])):
         if tform[i][j] == 0:
            if t[i][j] > a[0]:
               a[0] = t[i][j]
               a[1] = i
               a[2] = j
   return a

def inGrid(cx, cy, tf, tm):
   '''Check if a matrix f can fit in a matrix m with the coefficients cx and cy'''
   if cx < 0 or cy < 0 or tf[0] + cy > tm[0] or tf[1] + cx > tm[1]:
      return False
   return True

def with0(fo, gr, cx, cy):
   '''Check if a form can fit in a formTab'''
   for i in range(len(fo)):
      for j in range(len(fo[0])):
         if fo[i][j] == 1 and gr[i + cy][j + cx] != 0:
            return False
   return True

def allNums(fo, tab, cx, cy):
   '''Check if all the nums in the form are from 1 to n'''
   liste = []
   for i in range(len(fo)):
      for j in range(len(fo[0])):
         if fo[i][j] == 1:
            liste.append(tab[i + cy][j + cx])
   
   liste.sort()
   if liste[0] != 1:
      return False
   for i in range(1, len(liste)):
      if liste[i] - liste[i - 1] != 1:
         return False
   return True

def testNear(co, tab):
   '''Check if the number at co is not present in the surrounding cells'''
   for i in range(-1, 2):
      for j in range(-1, 2):
         if i != 0 or j != 0:
            y = co[0] + i
            x = co[1] + j
            if y >= 0 and x >= 0 and len(tab) > y and len(tab[0]) > x:
               if tab[y][x] == tab[co[0]][co[1]]:
                  return False
   return True
   
def testForm(co, tab, formTab):
   '''Check if the numbers in the form are valid'''
   l = []
   for i in range(-4, 5):
      for j in range(-4, 5):
         y = co[0] + i
         x = co[1] + j
         if y >= 0 and x >= 0 and len(tab) > y and len(tab[0]) > x:
            if 0 <= abs(i) + abs(j) < 5:
               if formTab[y][x] == formTab[co[0]][co[1]]:
                  l.append(tab[y][x])
   
   l.sort()
   if l[-1] > len(l):
      return False
   l = [elt for elt in l if elt != 0]
   for i in range(1, len(l)):
      if l[i] == l[i - 1]:
         return False
   return True
         
def next2(tab):
   '''Find the next cell to put a number in'''
   for j in range(len(tab)):
      for i in range(len(tab[0])):
         if tab[j][i] == 0:
            return j, i

def extract(liste):
   '''Choose randomly an item from a list, remove it, and return it'''
   if len(liste) > 0:
      a = choice(liste)
      liste.remove(a)
      return a
   return None