import tkinter as tk

janela  = tk.Tk()
janela.configure(bg = '#DCD7D7')

tk.Label(janela, text='FORMULARIO', bg = '#DCD7D7',font=('Montserrat', 12) ).grid(row=1, column=2, pady=20)

fr1 =  tk.Frame(janela, bg = '#DCD7D7')
fr1.grid(columnspan=2)

