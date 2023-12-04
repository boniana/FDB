import tkinter as tk
from tkinter import messagebox

class deletePessoaApp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pessoaController = self.controller.myController.pessoaController()

        self.cpf_var = tk.StringVar()

        tk.Label(self, text="Deletar Pessoa", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="CPF:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.cpf_var, width=30 ).grid(row=2, column=0, padx=10, pady=15)
        
        tk.Button(self, text="Deletar", command=self.deletar_pessoa, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)
        
        
    def deletar_pessoa(self):
        try:
            cpf = self.cpf_var.get()
            pessoa = self.pessoaController.get(cpf)
            if pessoa:
                d = self.pessoaController.delete(pessoa) 
                if d != "Deletado com sucesso!":
                    raise Exception(d)
                messagebox.showinfo("Sucesso", "Pessoa deletada com sucesso!")
                self.cpf_var.set("")
            else:
                raise Exception("Pessoa não encontrada!")
        
        except Exception as e:
            messagebox.showerror("Erro", e)
        
        
       

if __name__ == "__main__":
    root = tk.Tk()
    deletePessoaApp(root)
    root.mainloop()