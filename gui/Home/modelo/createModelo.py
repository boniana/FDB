import tkinter as tk
from models.entitys import Modelo

class CreateModelo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.modelo_controller = self.controller.myController.modeloController()
        
        self.nome_var = tk.StringVar()
        self.idMarca_var = tk.StringVar()
        
        tk.Label(self, text="Cadastrar Marca", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="Nome:", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.nome_var, width=30 ).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Id da Marca:", anchor="w").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.idMarca_var, width=30 ).grid(row=2, column=1, padx=10, pady=5)
        
        tk.Button(self, text="Cadastrar", command=self.cadastrar, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)
        
    def cadastrar(self):
        try:
            modelo = Modelo(nome = self.nome_var.get(), idMarca = self.idMarca_var.get())
            if self.modelo_controller.create(modelo):
                tk.messagebox.showinfo("Sucesso", "Modelo cadastrado com sucesso!")
                self.nome_var.set("")
                self.idMarca_var.set("")
            else:
                tk.messagebox.showerror("Erro", "Erro ao cadastrar modelo!")
            
        except Exception as e:
            tk.messagebox.showerror("Erro", e)