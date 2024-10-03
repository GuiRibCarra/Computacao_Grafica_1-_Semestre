import math
import tkinter as tk
import numpy as np

class Cohen:
    def __init__(self, root):
        self.root = root
        self.root.title("Cohen-Sutherland")
        self.retas = False
        self.window = False
        self.x, self.y = 0,0
        self.pontos_janelas = []

        self.canvas = tk.Canvas(root, width=700, height=700, bg="white")
        self.canvas.grid(row=0, column=0, sticky=tk.W)

        self.menubar = tk.Menu(root)
        self.img_menu = tk.Menu(self.menubar, tearoff=0)
        self.img_menu.add_command(label="Janela", command=self.activate_window)
        self.img_menu.add_command(label="Retas", command=self.activate_retas_y)
        self.menubar.add_cascade(label="Operacoes", menu=self.img_menu)

        self.root.config(menu=self.menubar)

    def get_x1_y1(self, event):
        self.x, self.y = event.x, event.y

    def activate_retas_y(self):
        self.retas = True
        self.canvas.bind("<Button-1>", self.get_x1_y1)
        self.canvas.bind("<ButtonRelease-1>",self.calculo)

    def activate_window(self):
        self.window = True
        self.canvas.bind("<Button-1>", self.get_x1_y1)
        self.canvas.bind("<ButtonRelease-1>", self.show_window)

    def desactivate_window(self):
        self.window = False
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.img_menu.entryconfig("Janela",state='disabled')

    def show_window(self,event):
        x2,y2 = event.x, event.y
        print(self.x, self.y)
        print(x2, y2)
        if self.x < x2:
            i = self.x
            while i <= x2:
                self.canvas.create_line(i, self.y, i + 1, self.y, fill='red')
                self.canvas.create_line(i, y2, i + 1, y2, fill='red')
                i = i + 1
        else:
            i = x2
            while i <= self.x:
                self.canvas.create_line(i, self.y, i + 1, self.y, fill='red')
                self.canvas.create_line(i, y2, i + 1, y2, fill='red')
                i = i + 1

        if self.y>y2:
            i = self.y
            while i >= y2:
                self.canvas.create_line(self.x, i, self.x + 1, i, fill='red')
                self.canvas.create_line(x2, i, x2 + 1, i, fill='red')
                i = i - 1
        else:
            i = y2
            while i >= self.y:
                self.canvas.create_line(self.x, i, self.x + 1, i, fill='red')
                self.canvas.create_line(x2, i, x2 + 1, i, fill='red')
                i = i - 1

        if self.y > y2:
            self.pontos_janelas.append(self.x)
            self.pontos_janelas.append(self.y)
            self.pontos_janelas.append(x2)
            self.pontos_janelas.append(y2)
        elif self.y < y2:
            self.pontos_janelas.append(self.x)
            self.pontos_janelas.append(y2)
            self.pontos_janelas.append(x2)
            self.pontos_janelas.append(self.y)
        self.x,self.y = 0,0
        self.desactivate_window()


    def calculo(self,event):
        x2,y2 = event.x, event.y
        bits_inicio = [0,0,0,0]
        bits_final = [0,0,0,0]
        if self.x > self.pontos_janelas[2]:
            bits_inicio[2] = 1
        if self.x < self.pontos_janelas[0]:
            bits_inicio[3] = 1
        if self.y < self.pontos_janelas[3]:
            bits_inicio[0] = 1
        if self.y > self.pontos_janelas[1]:
            bits_inicio[1] = 1

        if x2 > self.pontos_janelas[2]:
            bits_final[2]= 1
        if x2 < self.pontos_janelas[0]:
            bits_final[3] = 1
        if y2 < self.pontos_janelas[3]:
            bits_final[0]= 1
        if y2 > self.pontos_janelas[1]:
            bits_final[1] = 1

        bits_resultado = [0,0,0,0]

        if bits_inicio[0] == 1 and bits_final[0] == 1:
            bits_resultado[0]=1
        if bits_inicio[1] == 1 and bits_final[1] == 1:
            bits_resultado[1]=1
        if bits_inicio[2] == 1 and bits_final[2] == 1:
            bits_resultado[2]=1
        if bits_inicio[3] == 1 and bits_final[3] == 1:
            bits_resultado[3]=1
        apenas_zero = all(valor == 0 for valor in bits_inicio)
        apenas_zero2 = all(valor == 0 for valor in bits_final)
        resultado = all(valor == 0 for valor in bits_resultado)
        pontos_novos = []
        if apenas_zero and apenas_zero2:
            self.parametrica(self.x,self.y,x2,y2)
            return True
        elif resultado and apenas_zero != True or apenas_zero2 != True :
            if apenas_zero:
                left = False
                right = False
                bottom = False
                upper = False
                if bits_final[0] == 1:
                    bottom = True
                if bits_final[1] == 1:
                    upper = True
                if bits_final[2] == 1:
                    right = True
                if bits_final[3] == 1:
                    left = True

                m = (y2 - self.y) / (x2 - self.x)
                if left:
                    y_left = m * (self.pontos_janelas[0] - self.x) + self.y
                    y_real = int(y_left)
                    x_real = self.pontos_janelas[0]
                    pontos_novos.append([x_real, y_real])
                    print('passei left')
                if right:
                    y_right = m * (self.pontos_janelas[2] - self.x) + self.y
                    y_real = int(y_right)
                    x_real = self.pontos_janelas[2]
                    pontos_novos.append([x_real, y_real])
                    print('passei right')
                if upper:
                    x_bottom = ((self.pontos_janelas[1] - self.y) / m) + self.x
                    x_real = int(x_bottom)
                    y_real = self.pontos_janelas[1]
                    pontos_novos.append([x_real, y_real])
                    print('passei upper')
                if bottom:
                    x_top = ((self.pontos_janelas[3] - self.y) / m) + self.x
                    x_real = int(x_top)
                    y_real = self.pontos_janelas[3]
                    pontos_novos.append([x_real, y_real])
                    print('passei bottom')
                self.parametrica(self.x,self.y, pontos_novos[0][0], pontos_novos[0][1])
            elif apenas_zero2:
                left = False
                right = False
                bottom = False
                upper = False
                if bits_inicio[0] == 1:
                    bottom = True
                if bits_inicio[1] == 1:
                    upper = True
                if bits_inicio[2] == 1:
                    right = True
                if bits_inicio[3] == 1:
                    left = True

                m = (y2 - self.y) / (x2 - self.x)
                if left:
                    y_left = m * (self.pontos_janelas[0] - self.x) + self.y
                    y_real = int(y_left)
                    x_real = self.pontos_janelas[0]
                    pontos_novos.append([x_real, y_real])
                    print('passei left')
                if right:
                    y_right = m * (self.pontos_janelas[2] - self.x) + self.y
                    y_real = int(y_right)
                    x_real = self.pontos_janelas[2]
                    pontos_novos.append([x_real, y_real])
                    print('passei right')
                if upper:
                    x_bottom = ((self.pontos_janelas[1] - self.y) / m) + self.x
                    x_real = int(x_bottom)
                    y_real = self.pontos_janelas[1]
                    pontos_novos.append([x_real, y_real])
                    print('passei upper')
                if bottom:
                    x_top = ((self.pontos_janelas[3] - self.y) / m) + self.x
                    x_real = int(x_top)
                    y_real = self.pontos_janelas[3]
                    pontos_novos.append([x_real, y_real])
                    print('passei bottom')
                self.parametrica(x2, y2, pontos_novos[0][0], pontos_novos[0][1])
            else:
                m = (y2-self.y)/(x2-self.x)
                y_left = m * (self.pontos_janelas[0]-self.x) + self.y
                y_right = m * (self.pontos_janelas[2]-self.x) + self.y
                x_bottom = ((self.pontos_janelas[1]-self.y)/m) + self.x
                x_top = ((self.pontos_janelas[3]-self.y)/m) + self.x
                print(y_left,y_right,x_bottom,x_top)
                if self.pontos_janelas[3] <= y_left <= self.pontos_janelas[1]:
                    y_real = int(y_left)
                    x_real = self.pontos_janelas[0]
                    pontos_novos.append([x_real,y_real])
                    print('passei aqui 0')
                if self.pontos_janelas[3] <= y_right <= self.pontos_janelas[1]:
                    y_real = int(y_right)
                    x_real = self.pontos_janelas[2]
                    pontos_novos.append([x_real, y_real])
                    print('passei aqui 1')
                if self.pontos_janelas[0] <= x_top <= self.pontos_janelas[2]:
                    x_real = int(x_top)
                    y_real = self.pontos_janelas[3]
                    pontos_novos.append([x_real, y_real])
                    print('passei aqui 2')
                if self.pontos_janelas[0] <= x_bottom <= self.pontos_janelas[2]:
                    x_real = int(x_bottom)
                    y_real = self.pontos_janelas[1]
                    pontos_novos.append([x_real, y_real])
                    print('passei aqui 3')
                self.parametrica(pontos_novos[0][0],pontos_novos[0][1],pontos_novos[1][0],pontos_novos[1][1])

    def parametrica(self,x,y,x2,y2):
        Vx = x2 - x
        Vy = y2 - y
        t = 0.001
        while t <= 1.0:
            i = int(x + Vx * t)
            j = int(y + Vy * t)
            self.canvas.create_line(i, j, i + 1, j, fill='red')
            t = t + 0.001


if __name__ == "__main__":
    root = tk.Tk()
    editor = Cohen(root)
    root.mainloop()