import tkinter as tk
from gui.Home.marca.createMarca import CreateMarca
from gui.Home.marca.getMarca import GetMarca
from gui.Home.marca.updateMarca import UpdateMarca
from gui.Home.marca.deleteMarca import DeleteMarca
from gui.Home.marca.getAllMarca import GetAllMarca


class HomeMarca(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="Marca", font=("Helvetica", 16)).grid(row=0, column=0, sticky="nsew")
        
        tk.Button(self, text="Cadastrar", command=lambda: controller.show_frame(CreateMarca), width= 30).grid(row=1, column=0,padx=5, pady=4)
        tk.Button(self, text="Buscar Marca", command=lambda: controller.show_frame(GetMarca), width= 30).grid(row=2, column=0, padx=5, pady=4)
        tk.Button(self, text="Atualizar Marca", command=lambda: controller.show_frame(UpdateMarca), width= 30).grid(row=3, column=0, padx=5, pady=4)
        tk.Button(self, text="Deletar Marca", command=lambda: controller.show_frame(DeleteMarca), width= 30).grid(row=4, column=0, padx=5, pady=4)
        tk.Button(self, text="Listar Marcas", command=lambda: controller.show_frame(GetAllMarca), width= 30).grid(row=5, column=0, padx=5, pady=4)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: self.controller.show_frame(self.controller.first)).grid(row=6, column=0, padx=5, pady=4)
        
    