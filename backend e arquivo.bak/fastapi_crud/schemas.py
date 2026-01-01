from pydantic import BaseModel
from typing import Optional, List

# ----------------- Role -----------------
class RoleBase(BaseModel):
    nomerole: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    idRole: int

    class Config:
        orm_mode = True


# ----------------- Usuario -----------------
class UsuarioBase(BaseModel):
    nome: str
    email: str
    idRole: int
    Ativo: Optional[bool] = True

class UsuarioCreate(UsuarioBase):
    senhaHash: str

class Usuario(UsuarioBase):
    idUsuario: int

    class Config:
        orm_mode = True


# ----------------- Regiao -----------------
class RegiaoBase(BaseModel):
    Regnome: str
    RegDescricao: Optional[str] = None

class RegiaoCreate(RegiaoBase):
    pass

class Regiao(RegiaoBase):
    idRegiao: int

    class Config:
        orm_mode = True


# ----------------- Cliente -----------------
class ClienteBase(BaseModel):
    clinome: str
    clicpf_cnpj: str
    clitelefone: Optional[str] = None
    cliemail: Optional[str] = None
    clirua: Optional[str] = None
    clicidade: Optional[str] = None
    cliestado: Optional[str] = None
    idregiao: int

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    idCliente: int

    class Config:
        orm_mode = True


# ----------------- Vendedor -----------------
class VendedorBase(BaseModel):
    Vendnome: str
    VendTelefone: Optional[str] = None
    VendEmail: Optional[str] = None
    idregiao: int

class VendedorCreate(VendedorBase):
    pass

class Vendedor(VendedorBase):
    idVendedor: int

    class Config:
        orm_mode = True


# ----------------- Produto -----------------
class ProdutoBase(BaseModel):
    ProdNome: str
    proddescricao: Optional[str] = None
    Prodpreco: float
    Prodestoque: int

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    idProduto: int

    class Config:
        orm_mode = True


# ----------------- Pedido -----------------
class PedidoBase(BaseModel):
    idcliente: int
    idvendedor: int

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    idPedido: int

    class Config:
        orm_mode = True


# ----------------- ItemPedido -----------------
class ItemPedidoBase(BaseModel):
    IdPedido: int
    IdProduto: int
    ItemQuantidade: int
    PrecoUnitario: float

class ItemPedidoCreate(ItemPedidoBase):
    pass

class ItemPedido(ItemPedidoBase):
    IdItemPedido: int

    class Config:
        orm_mode = True


# ----------------- ComissaoPedido -----------------
class ComissaoPedidoBase(BaseModel):
    IdPedido: int
    IdVendedor: int
    percentual: float
    ValorCalculado: Optional[float] = None

class ComissaoPedidoCreate(ComissaoPedidoBase):
    pass

class ComissaoPedido(ComissaoPedidoBase):
    IdComissao: int

    class Config:
        orm_mode = True

# ----------------- Venda -----------------
class VendaBase(BaseModel):
    idCliente: int
    idVendedor: int
    idProduto: int
    quantidade: int
    valorTotal: float

class VendaCreate(VendaBase):
    pass

class Venda(VendaBase):
    idVenda: int

    class Config:
        orm_mode = True

