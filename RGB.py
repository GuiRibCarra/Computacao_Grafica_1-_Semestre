import tkinter as tk
from tkinter import messagebox
from colorsys import rgb_to_hls, hls_to_rgb

# Função para converter RGB para HSL
def rgb_to_hsl(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, l, s = rgb_to_hls(r, g, b)
    h = h * 360
    s = s * 100
    l = l * 100
    return round(h, 2), round(s, 2), round(l, 2)

# Função para converter HSL para RGB
def hsl_to_rgb(h, s, l):
    h, s, l = h / 360.0, s / 100.0, l / 100.0
    r, g, b = hls_to_rgb(h, l, s)
    r, g, b = round(r * 255), round(g * 255), round(b * 255)
    return r, g, b

# Função para realizar a conversão de RGB para HSL
def convert_rgb_to_hsl():
    try:
        r = int(entry_r.get())
        g = int(entry_g.get())
        b = int(entry_b.get())
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError
        h, s, l = rgb_to_hsl(r, g, b)
        label_result_hsl.config(text=f'HSL: {h}°, {s}%, {l}%')
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para RGB (0-255).")

# Função para realizar a conversão de HSL para RGB
def convert_hsl_to_rgb():
    try:
        h = float(entry_h.get())
        s = float(entry_s.get())
        l = float(entry_l.get())
        if not (0 <= h <= 360 and 0 <= s <= 100 and 0 <= l <= 100):
            raise ValueError
        r, g, b = hsl_to_rgb(h, s, l)
        label_result_rgb.config(text=f'RGB: {r}, {g}, {b}')
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para HSL (0-360 para H e 0-100 para S e L).")

# Configuração da janela principal
root = tk.Tk()
root.title("Conversor RGB para HSL e HSL para RGB")
root.geometry("400x300")  # Definir tamanho da janela

# Seção para conversão de RGB para HSL
label_rgb = tk.Label(root, text="RGB para HSL")
label_rgb.grid(row=0, columnspan=2)

label_r = tk.Label(root, text="R:")
label_r.grid(row=1, column=0)
entry_r = tk.Entry(root)
entry_r.grid(row=1, column=1)

label_g = tk.Label(root, text="G:")
label_g.grid(row=2, column=0)
entry_g = tk.Entry(root)
entry_g.grid(row=2, column=1)

label_b = tk.Label(root, text="B:")
label_b.grid(row=3, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=3, column=1)

button_convert_rgb = tk.Button(root, text="Converter para HSL", command=convert_rgb_to_hsl)
button_convert_rgb.grid(row=4, columnspan=2)

label_result_hsl = tk.Label(root, text="HSL:")
label_result_hsl.grid(row=5, columnspan=2)

# Seção para conversão de HSL para RGB
label_hsl = tk.Label(root, text="HSL para RGB")
label_hsl.grid(row=6, columnspan=2)

label_h = tk.Label(root, text="H:")
label_h.grid(row=7, column=0)
entry_h = tk.Entry(root)
entry_h.grid(row=7, column=1)

label_s = tk.Label(root, text="S:")
label_s.grid(row=8, column=0)
entry_s = tk.Entry(root)
entry_s.grid(row=8, column=1)

label_l = tk.Label(root, text="L:")
label_l.grid(row=9, column=0)
entry_l = tk.Entry(root)
entry_l.grid(row=9, column=1)

button_convert_hsl = tk.Button(root, text="Converter para RGB", command=convert_hsl_to_rgb)
button_convert_hsl.grid(row=10, columnspan=2)

label_result_rgb = tk.Label(root, text="RGB:")
label_result_rgb.grid(row=11, columnspan=2)

# Iniciar a interface gráfica
root.mainloop()