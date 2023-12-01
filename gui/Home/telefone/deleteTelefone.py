import tkinter as tk
from controllers.Controller import Controller

class DeleteTelefone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.telefoneController = self.controller.myController.telefoneController()
        
        self.cpf_var = tk.StringVar()
        self.numero_var = tk.StringVar()
        
        tk.Label(self, text="Deletar Telefone", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
        
        tk.Label(self, text="CPF:", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.cpf_var, width=30 ).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Número:", anchor="w").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.numero_var, width=30 ).grid(row=2, column=1, padx=10, pady=5)
        
        tk.Button(self, text="Deletar", command=self.deletar_telefone, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)
  
    def deletar_telefone(self):
        cpf = self.cpf_var.get()
        numero = self.numero_var.get()
        
        if not cpf or not numero:
            tk.messagebox.showerror("Erro", "CPF e Número são campos obrigatórios.")
            return
        
        try:
            self.telefoneController.delete(cpf, numero)
            tk.messagebox.showinfo("Sucesso", "Telefone deletado com sucesso.")
            
            self.cpf_var.set("")
            self.numero_var.set("")
            
        except Exception as e:
            tk.messagebox.showerror("Erro", str(e))
            return