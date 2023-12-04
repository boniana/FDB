import tkinter as tk
from gui.Home.modelo.createModelo import CreateModelo
from gui.Home.modelo.deleteModelo import DeleteModelo
from gui.Home.modelo.getModelo import GetModelo
from gui.Home.modelo.getAllModelo import GetAllModelo
from gui.Home.modelo.updateModelo import UpdateModelo

class HomeModelo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="Modelo", font=("Helvetica", 16)).grid(row=0, column=0, sticky="nsew")
        
        tk.Button(self, text="Cadastrar Modelo",
                            command=lambda: controller.show_frame(CreateModelo), width= 30).grid(row=1, column=0, padx=5, pady=4)
        tk.Button(self, text="Deletar Modelo",
                            command=lambda: controller.show_frame(DeleteModelo), width= 30).grid(row=2, column=0, padx=5, pady=4)
        tk.Button(self, text="Buscar Modelo",
                            command=lambda: controller.show_frame(GetModelo), width= 30).grid(row=3, column=0, padx=5, pady=4)
        tk.Button(self, text="Listar Modelos",
                            command=lambda: controller.show_frame(GetAllModelo), width= 30).grid(row=4, column=0, padx=5, pady=4)
        tk.Button(self, text="Atualizar Modelo",
                            command=lambda: controller.show_frame(UpdateModelo), width= 30).grid(row=5, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Voltar para a página inicial",
                            command=lambda: self.controller.show_frame(self.controller.first)).grid(row=6, column=0, padx=5, pady=4)