from tkinter import *

class Application:
    def __init__(self, master=None):
        self.corPdInt = "#DDD3CB" #cor padrão da interface
        self.corPdBotao = "#8C9CB5" #cor padrão dos botões
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master, bg=self.corPdInt)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master, bg=self.corPdInt)
        self.segundoContainer["pady"] = 100

        self.terceiroContainer = Frame(master, bg=self.corPdInt)
        self.terceiroContainer["pady"] = 10

        self.titulo = Label(self.primeiroContainer, text="Bem vindo(a)!", bg=self.corPdInt)
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.pack()
        
        self.lancar_taxas = Button(self.segundoContainer, bg=self.corPdBotao, command=self.segundo_frame)
        self.lancar_taxas["text"] = "Lançar taxas"
        self.lancar_taxas["font"] = ("Calibri", "16")
        self.lancar_taxas["width"] = 12
        self.lancar_taxas["height"] = 4
        
        self.opcoes = Button(self.terceiroContainer, text="Opções", bg=self.corPdBotao)
        self.opcoes["font"] = ("Calibri", "16")
        self.opcoes["width"] = 12
        self.opcoes["height"] = 4
        
        self.atualizar_interface()
        
    def atualizar_interface(self):
        # Destruir os widgets do primeiro container
        for widget in self.primeiroContainer.winfo_children():
            widget.destroy()
        
        # Empacotar o primeiro container
        self.primeiroContainer.pack()
        
        # Adicionar widgets ao primeiro container
        self.titulo.pack()
        self.lancar_taxas.pack()
        self.opcoes.pack()
        
    def segundo_frame(self):
        # Destruir os widgets do segundo container
        for widget in self.segundoContainer.winfo_children():
            widget.destroy()
        
        # Ocultar o primeiro container e o terceiro container
        self.primeiroContainer.pack_forget()
        self.terceiroContainer.pack_forget()
        
        # Atualizar o texto do título
        self.titulo["text"] = "Lançar Taxas"
        
        # Adicionar novos containers
        novo_container1 = Frame(self.segundoContainer, bg=self.corPdInt)
        novo_container1["pady"] = 20
        novo_container1.pack()
        
        novo_container2 = Frame(self.segundoContainer, bg=self.corPdInt)
        novo_container2["pady"] = 100
        novo_container2.pack()
        
        novo_container3 = Frame(self.segundoContainer, bg=self.corPdInt)
        novo_container3["pady"] = 10
        novo_container3.pack()
        
        # Adicionar widgets aos novos containers
        label2 = Label(novo_container2, text="Container 2")
        label2.pack()
        
        label3 = Label(novo_container3, text="Container 3")
        label3.pack()

root = Tk()
root.geometry("800x600")
root.configure(bg="#DDD3CB")
app = Application(root)
root.mainloop()
