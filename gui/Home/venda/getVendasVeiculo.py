import tkinter as tk

class GetVendasVeiculos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.vendaController = self.controller.myController.vendaController()
        
        self.chassi_var = tk.StringVar()
        
        tk.Label(self, text="Buscar Vendas por Veículo", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="Chassi do Veículo: ").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.chassi_var, width=30 ).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Button(self, text="Buscar", command=self.buscar_vendas, width=25 ).grid(row=2, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=3, column=0, columnspan=4, pady=10)
        
    def buscar_vendas(self):
        try:
            chassi = self.chassi_var.get()
            vendas = self.vendaController.getVendasVeiculo(chassi)
            
        except Exception as e:
            tk.messagebox.showerror("Erro", e)