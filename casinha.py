import math
import tkinter as tk
import numpy as np


class OP_Casinha:
    def __init__(self, root):
        self.root = root
        self.pontos = [[300,450],[300,400],[350,450],[350,400],[325,375],[370,430],[370,380],[420,430],[420,380],[395,355]]
        self.retas = [(0,1),(1,4),(4,3),(3,2),(2,0),(5,6),(6,9),(9,8),(8,7),(7,5),(0,5),(1,6),(4,9),(3,8),(2,7)]

        self.root.title("Casinha")
        self.canvas = tk.Canvas(root, width=700, height=700, bg="black")
        self.canvas.grid(row = 0, column = 0, sticky = tk.W)

        self.frame = tk.Frame(root, width=400, height=400)
        self.frame.grid(row=0, column=1, padx=5, pady=5)

        self.var = tk.IntVar()

        self.escala = tk.Label(self.frame, text='Escala')
        self.x_e = tk.Label(self.frame, text='X')
        self.y_e = tk.Label(self.frame, text='Y')
        self.z_e = tk.Label(self.frame, text='Z')

        self.R_l = tk.Radiobutton(self.frame, text="Local", value=0,variable=self.var)
        self.R_g = tk.Radiobutton(self.frame, text="Global", value=1,variable=self.var)

        self.E_x_l = tk.Entry(self.frame, bd=3,width=5)
        self.E_y_l = tk.Entry(self.frame, bd=3,width=5)
        self.E_z_l = tk.Entry(self.frame, bd=3,width=5)
        self.E_g = tk.Entry(self.frame, bd=3, width=5)

        self.escala.grid(row=0, column=0,padx = 10,pady = 10)
        self.x_e.grid(row=0, column=1,padx = 10,pady = 10)
        self.y_e.grid(row=0, column=2,padx = 10,pady = 10)
        self.z_e.grid(row=0, column=3,padx = 10,pady = 10)
        self.R_l.grid(row=1, column=0, padx=10, pady=10)
        self.R_g.grid(row=2, column=0, padx=10, pady=10)
        self.E_x_l.grid(row=1, column=1, padx=10, pady=10)
        self.E_y_l.grid(row=1, column=2, padx=10, pady=10)
        self.E_z_l.grid(row=1, column=3, padx=10, pady=10)
        self.E_g.grid(row=2, column=1, padx=10, pady=10)

        self.translacao = tk.Label(self.frame, text='Translação')
        self.x_t = tk.Label(self.frame, text='X')
        self.y_t = tk.Label(self.frame, text='Y')
        self.z_t = tk.Label(self.frame, text='Z')

        self.R_t = tk.Radiobutton(self.frame, text="", value=2,variable=self.var)

        self.E_x_t = tk.Entry(self.frame, bd=3, width=5)
        self.E_y_t = tk.Entry(self.frame, bd=3, width=5)
        self.E_z_t = tk.Entry(self.frame, bd=3, width=5)

        self.translacao.grid(row=3, column=0,padx = 10,pady = 10)
        self.x_t.grid(row=3, column=1,padx = 10,pady = 10)
        self.y_t.grid(row=3, column=2,padx = 10,pady = 10)
        self.z_t.grid(row=3, column=3,padx = 10,pady = 10)
        self.R_t.grid(row=4, column=0, padx=10, pady=10)
        self.E_x_t.grid(row=4, column=1, padx=10, pady=10)
        self.E_y_t.grid(row=4, column=2, padx=10, pady=10)
        self.E_z_t.grid(row=4, column=3, padx=10, pady=10)

        self.rotacao = tk.Label(self.frame, text='Rotação')
        self.r_eixo = tk.Label(self.frame, text='Eixo')
        self.r_graus= tk.Label(self.frame, text='Graus')

        self.R_r_o = tk.Radiobutton(self.frame, text="Origem", value=3,variable=self.var)
        self.R_r_c = tk.Radiobutton(self.frame, text="Centro do Objeto", value=4,variable=self.var)

        self.E_e = tk.Entry(self.frame, bd=3, width=5)
        self.E_r_g = tk.Entry(self.frame, bd=3, width=5)

        self.rotacao.grid(row=5, column=0, padx=10, pady=10)
        self.r_eixo.grid(row=6, column=2, padx=10, pady=10)
        self.r_graus.grid(row=7, column=2, padx=10, pady=10)
        self.R_r_o.grid(row=6, column=0, padx=10, pady=10)
        self.R_r_c.grid(row=7, column=0, padx=10, pady=10)
        self.E_e.grid(row=6, column=3, padx=10, pady=10)
        self.E_r_g.grid(row=7, column=3, padx=10, pady=10)

        self.frame_sh = tk.Frame(self.frame, width=100, height=100)
        self.frame_sh.grid(row=8, column=0, padx=5, pady=5)

        self.sh = tk.Label(self.frame_sh, text='Shearing')

        self.R_sh = tk.Radiobutton(self.frame_sh, text="", value=5,variable=self.var)

        valor_0 = tk.StringVar()
        valor_0.set('0')

        valor_1 = tk.StringVar()
        valor_1.set('1')

        self.E_sh_0 = tk.Entry(self.frame_sh, bd=3, width=5, textvariable=valor_1, state='readonly')
        self.E_sh_1 = tk.Entry(self.frame_sh, bd=3, width=5)
        self.E_sh_2 = tk.Entry(self.frame_sh, bd=3, width=5)
        self.E_sh_3 = tk.Entry(self.frame_sh, bd=3, width=5, textvariable=valor_0, state='readonly')

        self.E_sh_4 = tk.Entry(self.frame_sh, bd=3, width=5)
        self.E_sh_5 = tk.Entry(self.frame_sh, bd=3, width=5, textvariable=valor_1, state='readonly')
        self.E_sh_6 = tk.Entry(self.frame_sh, bd=3, width=5)
        self.E_sh_7 = tk.Entry(self.frame_sh, bd=3, width=5, textvariable=valor_0, state='readonly')

        self.E_sh_8 = tk.Entry(self.frame_sh, bd=3, width=5)
        self.E_sh_9 = tk.Entry(self.frame_sh, bd=3, width=5)
        self.E_sh_10 = tk.Entry(self.frame_sh, bd=3, width=5, textvariable=valor_1, state='readonly')
        self.E_sh_11 = tk.Entry(self.frame_sh, bd=3, width=5, textvariable=valor_0, state='readonly')

        self.E_sh_12 = tk.Entry(self.frame_sh, bd=3, width=5, textvariable=valor_0, state='readonly')
        self.E_sh_13 = tk.Entry(self.frame_sh, bd=3, width=5, textvariable=valor_0, state='readonly')
        self.E_sh_14 = tk.Entry(self.frame_sh, bd=3, width=5, textvariable=valor_0, state='readonly')
        self.E_sh_15 = tk.Entry(self.frame_sh, bd=3, width=5, textvariable=valor_1, state='readonly')

        self.sh.grid(row=0, column=0, padx=5, pady=5)
        self.R_sh.grid(row=1, column=0, padx=5, pady=5)

        self.E_sh_0.grid(row=1, column=1, padx=5, pady=5)
        self.E_sh_1.grid(row=1, column=2, padx=5, pady=5)
        self.E_sh_2.grid(row=1, column=3, padx=5, pady=5)
        self.E_sh_3.grid(row=1, column=4, padx=5, pady=5)

        self.E_sh_4.grid(row=2, column=1, padx=5, pady=5)
        self.E_sh_5.grid(row=2, column=2, padx=5, pady=5)
        self.E_sh_6.grid(row=2, column=3, padx=5, pady=5)
        self.E_sh_7.grid(row=2, column=4, padx=5, pady=5)

        self.E_sh_8.grid(row=3, column=1, padx=5, pady=5)
        self.E_sh_9.grid(row=3, column=2, padx=5, pady=5)
        self.E_sh_10.grid(row=3, column=3, padx=5, pady=5)
        self.E_sh_11.grid(row=3, column=4, padx=5, pady=5)

        self.E_sh_12.grid(row=4, column=1, padx=5, pady=5)
        self.E_sh_13.grid(row=4, column=2, padx=5, pady=5)
        self.E_sh_14.grid(row=4, column=3, padx=5, pady=5)
        self.E_sh_15.grid(row=4, column=4, padx=5, pady=5)

        self.executa = tk.Button(self.frame, text ="EXECUTAR",command=self.mostrar_selecao)
        self.zerar = tk.Button(self.frame, text ="Limpar casa",command=self.pontos_iniciais)

        self.executa.grid(row=8, column=3, padx=5, pady=5)
        self.zerar.grid(row=8, column=2, padx=5, pady=5)
        self.desenhar_casinha()

    def pontos_iniciais(self):
        self.pontos = [[300,450],[300,400],[350,450],[350,400],[325,375],[370,430],[370,380],[420,430],[420,380],[395,355]]
        self.desenhar_casinha()

    def desenhar_casinha(self):
        self.canvas.delete('all')
        for i in range(len(self.pontos)):
            self.canvas.create_rectangle(self.pontos[i][0], self.pontos[i][1], self.pontos[i][0] + 1, self.pontos[i][1]
                                         +1, outline="green", fill="green")
            self.parametrica()

    def parametrica(self):
        for a in range(len(self.retas)):
            Vx = self.pontos[self.retas[a][1]][0] - self.pontos[self.retas[a][0]][0]
            Vy = self.pontos[self.retas[a][1]][1] - self.pontos[self.retas[a][0]][1]
            t = 0.001
            while t <= 1.0:
                i = int(self.pontos[self.retas[a][0]][0] + Vx * t)
                j = int(self.pontos[self.retas[a][0]][1] + Vy * t)
                self.canvas.create_rectangle(i,j, i + 1, j + 1, outline="green", fill="green")
                t = t + 0.001

    def op_translacao(self,x,y):
        for i in range(len(self.pontos)):
            self.pontos[i][0] = int(self.pontos[i][0] + x)
            self.pontos[i][1] = int(self.pontos[i][1] + y)
        self.desenhar_casinha()

    def op_escala_local(self,x,y):
        pivox = self.pontos[0][0]
        pivoy =self.pontos[0][1]
        for i in range(len(self.pontos)):
            self.pontos[i][0] = int(self.pontos[i][0] * x)
            self.pontos[i][1] = int(self.pontos[i][1] * y)
        x_t = pivox - self.pontos[0][0]
        y_t = pivoy - self.pontos[0][1]
        self.op_translacao(x_t,y_t)

    def op_escala_global(self,g):
        pivox = self.pontos[0][0]
        pivoy = self.pontos[0][1]
        for i in range(len(self.pontos)):
            self.pontos[i][0] = int(self.pontos[i][0] * g)
            self.pontos[i][1] = int(self.pontos[i][1] * g)
        x_t = pivox - self.pontos[0][0]
        y_t = pivoy - self.pontos[0][1]
        self.op_translacao(x_t,y_t)



    def get_matriz_rotacao(self, eixo, graus):
        radiano = math.radians(graus)
        cos = math.cos(radiano)
        sin = math.sin(radiano)
        matriz_rotacao = []
        if eixo == 'x' or eixo == 'X':
            matriz_rotacao.append([cos,-sin])
            matriz_rotacao.append([sin, cos])
        elif eixo == 'y' or eixo == 'Y':
            matriz_rotacao.append([cos, sin])
            matriz_rotacao.append([-sin, cos])
        return matriz_rotacao

    def rotacao_graus(self, eixo, graus):
        matriz = np.array(self.get_matriz_rotacao(eixo,graus))
        pivox = self.pontos[0][0]
        pivoy = self.pontos[0][1]
        self.op_translacao(-pivox,-pivoy)

        for i in range(len(self.pontos)):
            array = np.array(self.pontos[i])
            self.pontos[i] = array @ matriz

        self.op_translacao(pivox,pivoy)

    def rotacao_centro(self, eixo, graus):
        matriz = np.array(self.get_matriz_rotacao(eixo,graus))
        pivox = 0
        pivoy = 0
        num_pontos = len(self.pontos)
        for i in range(len(self.pontos)):
            pivox = self.pontos[i][0] + pivox
            pivoy = self.pontos[i][1] + pivoy

        pivox = int(pivox / num_pontos)
        pivoy = int(pivoy / num_pontos)
        self.op_translacao(-pivox,-pivoy)

        for i in range(len(self.pontos)):
            array = np.array(self.pontos[i])
            self.pontos[i] = array @ matriz

        self.op_translacao(pivox,pivoy)

    def shearing(self,elem1,elem2,elem3,elem4,elem5,elem6):
        matriz = np.array([[1, elem1, elem2],
                           [elem3, 1, elem4],
                           [elem5, elem6, 1]])
        pivox = self.pontos[0][0]
        pivoy = self.pontos[0][1]
        for i in range(len(self.pontos)):
            array = np.array([self.pontos[i][0], self.pontos[i][1], 1])
            calculo = array @ matriz
            self.pontos[i] = [calculo[0],calculo[1]]
            print(self.pontos[i])

        self.op_translacao(pivox-self.pontos[0][0], pivoy-self.pontos[0][1])

    def mostrar_selecao(self):
        selecao = self.var.get()
        if selecao == 0:
            x_get = self.E_x_l.get()
            y_get = self.E_y_l.get()
            x_i = float(x_get)
            y_i = float(y_get)
            self.op_escala_local(x_i, y_i)
        elif selecao == 1:
            v_global = float(self.E_g.get())
            self.op_escala_global(v_global)
        elif selecao == 2:
            x_get = self.E_x_t.get()
            y_get = self.E_y_t.get()
            x_i = int(x_get)
            y_i = int(y_get)
            self.op_translacao(x_i,-y_i)
        elif selecao == 3:
            eixo = str(self.E_e.get())
            graus = float(self.E_r_g.get())
            self.rotacao_graus(eixo,graus)
        elif selecao == 4:
            eixo = str(self.E_e.get())
            graus = float(self.E_r_g.get())
            self.rotacao_centro(eixo, graus)
        elif selecao == 5:
            elem1 = float(self.E_sh_1.get())
            elem2 = float(self.E_sh_2.get())
            elem3 = float(self.E_sh_4.get())
            elem4 = float(self.E_sh_6.get())
            elem5 = float(self.E_sh_8.get())
            elem6 = float(self.E_sh_9.get())
            self.shearing(elem1,elem2,elem3,elem4,elem5,elem6)


if __name__ == "__main__":
    root = tk.Tk()
    editor = OP_Casinha(root)
    root.mainloop()