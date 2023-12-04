from gui.Home.pessoa import createPessoa, getPessoa, updatePessoa, deletePessoa, homePessoa, getAllPessoa
from gui.Home.telefone import createTelefone, homeTelefone, getTelefone, deleteTelefone
from gui.Home.marca import homeMarca, createMarca, getMarca, deleteMarca, updateMarca, getAllMarca
from gui.Home.modelo import homeModelo, createModelo, getModelo, getAllModelo, deleteModelo, updateModelo
from gui.Home.veiculo import homeVeiculo, createVeiculo, getVeiculo, getAllVeiculo, deleteVeiculo, updateVeiculo, maisVendidos, getVeiculoByCpf
from gui.Home.venda import homeVenda, createVenda, getVenda, deleteVenda, updateVenda, getAllVenda

class AllFrames:
    def __init__(self):
        self.FRAMES = [ 
        homePessoa.HomePessoa, createPessoa.CreatePessoaApp, deletePessoa.deletePessoaApp, getPessoa.getPessoaApp, updatePessoa.updatePessoaApp, getAllPessoa.GetAllPessoa,
        homeTelefone.HomeTelefone, createTelefone.CreateTelefone,  getTelefone.GetTelefone, deleteTelefone.DeleteTelefone,
        homeMarca.HomeMarca, createMarca.CreateMarca, getMarca.GetMarca, deleteMarca.DeleteMarca, updateMarca.UpdateMarca, getAllMarca.GetAllMarca,
        homeModelo.HomeModelo, createModelo.CreateModelo, getModelo.GetModelo, getAllModelo.GetAllModelo, deleteModelo.DeleteModelo, updateModelo.UpdateModelo,
        homeVeiculo.HomeVeiculo, createVeiculo.CreateVeiculo, getVeiculo.GetVeiculo, getAllVeiculo.GetAllVeiculo, deleteVeiculo.DeleteVeiculo, updateVeiculo.UpdateVeiculo, maisVendidos.MaisVendidos, getVeiculoByCpf.GetVeiculoByCpf,
        homeVenda.HomeVenda, createVenda.CreateVenda, getVenda.GetVenda, deleteVenda.DeleteVenda, updateVenda.UpdateVenda, getAllVenda.GetAllVenda
        ]