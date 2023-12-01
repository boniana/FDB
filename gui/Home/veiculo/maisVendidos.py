import tkinter as tk
from tkinter import ttk

class MaisVendidos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.veiculoController = self.controller.myController.veiculoController()
        
        tk.Label(self, text="Veículos mais vendidos", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
        
        tk.Button(self, text="Listar", command=self.listar, width=25 ).grid(row=1, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=2, column=0, columnspan=4, pady=10)
        
    def listar(self):
        maisVendidos = self.veiculoController.maisVendidos()
        
        list_view = ttk.Treeview(self)
        list_view.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        list_view.heading("#0", text="Modelo - Marca - Quantidade")
        
        for veiculo in maisVendidos:
            list_view.insert("", "end", text=f"{veiculo[0]} - {veiculo[1]} - {veiculo[2]}")
        
        
            
       