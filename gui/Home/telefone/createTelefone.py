import tkinter as tk
from controllers.Controller import Controller
from models.entitys import Telefone

class CreateTelefone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.telefoneController = self.controller.myController.telefoneController()
        
        self.cpf_var = tk.StringVar()
        self.numero_var = tk.StringVar()
        self.ddd_var = tk.StringVar()
        
        tk.Label(self, text="Cadastro de Telefone", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
        
        tk.Label(self, text="CPF:", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.cpf_var, width=30 ).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self, text="DDD:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.ddd_var, width=30 ).grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Número:", anchor="w").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.numero_var, width=30 ).grid(row=3, column=1, padx=10, pady=5)
    
        
        tk.Button(self, text="Cadastrar", command=self.cadastrar_telefone, width=25 ).grid(row=4, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=5, column=0, columnspan=4, pady=10)
        
    def cadastrar_telefone(self):
        cpf = self.cpf_var.get()
        numero = self.numero_var.get()
        ddd = self.ddd_var.get()
        
        try:
            if not cpf or not numero:
                raise Exception("Preencha todos os campos!")
            
            telefone = Telefone(cpf=cpf, telefone=numero, ddd=ddd)
            self.telefoneController.create(telefone)
            tk.messagebox.showinfo("Sucesso", "Telefone cadastrado com sucesso.")
                
            self.cpf_var.set("")
            self.numero_var.set("")
            self.ddd_var.set("")
            
        except Exception as e:
            tk.messagebox.showerror("Erro", str(e))
            return