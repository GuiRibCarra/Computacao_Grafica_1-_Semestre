import math
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps, ImageDraw


class ImageEditor:
    def __init__(self, root):
        self.root = root

        self.root.title("Editor de Imagens")

        self.menubar = tk.Menu(root)
        img_menu = tk.Menu(self.menubar, tearoff=0)
        img_menu.add_command(label="Carregar", command=self.load_image)
        img_menu.add_command(label="Negativo", command=self.apply_negative)
        img_menu.add_command(label="Desenhar", command=self.activate_drawing)
        self.menubar.add_cascade(label="Imagem", menu=img_menu)
        
        
        retas_menu = tk.Menu(self.menubar, tearoff=0)
        retas_menu.add_command(label="Reta: y = ax+b", command=self.activate_retas_y)
        retas_menu.add_command(label="Reta: Parametrica", command=self.activate_retas_p)
        retas_menu.add_command(label="Circulo: y=raiz(r2-x2)", command=self.activate_retas_c_y)
        retas_menu.add_command(label="Circulo: Parametrica", command=self.activate_retas_c_p)
        self.menubar.add_cascade(label="Pixels", menu=retas_menu)

        breseham_menu = tk.Menu(self.menubar, tearoff=0)
        breseham_menu.add_command(label="Retas", command=self.activate_retas_b)
        breseham_menu.add_command(label="Circunferencias", command=self.activate_circ_b)
        self.menubar.add_cascade(label="Breseham", menu=breseham_menu)
        
        self.root.config(menu = self.menubar)

        # Área de desenho
        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()

        # Variável para armazenar a imagem
        self.image = None
        self.photo = None
        self.canvas_image = None
        self.draw = None
        self.drawing = False
        self.retas = False
        self.x = 0
        self.y = 0
        self.x2 = 0
        self.y2 = 0

    def load_image(self):
        # Carregar uma imagem
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path).convert("RGB")
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.config(width=self.image.width, height=self.image.height)
            self.canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.draw = ImageDraw.Draw(self.image)

    def apply_negative(self):
        if self.image:
            # Aplicar efeito negativo
            self.image = ImageOps.invert(self.image)
            self.drawing = False
            self.update_canvas()


    def activate_drawing(self):
        if self.image:
            self.drawing = True
            self.canvas.bind("<B1-Motion>", self.draw_on_image)

    def get_x1_y1(self, event):
        if self.retas:
            self.x, self.y = event.x, event.y

    def activate_retas_y(self):
        if self.image:
            self.retas = True
            self.canvas.bind("<Button-1>", self.get_x1_y1)
            self.canvas.bind("<ButtonRelease-1>", self.y_a_b)

    def y_a_b(self, event):
        if self.retas:
            self.x2, self.y2 = event.x, event.y
            print(self.x2, self.y2)
            m = (self.y2-self.y)/(self.x2-self.x)
            dx = abs(self.x2-self.x)
            dy = abs(self.y2-self.y)
            if dx > dy:
                if self.x < self.x2:
                    i = self.x
                    while i != self.x2:
                        j = int(m * (i - self.x) + self.y)
                        self.image.putpixel((i, j), (255, 0, 0))
                        i = i + 1
                elif self.x2 < self.x:
                    i = self.x
                    while i != self.x2:
                        j = int(m * (i - self.x) + self.y)
                        self.image.putpixel((i, j), (255, 0, 0))
                        i = i - 1
            elif dy > dx:
                if self.y < self.y2:
                    i = self.y
                    while i != self.y2:
                        j = int((i - self.y)/m+self.x)
                        self.image.putpixel((j, i), (255, 0, 0))
                        i = i + 1
                elif self.y2 < self.y:
                    i = self.y
                    while i != self.y2:
                        j = int((i - self.y)/m+self.x)
                        self.image.putpixel((j, i), (255, 0, 0))
                        i = i - 1
            self.update_canvas()


    def activate_retas_p(self):
        if self.image:
            self.retas = True
            self.canvas.bind("<Button-1>", self.get_x1_y1)
            self.canvas.bind("<ButtonRelease-1>", self.parametrica)

    def parametrica(self, event):
        if self.retas:
            self.x2, self.y2 = event.x, event.y
            Vx = self.x2 - self.x
            Vy = self.y2 - self.y
            t = 0.001
            while t <= 1.0:
                i = int(self.x + Vx * t)
                j = int(self.y + Vy * t)
                print(i,j,t)
                self.image.putpixel((i, j), (255, 0, 0))
                t = t + 0.001
            self.update_canvas()

    def activate_retas_c_y(self):
        if self.image:
            self.retas = True
            self.canvas.bind("<Button-1>", self.get_x1_y1)
            self.canvas.bind("<ButtonRelease-1>", self.c_y_a_b)

    def c_y_a_b(self, event):
        if self.retas:
            self.x2, self.y2 = event.x, event.y
            raio = round(math.sqrt((self.x2-self.x)**2+(self.y2-self.y)**2))
            for x in range(int(-raio), int(raio)):
                y = math.sqrt(raio ** 2 - x ** 2)
                self.image.putpixel((int(x) + self.x, int(y) + self.y), (255, 0, 0))
                self.image.putpixel((int(x) + self.x, -int(y) + self.y), (255, 0, 0))
                self.image.putpixel((-int(x) + self.x, int(y) + self.y), (255, 0, 0))
                self.image.putpixel((-int(x) + self.x, -int(y) + self.y), (255, 0, 0))
            self.update_canvas()

    def activate_retas_c_p(self):
        if self.image:
            self.retas = True
            self.canvas.bind("<Button-1>", self.get_x1_y1)
            self.canvas.bind("<ButtonRelease-1>", self.c_parametrica)

    def calcular_numero_de_pontos(self,r, distancia_entre_pontos):
        circunferencia = 2 * math.pi * r  # Cálculo da circunferência
        pontos = int(circunferencia / distancia_entre_pontos)  # Número de pontos
        return pontos

    def c_parametrica(self, event):
        if self.retas:
            self.x2, self.y2 = event.x, event.y
            raio = round(math.sqrt((self.x2 - self.x) ** 2 + (self.y2 - self.y) ** 2))
            pontos = self.calcular_numero_de_pontos(raio, 1)
            for a in range(0, pontos):
                theta = 2 * math.pi * a / pontos
                x = raio * math.cos(theta)
                y = raio * math.sin(theta)
                self.image.putpixel((int(x) + self.x, int(y) + self.y), (255, 0, 0))
            self.update_canvas()

    def activate_retas_b(self):
        if self.image:
            self.retas = True
            self.canvas.bind("<Button-1>", self.get_x1_y1)
            self.canvas.bind("<ButtonRelease-1>", self.r_bresenham)

    def bresenham(self,x0, y0, x1, y1):
        # Lista para armazenar as coordenadas
        pontos = []

        # Definindo o delta entre os pontos
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        # Definindo a direção da linha
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1

        # Inicializando o erro
        err = dx - dy

        while True:
            # Adiciona o ponto atual (x0, y0) à lista de pontos
            pontos.append((x0, y0))

            # Se chegou no ponto final, sai do loop
            if x0 == x1 and y0 == y1:
                break

            # Calcula o erro duplo
            e2 = 2 * err

            # Ajusta as coordenadas baseadas no erro
            if e2 > -dy:
                err -= dy
                x0 += sx

            if e2 < dx:
                err += dx
                y0 += sy

        return pontos

    def r_bresenham(self, event):
        if self.retas:
            self.x2, self.y2 = event.x, event.y
            pontos = self.bresenham(self.x,self.y,self.x2,self.y2)
            for i in range(len(pontos)):
                x = pontos[i][0]
                y = pontos[i][1]
                self.image.putpixel((int(x), int(y)), (255, 0, 0))
            self.update_canvas()

    def activate_circ_b(self):
        if self.image:
            self.retas = True
            self.canvas.bind("<Button-1>", self.get_x1_y1)
            self.canvas.bind("<ButtonRelease-1>", self.b_circunferencia)

    def bresenham_circunferencia(self,cx, cy, raio):
        # Lista para armazenar os pontos da circunferência
        pontos = []

        # Coordenadas iniciais
        x = 0
        y = raio
        d = 3 - 2 * raio  # Decisão inicial

        # Função para adicionar os 8 pontos simétricos
        def adicionar_pontos_simetricos(cx, cy, x, y):
            pontos.append((cx + x, cy + y))
            pontos.append((cx - x, cy + y))
            pontos.append((cx + x, cy - y))
            pontos.append((cx - x, cy - y))
            pontos.append((cx + y, cy + x))
            pontos.append((cx - y, cy + x))
            pontos.append((cx + y, cy - x))
            pontos.append((cx - y, cy - x))

        # Calcula e adiciona os pontos
        while x <= y:
            # Adiciona os 8 pontos simétricos
            adicionar_pontos_simetricos(cx, cy, x, y)

            # Atualiza a decisão e os valores de x e y
            if d < 0:
                d = d + 4 * x + 6
            else:
                d = d + 4 * (x - y) + 10
                y -= 1
            x += 1

        return pontos

    def b_circunferencia(self, event):
        if self.retas:
            self.x2, self.y2 = event.x, event.y
            raio = round(math.sqrt((self.x2 - self.x) ** 2 + (self.y2 - self.y) ** 2))
            pontos = self.bresenham_circunferencia(self.x,self.y,raio)
            for i in range(len(pontos)):
                x = pontos[i][0]
                y = pontos[i][1]
                self.image.putpixel((int(x), int(y)), (255, 0, 0))
            self.update_canvas()

    def draw_on_image(self, event):
        if self.drawing:
            x, y = event.x, event.y
            self.draw.ellipse([x - 5, y - 5, x + 5, y + 5], fill="red", outline="red")
            self.update_canvas()

    def apply_pixel(self):
        if self.image:
            # Coordenadas do pixel que deseja alterar (ex: pixel na posição (100, 100))
            x, y = 100, 100

            # Cor para pintar o pixel (ex: vermelho)
            color = (255, 0, 0)
            while x != 200:
                while y != 200:
                    # Aplicar cor ao pixel na posição (x, y)
                    self.image.putpixel((x, y), color)
                    y = y+1
                x = x+1
            # Atualizar o Canvas com a nova imagem
            self.update_canvas()

    def update_canvas(self):
        self.photo = ImageTk.PhotoImage(self.image)  # Atualiza a imagem para o formato PhotoImage
        self.canvas.itemconfig(self.canvas_image, image=self.photo)  # Atualiza a imagem no Canvas
        self.canvas.image = self.photo  # Mantém a referência da imagem para não ser removida pelo garbage collector

if __name__ == "__main__":
    root = tk.Tk()
    editor = ImageEditor(root)
    root.mainloop()