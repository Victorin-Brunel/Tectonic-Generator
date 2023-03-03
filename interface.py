from tkinter import *
from tectonic import *

def g(x, y):
   canvas.delete("all")
   if x * y > 35:
      canvas.create_text(125, 125, anchor = CENTER, text = 'Too big size !', font = (15))
   else:
      tab, formTab = generate(x, y)
      if tab == 'Error':
         a = ''
         for elt in formTab:
            for i in elt:
               a += str(i)
         print('Error : no shape placement configuration found - Code error : ' + str(y) + str(x) + a)
      else:     
         if x != y: # Creation of the frame
            max = x if x > y else y
            min = y if x > y else x
            length = 250 / max
            ecart = (max - min) * length / 2
            if x > y:
               x1, x2, y1, y2 = 3, 250, 3 + ecart, 250 - ecart
            else:
               x1, x2, y1, y2 = 3 + ecart, 250 - ecart, 3, 250
         else:
            x1, y1, x2, y2 = 3, 3, 250, 250
            length = 250 / x
         
         canvas.create_rectangle(x1, y1, x2, y2, width = 3)
         
         for i in range(1, x):
            for j in range(y):
               canvas.create_line(x1 + i * length, y1 + j * length - 1, x1 + i * length, y1 + (j + 1) * length - 3 * (j == y - 1) + 2, width = 1 if formTab[j][i] == formTab[j][i - 1] else 3)
               
         for i in range(1, y):
            for j in range(x):
               canvas.create_line(x1 + j * length - 1, y1 + i * length, x1 + (j + 1) * length - 3 * (j == x - 1) + 2, y1  + i * length, width = 1 if formTab[i][j] == formTab[i - 1][j] else 3)
      
         for i in range(x):
            for j in range(y):
               a = tab[j][i]
               if a != 0:
                  canvas.create_text(x1 + length * (i + 1 / 2), y1 + length * (j + 1 / 2), anchor = CENTER, text = a, font = ('BOLD'))

window = Tk()
window.title("Tectonic Generator")
window.iconbitmap("T.ico")
window.minsize(500, 370)
window.maxsize(500, 370)
window.rowconfigure(0, minsize = 80)
window.rowconfigure(2, minsize = 40)
window.columnconfigure(0, minsize = 50)
window.columnconfigure(1, minsize = 250)
window.columnconfigure(2, minsize = 150)
window.columnconfigure(3, minsize = 50)

top = Frame(window)
titre = Label(top, text = "Tectonic Generator", font = (20))
top.grid(row = 0, column = 0, columnspan = 4)
titre.pack()

middleL = Frame(window)
canvas = Canvas(middleL, height = 250, width = 250)
middleL.grid(row = 1, column = 1)
canvas.pack()

middleR = Frame(window)
t = Label(middleR, text = 'Size')
t.grid(column = 0, row = 0, columnspan = 2)
x = IntVar()
x.set(5)
l1 = Label(middleR, text = 'X = ')
e1 = Entry(middleR, width = 10, textvariable = x)
l1.grid(column = 0, row = 1)
e1.grid(column = 1, row = 1)

y = IntVar()
y.set(5)
l2 = Label(middleR, text = 'Y = ')
e2 = Entry(middleR, width = 10, textvariable = y)
l2.grid(column = 0, row = 2)
e2.grid(column = 1, row = 2)

b = Button(middleR, text = "Generate", command = lambda:g(int(e1.get()), int(e2.get())))
b.grid(row = 3, column = 0, columnspan = 2)
middleR.grid(row = 1, column = 2)

window.mainloop()