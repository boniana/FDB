import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from models.entitys import Pessoa


class CreatePessoaApp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pessoaController = self.controller.myController.pessoaController()

        self.cpf_var = tk.StringVar()
        self.nome_var = tk.StringVar()
        self.endereco_var = tk.StringVar()
        self.estado_civil_var = tk.StringVar()
        self.cpf_conjuge_var = tk.StringVar()

        tk.Label(self, text="Cadastro de Pessoa", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

            # Criando os rótulos e campos de entrada
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
        tk.Button(self, text="Cadastrar", command=self.cadastrar_pessoa, width=25 ).grid(row=6, column=0, columnspan=4, pady=3)
        tk.Button(self, text="Voltar para a página inicial", command=lambda: controller.show_frame(controller.first), width=25).grid(row=7, column=0, columnspan=4, pady=10)


    def cadastrar_pessoa(self):
            cpf = self.cpf_var.get()
            nome = self.nome_var.get()
            endereco = self.endereco_var.get()
            estado_civil = self.estado_civil_var.get()
            cpf_conjuge = self.cpf_conjuge_var.get()

            if not cpf or not nome:
                messagebox.showerror("Erro", "CPF e Nome são campos obrigatórios.")
                return

            try:
                if cpf_conjuge == "":
                    cpf_conjuge = None
                else:
                    conjuge = self.pessoaController.get(cpf_conjuge)
                    if conjuge == None:
                        raise Exception("Cônjuge não encontrado")
                    
                pessoa = Pessoa(cpf=cpf, nome=nome, estadoCivil=estado_civil, endereco=endereco, cpfConjuge=cpf_conjuge)
                
                
                
                if self.pessoaController.create(pessoa) != "Cadastrado com sucesso!":
                    raise Exception("Pessoa não cadastrada")
                
                messagebox.showinfo("Cadastro realizado", pessoa.__repr__())
                
            except Exception as e:
                messagebox.showerror("Erro", e)

            self.cpf_var.set("")
            self.nome_var.set("")
            self.endereco_var.set("")
            self.estado_civil_var.set("")
            self.cpf_conjuge_var.set("")

