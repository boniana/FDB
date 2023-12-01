import tkinter as tk

class UpdateMarca(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.marcaController = controller.myController.marcaController()
        
        self.idMarca_var = tk.StringVar()
        self.nome_var = tk.StringVar()
        
        tk.Label(self, text="Atualizar Marca", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="ID Marca:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.idMarca_var, width=30 ).grid(row=2, column=0, padx=10, pady=5)
        
        tk.Label(self, text="Nome:").grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.nome_var, width=30 ).grid(row=4, column=0, padx=10, pady=5)
        
        tk.Button(self, text="Atualizar", command=self.atualizar_marca, width=25 ).grid(row=5, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=6, column=0, columnspan=4, pady=5)
        
    def atualizar_marca(self):
        idMarca = self.idMarca_var.get()
        marca = self.marcaController.get(idMarca)
        if marca:
            marca.nome = self.nome_var.get()
            self.marcaController.update(marca)
            tk.messagebox.showinfo("Sucesso", "Marca atualizada com sucesso!")
        else:
            tk.messagebox.showerror("Erro", "Marca não encontrada!")
        
        self.idMarca_var.set("")
        self.nome_var.set("")
        