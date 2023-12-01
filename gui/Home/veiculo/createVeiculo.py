import tkinter as tk
from models.entitys import Veiculo

class CreateVeiculo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.veiculoController = self.controller.myController.veiculoController()
        
        self.chassi_var = tk.StringVar()
        self.id_modelo_var = tk.StringVar()
        self.cor_var = tk.StringVar()
        self.ano_var = tk.StringVar()
        self.cpfProprietario_var = tk.StringVar()
        
        
        tk.Label(self, text="Cadastro de Veículo", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

        tk.Label(self, text="Chassi", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.chassi_var, width=30 ).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Id do Modelo", anchor="w").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.id_modelo_var, width=30 ).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Cor:", anchor="w").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.cor_var, width=30 ).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self, text="Ano:", anchor="w").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.ano_var, width=30 ).grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self, text="CPF Proprietário:", anchor="w").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.cpfProprietario_var, width=30 ).grid(row=5, column=1, padx=10, pady=5)

        tk.Button(self, text="Cadastrar", command=self.cadastrar_pessoa, width=25 ).grid(row=6, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=7, column=0, columnspan=4, pady=10)

    def cadastrar_pessoa(self):
        try:
            chassi = self.chassi_var.get()
            id_modelo = self.id_modelo_var.get()
            cor = self.cor_var.get()
            ano = self.ano_var.get()
            cpfProprietario = self.cpfProprietario_var.get()
            
            if not chassi or not id_modelo or not cor or not ano or not cpfProprietario:
                raise Exception("Todos os campos devem ser preenchidos")
            
            pessoa = self.controller.myController.pessoaController().get(cpfProprietario)
            if pessoa == None:
                raise Exception("Pessoa não encontrada")
            
            veiculo = Veiculo(numeroChassi = chassi,
                idModelo = id_modelo,
                cor = cor, 
                ano = ano,
                cpfProprietario =cpfProprietario)
            v = self.veiculoController.create(veiculo)
            
            if not v:
                raise Exception("Veículo não cadastrado")
            
            tk.messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso")
            
            self.chassi_var.set("")
            self.id_modelo_var.set("")
            self.cor_var.set("")
            self.ano_var.set("")
            self.cpfProprietario_var.set("")
            
        except Exception as e:
            tk.messagebox.showerror("Erro", e)