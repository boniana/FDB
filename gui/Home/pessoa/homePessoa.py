import tkinter as tk
from gui.Home.pessoa.createPessoa import CreatePessoaApp
from gui.Home.pessoa.getPessoa import getPessoaApp
from gui.Home.pessoa.updatePessoa import updatePessoaApp
from gui.Home.pessoa.deletePessoa import deletePessoaApp
from gui.Home.pessoa.getAllPessoa import GetAllPessoa

class HomePessoa(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        tk.Label(self, text="Pessoa", font=("Helvetica", 16)).grid(row=0, column=0, sticky="nsew")
        
        tk.Button(self, text="Cadastrar Pessoa",
                            command=lambda: controller.show_frame(CreatePessoaApp), width= 30).grid(row=1, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Buscar Pessoa", 
                            command=lambda: controller.show_frame(getPessoaApp), width= 30).grid(row=2, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Atualizar Pessoa",
                            command=lambda: controller.show_frame(updatePessoaApp), width= 30).grid(row=3, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Deletar Pessoa",
                            command=lambda: controller.show_frame(deletePessoaApp), width= 30).grid(row=4, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Listar Todas Pessoas",
                            command=lambda: controller.show_frame(GetAllPessoa), width= 30).grid(row=5, column=0, padx=5, pady=4)
        
        tk.Button(self, text="Voltar para a página inicial",
                            command=lambda: self.controller.show_frame(self.controller.first)).grid(row=6, column=0, padx=5, pady=4)
        

        