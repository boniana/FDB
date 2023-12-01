import tkinter as tk

class getPessoaApp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pessoaController = self.controller.myController.pessoaController()

        self.cpf_var = tk.StringVar()

        tk.Label(self, text="Buscar Pessoa", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self, text="CPF:").grid(row=1, column=0, padx=10, pady=5, columnspan=4)
        tk.Entry(self, textvariable=self.cpf_var, width=30 ).grid(row=2, column=0, padx=10, pady=15, columnspan=4)
        tk.Button(self, text="Buscar", command=self.buscar_pessoa, width=25 ).grid(row=3, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=4, column=0, columnspan=4, pady=10)


    def buscar_pessoa(self):
        try:
            pessoa = self.pessoaController.get(self.cpf_var.get())
            if not pessoa:
                raise Exception("Pessoa não encontrada!")
            
            tk.messagebox.showinfo("Sucesso", f"Nome: {pessoa.nome}\nCPF: {pessoa.cpf}\nEndereço: {pessoa.endereco}\nEstado Civil: {pessoa.estadoCivil}\n { "Cpf Conjuge: " +pessoa.cpfConjuge  if pessoa.cpfConjuge != None else ""}" )
        except Exception as e:
            tk.messagebox.showerror("Erro", e)
            
        self.cpf_var.set("")

