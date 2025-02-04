import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    nome = entrada.get()
    messagebox.showinfo("Saudação", f"Olá, {nome}!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Meu Aplicativo")
janela.geometry("300x200")

# Criar um rótulo
rotulo = tk.Label(janela, text="Digite seu nome:")
rotulo.pack(pady=10)

# Criar um campo de entrada
entrada = tk.Entry(janela)
entrada.pack(pady=10)

# Criar um botão
botao = tk.Button(janela, text="Saudar", command=mostrar_mensagem)
botao.pack(pady=10)

# Iniciar o loop da interface
janela.mainloop()