import tkinter as tk

class GetVeiculo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.veiculoController = self.controller.myController.veiculoController()
        
        self.numeroChassi = tk.StringVar()

        tk.Label(self, text="Buscar Veículos", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self, text="Chassi:").grid(row=1, column=0, padx=10, pady=5, columnspan=4)
        tk.Entry(self, textvariable=self.numeroChassi, width=30 ).grid(row=2, column=0, padx=10, pady=15, columnspan=4)
        tk.Button(self, text="Buscar", command=self.buscar_veiculo, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)

    def buscar_veiculo(self):
        chassi = self.numeroChassi.get()
        veiculo = self.veiculoController.get(chassi)
        
        if not veiculo:
            tk.messagebox.showerror("Erro", "Veículo não encontrado.")
        else:
            tk.messagebox.showinfo("Veículo", "Veículo encontrado.\n\n" + 
                "Chassi: " + str(veiculo.numeroChassi) + "\n" +
                "Modelo: " + str(veiculo.modelo.nome) + " - " + veiculo.modelo.marca.nome + "\n" +
                "Cor: " + str(veiculo.cor) + "\n" +
                "Ano: " + str(veiculo.ano) + "\n" +
                "CPF Proprietário: " + str(veiculo.cpfProprietario) + " - " + str(veiculo.proprietario.nome)+"\n"
                                )
            
        
        
        