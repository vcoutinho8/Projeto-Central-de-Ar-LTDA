from sqlalchemy.orm import Session
from sqlalchemy import func
import models
import schemas


# =========================
#   PRODUTO
# =========================
def listar_produtos(db: Session):
    return db.query(models.Produto).all()

def obter_produto(db: Session, idProduto: int):
    return db.query(models.Produto).filter(models.Produto.idProduto == idProduto).first()

def criar_produto(db: Session, produto: schemas.ProdutoCreate):
    novo = models.Produto(**produto.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def atualizar_produto(db: Session, idProduto: int, dados: schemas.ProdutoCreate):
    produto = obter_produto(db, idProduto)
    if not produto:
        return None
    for campo, valor in dados.dict().items():
        setattr(produto, campo, valor)
    db.commit()
    db.refresh(produto)
    return produto

def deletar_produto(db: Session, idProduto: int):
    produto = obter_produto(db, idProduto)
    if not produto:
        return None
    db.delete(produto)
    db.commit()
    return True


# =========================
#   REGIÃO
# =========================
def listar_regioes(db: Session):
    return db.query(models.Regiao).all()

def obter_regiao(db: Session, idRegiao: int):
    return db.query(models.Regiao).filter(models.Regiao.idRegiao == idRegiao).first()

def criar_regiao(db: Session, regiao: schemas.RegiaoCreate):
    nova = models.Regiao(**regiao.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def atualizar_regiao(db: Session, idRegiao: int, dados: schemas.RegiaoCreate):
    regiao = obter_regiao(db, idRegiao)
    if not regiao:
        return None
    for campo, valor in dados.dict().items():
        setattr(regiao, campo, valor)
    db.commit()
    db.refresh(regiao)
    return regiao

def deletar_regiao(db: Session, idRegiao: int):
    regiao = obter_regiao(db, idRegiao)
    if not regiao:
        return None
    db.delete(regiao)
    db.commit()
    return True


# =========================
#   CLIENTE
# =========================
def listar_clientes(db: Session):
    return db.query(models.Cliente).all()

def obter_cliente(db: Session, id: int):
    return db.query(models.Cliente).filter(models.Cliente.idCliente == id).first()

def criar_cliente(db: Session, cliente: schemas.ClienteCreate):
    novo = models.Cliente(**cliente.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def atualizar_cliente(db: Session, id: int, dados: schemas.ClienteCreate):
    cliente = obter_cliente(db, id)
    if not cliente:
        return None
    for campo, valor in dados.dict().items():
        setattr(cliente, campo, valor)
    db.commit()
    db.refresh(cliente)
    return cliente

def deletar_cliente(db: Session, id: int):
    cliente = obter_cliente(db, id)
    if not cliente:
        return None
    db.delete(cliente)
    db.commit()
    return True


# =========================
#   VENDEDOR
# =========================
def listar_vendedores(db: Session):
    return db.query(models.Vendedor).all()

def obter_vendedor(db: Session, idVendedor: int):
    return db.query(models.Vendedor).filter(models.Vendedor.idVendedor == idVendedor).first()

def criar_vendedor(db: Session, vendedor: schemas.VendedorCreate):
    novo = models.Vendedor(**vendedor.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def atualizar_vendedor(db: Session, idVendedor: int, dados: schemas.VendedorCreate):
    vendedor = obter_vendedor(db, idVendedor)
    if not vendedor:
        return None
    for campo, valor in dados.dict().items():
        setattr(vendedor, campo, valor)
    db.commit()
    db.refresh(vendedor)
    return vendedor

def deletar_vendedor(db: Session, idVendedor: int):
    vendedor = obter_vendedor(db, idVendedor)
    if not vendedor:
        return None
    db.delete(vendedor)
    db.commit()
    return True
# =========================
#   PEDIDO
# =========================
def listar_pedidos(db: Session):
    return db.query(models.Pedido).all()

def obter_pedido(db: Session, idPedido: int):
    return db.query(models.Pedido).filter(models.Pedido.idPedido == idPedido).first()

def criar_pedido(db: Session, pedido: schemas.PedidoCreate):
    novo = models.Pedido(**pedido.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def atualizar_pedido(db: Session, idPedido: int, dados: schemas.PedidoCreate):
    pedido = obter_pedido(db, idPedido)
    if not pedido:
        return None
    for campo, valor in dados.dict().items():
        setattr(pedido, campo, valor)
    db.commit()
    db.refresh(pedido)
    return pedido

def deletar_pedido(db: Session, idPedido: int):
    pedido = obter_pedido(db, idPedido)
    if not pedido:
        return None
    db.delete(pedido)
    db.commit()
    return True


# =========================
#   ITEM PEDIDO
# =========================
def listar_itens_pedido(db: Session):
    return db.query(models.ItemPedido).all()

def obter_item_pedido(db: Session, IdItemPedido: int):
    return db.query(models.ItemPedido).filter(models.ItemPedido.IdItemPedido == IdItemPedido).first()

def criar_item_pedido(db: Session, item: schemas.ItemPedidoCreate):
    novo = models.ItemPedido(**item.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def atualizar_item_pedido(db: Session, IdItemPedido: int, dados: schemas.ItemPedidoCreate):
    item = obter_item_pedido(db, IdItemPedido)
    if not item:
        return None
    for campo, valor in dados.dict().items():
        setattr(item, campo, valor)
    db.commit()
    db.refresh(item)
    return item

def deletar_item_pedido(db: Session, IdItemPedido: int):
    item = obter_item_pedido(db, IdItemPedido)
    if not item:
        return None
    db.delete(item)
    db.commit()
    return True


# =========================
#   COMISSÃO PEDIDO
# =========================
def listar_comissoes(db: Session):
    return db.query(models.ComissaoPedido).all()

def obter_comissao(db: Session, IdComissao: int):
    return db.query(models.ComissaoPedido).filter(models.ComissaoPedido.IdComissao == IdComissao).first()

def criar_comissao(db: Session, comissao: schemas.ComissaoPedidoCreate):
    nova = models.ComissaoPedido(**comissao.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def atualizar_comissao(db: Session, IdComissao: int, dados: schemas.ComissaoPedidoCreate):
    comissao = obter_comissao(db, IdComissao)
    if not comissao:
        return None
    for campo, valor in dados.dict().items():
        setattr(comissao, campo, valor)
    db.commit()
    db.refresh(comissao)
    return comissao

def deletar_comissao(db: Session, IdComissao: int):
    comissao = obter_comissao(db, IdComissao)
    if not comissao:
        return None
    db.delete(comissao)
    db.commit()
    return True

# ========================= RELATÓRIOS ==========================

def total_vendido_por_regiao(db: Session):
    return db.query(models.Regiao.Regnome.label("regiao"), func.sum(models.Venda.valorTotal).label("total"))\
        .join(models.Cliente, models.Cliente.idregiao == models.Regiao.idRegiao)\
        .join(models.Venda, models.Venda.idCliente == models.Cliente.idCliente)\
        .group_by(models.Regiao.Regnome)\
        .all()

def total_vendido_por_cliente(db: Session):
    return db.query(models.Cliente.idCliente.label("id"), models.Cliente.clinome.label("nome"), func.sum(models.Venda.valorTotal).label("total"))\
        .join(models.Venda, models.Venda.idCliente == models.Cliente.idCliente)\
        .group_by(models.Cliente.idCliente, models.Cliente.clinome)\
        .all()

def total_vendido_por_vendedor(db: Session):
    return db.query(models.Vendedor.idVendedor.label("id"), models.Vendedor.Vendnome.label("nome"), func.sum(models.Venda.valorTotal).label("total"))\
        .join(models.Venda, models.Venda.idVendedor == models.Vendedor.idVendedor)\
        .group_by(models.Vendedor.idVendedor, models.Vendedor.Vendnome)\
        .all()

def total_vendido_por_produto(db: Session):
    return db.query(models.Produto.idProduto.label("id"), models.Produto.ProdNome.label("nome"), func.sum(models.Venda.valorTotal).label("total"))\
        .join(models.Venda, models.Venda.idProduto == models.Produto.idProduto)\
        .group_by(models.Produto.idProduto, models.Produto.ProdNome)\
        .all()

def vendedores_por_regiao(db: Session, idRegiao: int):
    return db.query(models.Vendedor.idVendedor.label("id"), models.Vendedor.Vendnome.label("nome"), models.Vendedor.VendTelefone.label("telefone"))\
        .filter(models.Vendedor.idregiao == idRegiao)\
        .all()

def clientes_por_regiao(db: Session, idRegiao: int):
    return db.query(models.Cliente.idCliente.label("id"), models.Cliente.clinome.label("nome"), models.Cliente.clitelefone.label("telefone"))\
        .filter(models.Cliente.idregiao == idRegiao)\
        .all()
