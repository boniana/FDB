import tkinter as tk
from tkinter import ttk

class GetVeiculoByCpf(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.veiculoController = self.controller.myController.veiculoController()
        
        self.cpf_var = tk.StringVar()
        
        tk.Label(self, text="Buscar Veículo por CPF", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="CPF:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.cpf_var, width=30 ).grid(row=2, column=0, padx=10, pady=15)
        
        tk.Button(self, text="Buscar", command=self.get_veiculo, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)
        
    def get_veiculo(self):
            cpf = self.cpf_var.get()
            veiculos = self.veiculoController.getVeiculoByCPF(cpf)
            list_view = ttk.Treeview(self)
            list_view.grid(row=5, column=0, columnspan=6, padx=10, pady=5, sticky="nsew") 
            list_view.heading("#0", text="Chassi - Modelo - Cor - Ano")
                
            try:
                if veiculos:
                    for veiculo in veiculos:
                        list_view.insert("" ,"end", text = f"{veiculo.numeroChassi} - {veiculo.modelo.nome} - {veiculo.cor} - {veiculo.ano}")
                else:
                    raise Exception("Veículo não encontrado!")
            except Exception as e:
                tk.messagebox.showerror("Erro", e)
        
