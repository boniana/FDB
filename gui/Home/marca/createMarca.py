import tkinter as tk
from models.entitys import Marca

class CreateMarca(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.marca_controller = self.controller.myController.marcaController()
        
        self.nome_var = tk.StringVar()
        
        tk.Label(self, text="Cadastrar Marca", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="Nome:", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.nome_var, width=30 ).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Button(self, text="Cadastrar", command=self.cadastrar, width=25 ).grid(row=6, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=7, column=0, columnspan=4, pady=10)
    
    def cadastrar(self):
        try:
            marca = Marca(nome = self.nome_var.get())
            if self.marca_controller.create(marca):
                tk.messagebox.showinfo("Sucesso", "Marca cadastrada com sucesso!")
                self.nome_var.set("")
            else:
                tk.messagebox.showerror("Erro", "Erro ao cadastrar marca!")
            
        except Exception as e:
            tk.messagebox.showerror("Erro", e)
        
        