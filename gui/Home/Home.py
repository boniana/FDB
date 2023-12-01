import tkinter as tk
from gui.Home.pessoa.homePessoa import HomePessoa
from gui.Home.telefone.homeTelefone import HomeTelefone
from gui.Home.marca.homeMarca import HomeMarca
from gui.Home.modelo.homeModelo import HomeModelo
from gui.Home.veiculo.homeVeiculo import HomeVeiculo
from gui.Home.venda.homeVenda import HomeVenda
from gui.Home.Frames import AllFrames
from controllers.Controller import Controller
from database.dados import create_dados

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Aplicação")
        self.geometry("400x400+40+40")
        self.eval('tk::PlaceWindow . center')
        self.resizable(False, False)
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        
        self.myController = Controller()
        
        self.first = StartPage
        all_frames = AllFrames().FRAMES
        all_frames.append(StartPage)
        
        for F in all_frames:
            frame = F(self.container, self)
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.container.grid_columnconfigure(0, weight=1)
        
        for frame in self.frames.values():
            frame.grid_columnconfigure(0, weight=1)
            
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        self.current_frame = self.frames[cont]
        self.current_frame.tkraise()
        
    
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Página Inicial", font=("Helvetica", 16))

        button1 = tk.Button(self, text="Pessoa",
                            command=lambda: controller.show_frame(HomePessoa), width=30)
        button2 = tk.Button(self, text="Telefone da Pessoa",
                            command=lambda: controller.show_frame(HomeTelefone), width=30)
        button3 = tk.Button(self, text="Marca",
                            command=lambda: controller.show_frame(HomeMarca), width=30)
        button4 = tk.Button(self, text="Modelo",
                            command=lambda: controller.show_frame(HomeModelo), width=30)
        button5 = tk.Button(self, text="Veículo",
                            command=lambda: controller.show_frame(HomeVeiculo) , width=30)
        button6 = tk.Button(self, text="Venda",
                            command=lambda: controller.show_frame(HomeVenda), width=30)

        label.grid(row=1, column=0, sticky="nsew")
        
        button1.grid(row=2, column=0, padx=5, pady=4)
        button2.grid(row=3, column=0, padx=5, pady=4)
        button3.grid(row=4, column=0, padx=5, pady=4)
        button4.grid(row=5, column=0, padx=5, pady=4)
        button5.grid(row=6, column=0, padx=5, pady=4)
        button6.grid(row=7, column=0, padx=5, pady=4)
