import tkinter as tk
from gui.Home.telefone.createTelefone import CreateTelefone
from gui.Home.telefone.deleteTelefone import DeleteTelefone
from gui.Home.telefone.getTelefone import GetTelefone


class HomeTelefone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="Telefone", font=("Helvetica", 16)).grid(row=0, column=0, sticky="nsew")
        
        tk.Button(self, text="Cadastrar Telefone",
                            command=lambda: controller.show_frame(CreateTelefone), width= 30).grid(row=1, column=0, padx=5, pady=4)
        tk.Button(self, text="Deletar Telefone",
                            command=lambda: controller.show_frame(DeleteTelefone), width= 30).grid(row=2, column=0, padx=5, pady=4)
        tk.Button(self, text="Buscar Telefone",
                            command=lambda: controller.show_frame(GetTelefone), width= 30).grid(row=3, column=0, padx=5, pady=4)
        tk.Button(self, text="Voltar para a página inicial",
                            command=lambda: self.controller.show_frame(self.controller.first)).grid(row=4, column=0, padx=5, pady=4)
        
        
