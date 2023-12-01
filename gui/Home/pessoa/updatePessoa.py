import tkinter as tk
from tkinter import ttk

class updatePessoaApp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pessoaController = self.controller.myController.pessoaController()

        self.cpf_var = tk.StringVar()
        self.nome_var = tk.StringVar()
        self.endereco_var = tk.StringVar()
        self.estado_civil_var = tk.StringVar()
        self.cpf_conjuge_var = tk.StringVar()
        
        tk.Label(self, text="Atualizar Pessoa", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
    
        tk.Label(self, text="CPF:", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.cpf_var, width=30 ).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Nome:", anchor="w").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.nome_var, width=30 ).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Endereço:", anchor="w").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.endereco_var, width=30 ).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self, text="Estado Civil:", anchor="w").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        combo = ttk.Combobox(self, textvariable=self.estado_civil_var, width=30 )
        combo['values'] = ('Solteiro', 'Casado', 'Divorciado', 'Viúvo')
        combo['state'] = 'readonly'
        combo.current(0)
        combo.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self, text="CPF do Cônjuge:", anchor="w").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        tk.Entry(self, textvariable=self.cpf_conjuge_var, width=30 ).grid(row=5, column=1, padx=10, pady=5)

            # Botão de submissão
        tk.Button(self, text="Atualizar", command=self.atualizar_pessoa, width=25 ).grid(row=6, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=7, column=0, columnspan=4, pady=10)
 
      
    def atualizar_pessoa(self):
        try:
            pessoa = self.pessoaController.get(self.cpf_var.get())
            if not pessoa:
                raise Exception("Pessoa não encontrada!")
            
            pessoa.nome = self.nome_var.get()
            pessoa.endereco = self.endereco_var.get()
            pessoa.estadoCivil = self.estado_civil_var.get()
            cpf_conjuge = self.cpf_conjuge_var.get()
            
            print(cpf_conjuge)
            if pessoa.cpfConjuge == "" or pessoa.cpfConjuge == None:
                pessoa.cpfConjuge = None
            else:
                conjuge = self.pessoaController.get(cpf_conjuge)
                if not conjuge:
                    raise Exception("Cpf do cônjuge não encontrado!")
                pessoa.cpfConjuge = cpf_conjuge
            
            
            if self.pessoaController.update(pessoa) == None:
                raise Exception("Não foi possível atualizar a pessoa!")
            
            tk.messagebox.showinfo("Sucesso", "Pessoa Atualizada" )   
            
        except Exception as e:
            tk.messagebox.showerror("Erro", e) 
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = updatePessoaApp(root)
    root.mainloop()

