import tkinter as tk

class DeleteVeiculo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.veiculoController = self.controller.myController.veiculoController()
        
        self.numeroChassi = tk.StringVar()
        
        tk.Label(self, text="Deletar Veículo", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="Chassi:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.numeroChassi, width=30 ).grid(row=2, column=0, padx=10, pady=15)
        
        tk.Button(self, text="Deletar", command=self.deletar_veiculo, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)
        
    def deletar_veiculo(self):
        try:
            chassi = self.numeroChassi.get()
            veiculo = self.veiculoController.get(chassi)
            if veiculo:
                self.veiculoController.delete(veiculo)
                tk.messagebox.showinfo("Sucesso", "Veículo deletado com sucesso!")
                self.numeroChassi.set("")
            else:
                tk.messagebox.showerror("Erro", "Veículo não encontrado!")
        except Exception as e:
            tk.messagebox.showerror("Erro", e)
        
        