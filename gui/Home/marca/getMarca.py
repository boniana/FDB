import tkinter as tk
from models.entitys import Marca

class GetMarca(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.marca_controller = self.controller.myController.marcaController()
        
        self.idMarca = tk.StringVar()
        
        tk.Label(self, text="Buscar Pessoa", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self, text="idMarca:").grid(row=1, column=0, padx=10, pady=5, columnspan=4)
        tk.Entry(self, textvariable=self.idMarca, width=30 ).grid(row=2, column=0, padx=10, pady=15, columnspan=4)
        tk.Button(self, text="Buscar", command=self.buscar_marca, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)

        
    def buscar_marca(self):
        try:
            m = self.marca_controller.get(self.idMarca.get())
            
            if not m:
                tk.messagebox.showerror("Erro", "Marca não encontrada.")
            else:
                tk.messagebox.showinfo("Marca", "Marca encontrada.\n\n" + self.idMarca.get() + " - " + m.nome )
            
        except:
            tk.messagebox.showerror("Erro", "Marca não encontrada.")
            
            
        

       