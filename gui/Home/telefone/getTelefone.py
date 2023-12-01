import tkinter as tk
from tkinter import messagebox


class GetTelefone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.telefoneController = self.controller.myController.telefoneController()

        self.cpf_var = tk.StringVar()

        tk.Label(self, text="Buscar Telefone", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self, text="CPF:").grid(row=1, column=0, padx=10, pady=5, columnspan=4)
        tk.Entry(self, textvariable=self.cpf_var, width=30 ).grid(row=2, column=0, padx=10, pady=15, columnspan=4)
        tk.Button(self, text="Buscar", command=self.buscar_telefone, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)
        
        
    def buscar_telefone(self):
        try:
            cpf = self.cpf_var.get()
            telefones = self.telefoneController.getAll(cpf)
            
            if not telefones:
                raise Exception("CPF não possui telefone cadastrado!")
            
            fones = ""
            for telefone in telefones:
                fones += f"({telefone.ddd}) {telefone.telefone}\n" 
                
                
            messagebox.showinfo("Telefone", fones)
                
            self.cpf_var.set("")
        
        except Exception as e:
            messagebox.showerror("Erro", e)
       