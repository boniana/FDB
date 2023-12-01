import tkinter as tk
from gui.Home.veiculo.createVeiculo import CreateVeiculo
from gui.Home.veiculo.updateVeiculo import UpdateVeiculo
from gui.Home.veiculo.deleteVeiculo import DeleteVeiculo
from gui.Home.veiculo.getVeiculo import GetVeiculo
from gui.Home.veiculo.getAllVeiculo import GetAllVeiculo
from gui.Home.veiculo.maisVendidos import MaisVendidos

class HomeVeiculo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="Veículo", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
     
        tk.Button(self, text="Cadastrar Veículo",
                            command=lambda: controller.show_frame(CreateVeiculo), width= 30).grid(row=1, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Buscar Veículo", 
                            command=lambda: controller.show_frame(GetVeiculo), width= 30).grid(row=2, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Buscar Veículos",
                            command=lambda: controller.show_frame(GetAllVeiculo), width= 30).grid(row=3, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Deletar Veículo",	
                            command=lambda: controller.show_frame(DeleteVeiculo), width= 30).grid(row=4, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Atualizar Veículo",
                            command=lambda: controller.show_frame(UpdateVeiculo), width= 30).grid(row=5, column=0, padx=5, pady=4)
       
        tk.Button(self, text="Veículos mais vendidos",
                            command=lambda: controller.show_frame(MaisVendidos), width= 30).grid(row=6, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Voltar para a página inicial",
                            command=lambda: self.controller.show_frame(self.controller.first)).grid(row=7, column=0, padx=5, pady=4)
        
        