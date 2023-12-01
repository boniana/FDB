import tkinter as tk
from tkinter import ttk


class GetAllMarca(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.marcaController = controller.myController.marcaController()
            
            tk.Label(self, text="Listar Marcas", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
            tk.Button(self, text="Listar", command=self.listar_marcas, width=25 ).grid(row=1, column=0, columnspan=4, pady=3)
            tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=2, column=0, columnspan=2, pady=10)
            
        def listar_marcas(self):
            marcas = self.marcaController.getAll()
            
            list_view = ttk.Treeview(self)
            list_view.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
            list_view.heading("#0", text="ID - Nome")
            
            for marca in marcas:
                list_view.insert("", "end", text=f"{marca.idMarca} - {marca.nome}")
