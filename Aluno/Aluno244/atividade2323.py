import tkinter as tk

def realizar_cadastro():
    print(entry_nome.get(), entry_idade.get(), entry_email.get(), entry_endereço.get(), entry_celular.get(), entry_cep.get(), entry_cidade.get(), entry_cursos.get())
    # nome = entry_nome.get()
    # idade = entry_idade.get()
    # email = entry_email.get()
    # endereço = entry_endereço.get()
    # celular = entry_celular.get()
    # cep = entry_cep.get()
    # cidade = entry_cidade.get()
    # curso = entry_cursos.get()



janela  = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("1700x750")
janela.configure(bg='#f0f0f0')

pad_y = 5
pad_x = 10

tk.Label(janela, text="Nome Completo: ", bg="#f0f0f0").pack(anchor='w', padx=pad_x)
entry_nome = tk.Entry(janela, width=50)
entry_nome.pack(padx=pad_x, pady=(0, pad_y))

tk.Label(janela, text="Idade: ", bg="#f0f0f0").pack(anchor='w', padx=pad_x)
entry_idade = tk.Entry(janela, width=50)
entry_idade.pack(padx=pad_x, pady=(0, pad_y))

tk.Label(janela, text="Email: ", bg="#f0f0f0").pack(anchor='w', padx=pad_x)
entry_email = tk.Entry(janela, width=50)
entry_email.pack(padx=pad_x, pady=(0, pad_y))

tk.Label(janela, text="Endereço: ", bg="#f0f0f0").pack(anchor='w', padx=pad_x)
entry_endereço = tk.Entry(janela, width=80)
entry_endereço.pack(padx=pad_x, pady=(0, pad_y))

tk.Label(janela, text="Celular: ", bg="#f0f0f0").pack(anchor='w', padx=pad_x)
entry_celular = tk.Entry(janela, width=50)
entry_celular.pack(padx=pad_x, pady=(0, pad_y))

tk.Label(janela, text="CEP: ", bg="#f0f0f0").pack(anchor='w', padx=pad_x)
entry_cep = tk.Entry(janela, width=50)
entry_cep.pack(padx=pad_x, pady=(0, pad_y))

tk.Label(janela, text="Cidade: ", bg="#f0f0f0").pack(anchor='w', padx=pad_x)
entry_cidade = tk.Entry(janela, width=80)
entry_cidade.pack(padx=pad_x, pady=(0, pad_y))

tk.Label(janela, text="Cursos: ", bg="#f0f0f0").pack(anchor='w', padx=pad_x)
entry_cursos = tk.Entry(janela, width=80)
entry_cursos.pack(padx=pad_x, pady=(0, pad_y))

btn_enviar = tk.Button(janela, text="Enviar", command=realizar_cadastro, bg='#4CAF50', fg="white", font=("Arial", 10, 'bold'))
btn_enviar.pack(pady=50)

janela.mainloop()

