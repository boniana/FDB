import tkinter as tk
from models.entitys import Modelo

class UpdateModelo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.modelo_controller = self.controller.myController.modeloController()
        
        self.idModelo_var = tk.StringVar()
        self.nome_var = tk.StringVar()
        self.idMarca_var = tk.StringVar()
        
        tk.Label(self, text="Atualizar Marca", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="Id do Modelo:", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.idModelo_var, width=30 ).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Nome:", anchor="w").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.nome_var, width=30 ).grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Id da Marca:", anchor="w").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.idMarca_var, width=30 ).grid(row=3, column=1, padx=10, pady=5)
        
        tk.Button(self, text="Cadastrar", command=self.atualizar_modelo, width=25 ).grid(row=4, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=5, column=0, columnspan=4, pady=10)
        
    def atualizar_modelo(self):
        try:
            m = self.modelo_controller.get(self.idModelo_var.get())
            
            if not m:
                tk.messagebox.showerror("Erro", "Modelo não encontrado.")
            else:
                m.nome = self.nome_var.get()
                m.idMarca = self.idMarca_var.get()
                
                self.modelo_controller.update(m)
                
                tk.messagebox.showinfo("Modelo", "Modelo atualizado com sucesso.")
        except:
            tk.messagebox.showerror("Erro", "Modelo não encontrado.")