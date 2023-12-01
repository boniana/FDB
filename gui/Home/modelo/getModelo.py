import tkinter as tk

class GetModelo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.modelo_controller = self.controller.myController.modeloController()
        
        self.idModelo = tk.StringVar()
        
        tk.Label(self, text="Buscar Modelo", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self, text="idModelo:").grid(row=1, column=0, padx=10, pady=5, columnspan=4)
        tk.Entry(self, textvariable=self.idModelo, width=30 ).grid(row=2, column=0, padx=10, pady=15, columnspan=4)
        tk.Button(self, text="Buscar", command=self.buscar_modelo, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)

    def buscar_modelo(self):
        try:
            m = self.modelo_controller.get(self.idModelo.get())
            
            if not m:
                tk.messagebox.showerror("Erro", "Modelo não encontrado.")
            else:
                tk.messagebox.showinfo("Modelo", "Modelo encontrado.\n\n" + self.idModelo.get() + " - " + m.nome  + " - " + m.marca.nome)
            
        except:
            tk.messagebox.showerror("Erro", "Modelo não encontrado.")