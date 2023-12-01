import tkinter as tk
from tkinter import ttk

class GetAllVeiculo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.veiculoController = self.controller.myController.veiculoController()
        
        tk.Label(self, text="Listar Todos Veículos", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Button(self, text="Listar", command=self.listar_veiculos, width=25 ).grid(row=1, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=2, column=0, columnspan=2, pady=10)
           
           
    def listar_veiculos(self):
        veiculos = self.veiculoController.getAll()
                    
        list_view = ttk.Treeview(self)
        list_view.grid(row=3, column=0, columnspan=6, padx=10, pady=5, sticky="nsew") 
        list_view.heading("#0", text="Chassi - Modelo - Cor - Ano - CPF Proprietário")
            
        for veiculo in veiculos:
            list_view.insert("" ,"end", text = f"{veiculo.numeroChassi} - {veiculo.modelo.nome} - {veiculo.cor} - {veiculo.ano} - {veiculo.cpfProprietario}")