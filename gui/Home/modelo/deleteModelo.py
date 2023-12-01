import tkinter as tk

class DeleteModelo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.modeloController = self.controller.myController.modeloController()
        
        self.idModelo_var = tk.StringVar()
        
        tk.Label(self, text="Deletar Modelo", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="ID Modelo:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.idModelo_var, width=30 ).grid(row=2, column=0, padx=10, pady=15)
        
        tk.Button(self, text="Deletar", command=self.deletar, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)
        
    def deletar(self):
        try:
            idModelo = self.idModelo_var.get()
            modelo = self.modeloController.get(idModelo)
            if modelo:
                self.modeloController.delete(modelo)
                tk.messagebox.showinfo("Sucesso", "Modelo deletado com sucesso!")
            else:
                tk.messagebox.showerror("Erro", "Modelo não encontrado!")
        except Exception as e:
            tk.messagebox.showerror("Erro", e)
        
        self.idModelo_var.set("")