from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL


Base = declarative_base()

class Usuario(Base):
    __tablename__ = "Usuario"
    idUsuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True)
    senhaHash = Column(String)
    idRole = Column(Integer, ForeignKey("Role.idRole"))
    Ativo = Column(Boolean)


class Cliente(Base):
    __tablename__ = "Cliente"
    idCliente = Column(Integer, primary_key=True, index=True)
    clinome = Column(String)
    clicpf_cnpj = Column(String)
    clitelefone = Column(String)
    cliemail = Column(String)
    clirua = Column(String)
    clicidade = Column(String)
    cliestado = Column(String)
    idregiao = Column(Integer, ForeignKey("Regiao.idRegiao"))


class Regiao(Base):
    __tablename__ = "Regiao"
    idRegiao = Column(Integer, primary_key=True, index=True)
    Regnome = Column(String)
    RegDescricao = Column(String)


class Produto(Base):
    __tablename__ = "Produto"
    idProduto = Column(Integer, primary_key=True, index=True)
    ProdNome = Column(String)
    proddescricao = Column(String)
    Prodpreco = Column(Float)
    Prodestoque = Column(Integer)


class Vendedor(Base):
    __tablename__ = "Vendedor"
    idVendedor = Column(Integer, primary_key=True, index=True)
    Vendnome = Column(String)
    VendTelefone = Column(String)
    VendEmail = Column(String)
    idregiao = Column(Integer, ForeignKey("Regiao.idRegiao"))


class Pedido(Base):
    __tablename__ = "Pedido"
    idPedido = Column(Integer, primary_key=True, index=True)
    idcliente = Column(Integer, ForeignKey("Cliente.id"))
    idvendedor = Column(Integer, ForeignKey("Vendedor.idVendedor"))


class ItemPedido(Base):
    __tablename__ = "ItemPedido"
    IdItemPedido = Column(Integer, primary_key=True, index=True)
    IdPedido = Column(Integer, ForeignKey("Pedido.idPedido"))
    IdProduto = Column(Integer, ForeignKey("Produto.idProduto"))
    ItemQuantidade = Column(Integer)
    PrecoUnitario = Column(Float)


class ComissaoPedido(Base):
    __tablename__ = "ComissaoPedido"
    IdComissao = Column(Integer, primary_key=True, index=True)
    IdPedido = Column(Integer, ForeignKey("Pedido.idPedido"))
    IdVendedor = Column(Integer, ForeignKey("Vendedor.idVendedor"))
    percentual = Column(Float)
    ValorCalculado = Column(Float)


class Role(Base):
    __tablename__ = "Role"
    idRole = Column(Integer, primary_key=True, index=True)
    nomerole = Column(String)


class Venda(Base):
    __tablename__ = "Venda"

    idVenda = Column(Integer, primary_key=True, index=True)
    idCliente = Column(Integer, ForeignKey("Cliente.idCliente"))
    idVendedor = Column(Integer, ForeignKey("Vendedor.idVendedor"))
    idProduto = Column(Integer, ForeignKey("Produto.idProduto"))
    quantidade = Column(Integer, nullable=False)
    valorTotal = Column(DECIMAL(10,2), nullable=False)

