import tkinter as tk

class DeleteVenda(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.vendaController = self.controller.myController.vendaController()
        
        self.idVenda = tk.StringVar()
        
        tk.Label(self, text="Deletar Venda", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="Id da Venda: ").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.idVenda, width=30 ).grid(row=2, column=0, padx=10, pady=15)
        
        tk.Button(self, text="Deletar", command=self.deletar_venda, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)
        
    def deletar_venda(self):
        try:
            idVenda = self.idVenda.get()
            venda = self.vendaController.get(idVenda)
            if venda:
                self.vendaController.delete(venda)
                tk.messagebox.showinfo("Sucesso", "Venda deletada com sucesso!")
                self.idVenda.set("")
            else:
                tk.messagebox.showerror("Erro", "Venda não encontrada!")
        except Exception as e:
            tk.messagebox.showerror("Erro", e)