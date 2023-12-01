import tkinter as tk
from datetime import datetime

class UpdateVenda(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.vendaController = self.controller.myController.vendaController()
        
        self.idVenda_var = tk.StringVar()
        self.chassi_var = tk.StringVar()
        self.cpfVendedor_var = tk.StringVar()
        self.cpfComprador_var = tk.StringVar()
        self.preco_var = tk.StringVar()
        self.data_var = tk.StringVar()
        
        tk.Label(self, text="Atualizar Venda", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
        
        tk.Label(self, text="Id da Venda: ").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.idVenda_var, width=30 ).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Chassi", anchor="w").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.chassi_var, width=30 ).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="CPF do Vendedor", anchor="w").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.cpfVendedor_var, width=30 ).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self, text="CPF do Comprador:", anchor="w").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.cpfComprador_var, width=30 ).grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self, text="preco:", anchor="w").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.preco_var, width=30 ).grid(row=5, column=1, padx=10, pady=5)

        tk.Label(self, text="data", anchor="w").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.data_var, width=30 ).grid(row=6, column=1, padx=10, pady=5)

        tk.Button(self, text="Cadastrar", command=self.atualizar_venda, width=25 ).grid(row=7, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=8, column=0, columnspan=4, pady=10)

    def atualizar_venda(self):
        try:
            idVenda = self.idVenda_var.get()
            venda = self.vendaController.get(idVenda)
            if venda == None:
                raise Exception("Venda não encontrada!")

            chassi = self.chassi_var.get()
            cpfVendedor = self.cpfVendedor_var.get()
            cpfComprador = self.cpfComprador_var.get()
            preco = self.preco_var.get()
            data = self.data_var.get()
            
            if cpfComprador == cpfVendedor:
                raise Exception("O comprador não pode ser o mesmo que o vendedor!")
            
            carro = self.controller.myController.veiculoController().get(chassi)
            if carro == None:
                raise Exception("Veículo não encontrado!")
            
            vendedor = self.controller.myController.pessoaController().get(cpfVendedor)
            if vendedor == None:
                raise Exception("Vendedor não encontrado!")
            
            comprador = self.controller.myController.pessoaController().get(cpfComprador)
            if comprador == None:
                raise Exception("Comprador não encontrado!")
            
            
            venda.cpfVendedor = cpfVendedor
            venda.cpfComprador = cpfComprador
            venda.preco = preco
            venda.data = datetime.strptime(data, '%d-%m-%Y')
            
            if self.vendaController.update(venda) == None:
                raise Exception("Não foi possível atualizar a venda!")
            
            tk.messagebox.showinfo("Sucesso", "Venda Atualizada" )
        
        except Exception as e:
            tk.messagebox.showerror("Erro", e)