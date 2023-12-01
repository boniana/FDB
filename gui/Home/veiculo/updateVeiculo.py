import tkinter as tk

class UpdateVeiculo(tk.Frame):
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

        tk.Button(self, text="Cadastrar", command=self.atualizar_veiculo, width=25 ).grid(row=6, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=7, column=0, columnspan=4, pady=10)

    def atualizar_veiculo(self):
        try:
            veiculo = self.veiculoController.get(self.chassi_var.get())
            if not veiculo:
                raise Exception("Veículo não encontrado!")
            
            veiculo.id_modelo = self.id_modelo_var.get()
            veiculo.cor = self.cor_var.get()
            veiculo.ano = self.ano_var.get()
            veiculo.cpfProprietario = self.cpfProprietario_var.get()
            
            self.veiculoController.update(veiculo)
            tk.messagebox.showinfo("Sucesso", "Veículo Atualizado" )
        except:
            tk.messagebox.showerror("Erro", "Não foi possível atualizar o veículo" )