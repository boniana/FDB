import tkinter as tk
from tkinter import ttk

class GetAllVenda(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.vendaController = self.controller.myController.vendaController()
        
        tk.Label(self, text="Listar Todas Vendas", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Button(self, text="Listar", command=self.listar_vendas, width=25 ).grid(row=1, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=2, column=0, columnspan=2, pady=10)
           
           
    def listar_vendas(self):
        vendas = self.vendaController.getAll()
                    
        list_view = ttk.Treeview(self)
        list_view.grid(row=3, column=0, columnspan=6, padx=10, pady=5, sticky="nsew") 
        list_view.heading("#0", text="idVenda - Chassi - Comprador - Data - Valor")
            
        for venda in vendas:
            list_view.insert("" ,"end", text = f"{venda.idVenda} - {venda.numeroChassi} - {venda.cpfCompra} - {venda.data} - {venda.preco}")