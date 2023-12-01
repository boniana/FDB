import tkinter as tk
from gui.Home.venda.createVenda import CreateVenda
from gui.Home.venda.getVenda import GetVenda
from gui.Home.venda.deleteVenda import DeleteVenda
from gui.Home.venda.updateVenda import UpdateVenda

class HomeVenda(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Veículo", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
   
        tk.Button(self, text="Cadastrar Venda", command=lambda: controller.show_frame(CreateVenda), width=30).grid(row=1, column=0, columnspan=4, pady=10)
        tk.Button(self, text="Buscar Venda", command=lambda: controller.show_frame(GetVenda), width=30).grid(row=2, column=0, columnspan=4, pady=10)
        tk.Button(self, text="Deletar Venda", command=lambda: controller.show_frame(DeleteVenda), width=30).grid(row=3, column=0, columnspan=4, pady=10)
        tk.Button(self, text="Atualizar Venda", command=lambda: controller.show_frame(UpdateVenda), width=30).grid(row=4, column=0, columnspan=4, pady=10)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first)).grid(row=5, column=0, columnspan=4, pady=10)