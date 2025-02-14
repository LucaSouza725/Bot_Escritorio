import customtkinter
import subprocess
import sys
import os
from PIL import Image

# Variável global para controle do processo
processo = None
janela_parar = None

# Caminho das imagens
imagem_iniciar_path = r"C:/Projeto/Meu_projeto/resources/imagens/botao-play.png"
imagem_pausar_path = r"C:/Projeto/Meu_projeto/resources/imagens/botao-pausa.png"

# Iniciando imagens
imagem_iniciar = customtkinter.CTkImage(
    light_image=Image.open(imagem_iniciar_path),
    dark_image=Image.open(imagem_iniciar_path),
    size=(30, 30)
)

imagem_pausar = customtkinter.CTkImage(
    light_image=Image.open(imagem_pausar_path),
    dark_image=Image.open(imagem_pausar_path),
    size=(30, 30)
)

# Função para iniciar a main.py


def iniciar_main():
    # Adicionando global para que a variável seja reconhecida corretamente
    global processo, janela_parar
    if processo is None:
        processo = subprocess.Popen(["python", "src/main.py"])
        app.iconify()

        # Criar uma janela pequena com botão "PARAR"
        janela_parar = customtkinter.CTkToplevel(app)
        janela_parar.geometry("190x80+820+0")
        janela_parar.title("Parar")
        janela_parar.resizable(False, False)
        janela_parar.attributes("-topmost", True)

        botao_parar = customtkinter.CTkButton(
            janela_parar, text="PARAR", fg_color="#a83232", image=imagem_pausar, font=("Arial", 15),
            command=parar_main
        )
        botao_parar.pack(pady=20)

        # Manter janela sempre visível
        def manter_topo():
            global janela_parar  # Adicionando global aqui também
            if processo is not None and janela_parar is not None:
                janela_parar.lift()
                janela_parar.attributes("-topmost", True)
                janela_parar.after(500, manter_topo)

        manter_topo()

# Função para parar a main.py


def parar_main():
    global processo, janela_parar
    if processo is not None:
        processo.terminate()  # Encerra o processo
        processo = None  # Reseta a variável

        # Fechar a janela "PARAR"
        if janela_parar is not None:
            janela_parar.destroy()
            janela_parar = None

        # Restaurar a tela principal
        app.deiconify()


# Configuração da interface principal
customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.geometry("800x500")
app.title("Lançamento Automático na BIOS")

# Criando o Título:
titulo = customtkinter.CTkLabel(
    app, text="Lançamentos Automáticos", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

# Botão para iniciar
titulo_botao_iniciar = customtkinter.CTkLabel(
    app, text="Iniciar programa", font=("Arial", 20))
titulo_botao_iniciar.pack(pady=(50, 0))

botao_iniciar = customtkinter.CTkButton(
    app, text="INICIAR", fg_color="#1c5052", image=imagem_iniciar, font=("Arial", 15), command=iniciar_main
)
botao_iniciar.pack(pady=20)

# Botão para parar
titulo_botao_parar = customtkinter.CTkLabel(
    app, text="Parar programa", font=("Arial", 20))
titulo_botao_parar.pack(pady=(50, 0))

botao_parar = customtkinter.CTkButton(
    app, text="PARAR", fg_color="#1c5052", image=imagem_pausar, font=("Arial", 15), command=parar_main
)
botao_parar.pack(pady=20)

app.mainloop()
