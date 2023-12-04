import tkinter as tk
from tkinter import ttk

class GetAllPessoa(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pessoaController = self.controller.myController.pessoaController()
        
        tk.Label(self, text="Listar Todos Pessoas", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Button(self, text="Listar", command=self.listar_pessoas, width=25 ).grid(row=1, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=2, column=0, columnspan=2, pady=10)
           
            
    def listar_pessoas(self):
        pessoas = self.pessoaController.getAll()
                    
        list_view = ttk.Treeview(self)
        list_view.grid(row=3, column=0, columnspan=6, padx=10, pady=5, sticky="nsew") 
        list_view.heading("#0", text="CPF - Nome - Estado Civil - Cpf Conjuge")
            
        for pessoa in pessoas:
            list_view.insert("" ,"end", text = f"{pessoa.cpf} - {pessoa.nome} - {pessoa.estadoCivil} - {pessoa.cpfConjuge if pessoa.cpfConjuge != None else ''}")