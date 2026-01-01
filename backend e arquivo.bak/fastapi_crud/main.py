from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from models import Vendedor, Cliente, Produto
from fastapi.security import OAuth2PasswordRequestForm
import crud
import models
import schemas
from database import engine, get_db

# -------------------- Cria tabelas --------------------
models.Base.metadata.create_all(bind=engine)

# -------------------- FastAPI --------------------
app = FastAPI(title="Central Backend", version="1.0")

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

valid_users = {
    "admin@empresa.com": "12345"
}
# -------------------- Router dos relatórios --------------------
router = APIRouter(prefix="/relatorio")

# -------------------- ADMIN --------------------
@app.get("/admin", response_class=HTMLResponse)
async def admin_index():
    with open("telaprincipal.html", "r", encoding="utf-8") as f:
        return f.read()

# ========================= USUARIO =========================
@app.get("/usuario/", response_model=list[schemas.Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.listar_usuarios(db)

@app.get("/usuario/{idUsuario}", response_model=schemas.Usuario)
def buscar_usuario(idUsuario: int, db: Session = Depends(get_db)):
    usuario = crud.obter_usuario(db, idUsuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if valid_users.get(form_data.username) == form_data.password:
        return {"access_token": "fake-jwt-token-123"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")

@app.post("/usuario/", response_model=schemas.Usuario)
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.criar_usuario(db, usuario)

@app.put("/usuario/{idUsuario}", response_model=schemas.Usuario)
def atualizar_usuario(idUsuario: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    u = crud.atualizar_usuario(db, idUsuario, usuario)
    if not u:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return u

@app.delete("/usuario/{idUsuario}")
def deletar_usuario(idUsuario: int, db: Session = Depends(get_db)):
    sucesso = crud.deletar_usuario(db, idUsuario)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"mensagem": "Usuário deletado com sucesso"}

# ========================= CLIENTE =========================

@app.get("/cliente/", response_model=list[schemas.Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    return crud.listar_clientes(db)

@app.get("/cliente/{id}", response_model=schemas.Cliente)
def buscar_cliente(id: int, db: Session = Depends(get_db)):
    c = crud.obter_cliente(db, id)
    if not c:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return c

@app.post("/cliente/", response_model=schemas.Cliente)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.criar_cliente(db, cliente)

@app.put("/cliente/{id}", response_model=schemas.Cliente)
def atualizar_cliente(id: int, cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    c = crud.atualizar_cliente(db, id, cliente)
    if not c:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return c

@app.delete("/cliente/{id}")
def deletar_cliente(id: int, db: Session = Depends(get_db)):
    sucesso = crud.deletar_cliente(db, id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"mensagem": "Cliente deletado com sucesso"}

# ========================= PRODUTO =========================

@app.get("/produto/", response_model=list[schemas.Produto])
def listar_produtos(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)

@app.get("/produto/{idProduto}", response_model=schemas.Produto)
def buscar_produto(idProduto: int, db: Session = Depends(get_db)):
    p = crud.obter_produto(db, idProduto)
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return p

@app.post("/produto/", response_model=schemas.Produto)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    return crud.criar_produto(db, produto)

@app.put("/produto/{idProduto}", response_model=schemas.Produto)
def atualizar_produto(idProduto: int, produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    p = crud.atualizar_produto(db, idProduto, produto)
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return p

@app.delete("/produto/{idProduto}")
def deletar_produto(idProduto: int, db: Session = Depends(get_db)):
    sucesso = crud.deletar_produto(db, idProduto)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"mensagem": "Produto deletado com sucesso"}

# ========================= REGIÃO =========================

@app.get("/regiao/", response_model=list[schemas.Regiao])
def listar_regioes(db: Session = Depends(get_db)):
    return crud.listar_regioes(db)

# ========================= VENDEDOR =========================

@app.get("/vendedor/", response_model=list[schemas.Vendedor])
def listar_vendedores(db: Session = Depends(get_db)):
    return crud.listar_vendedores(db)

@app.post("/vendedor/", response_model=schemas.Vendedor)
def criar_vendedor(vendedor: schemas.VendedorCreate, db: Session = Depends(get_db)):
    db.add(models.Vendedor(
        Vendnome=vendedor.Vendnome,
        VendTelefone=vendedor.VendTelefone,
        VendEmail=vendedor.VendEmail,
        idregiao=vendedor.idregiao
    ))
    db.commit()
    db.refresh(db.query(models.Vendedor).order_by(models.Vendedor.idVendedor.desc()).first())
    return db.query(models.Vendedor).order_by(models.Vendedor.idVendedor.desc()).first()


@app.delete("/vendedor/{id}")
def delete_vendedor(id: int, db: Session = Depends(get_db)):
    vendedor = db.query(Vendedor).filter(Vendedor.idVendedor == id).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    db.delete(vendedor)
    db.commit()
    return {"detail": "Vendedor deletado com sucesso"}

# ========================= PEDIDO / ITENS / COMISSÃO =========================
# (Não mexi pois estavam corretos)

# ===================== RELATÓRIOS =====================

@router.get("/regiao")
def relatorio_regiao(db: Session = Depends(get_db)):
    resultados = db.execute(text("""
        SELECT r.idRegiao AS id, r.Regnome AS nome, COALESCE(SUM(v.valorTotal), 0) AS total
        FROM Regiao r
        LEFT JOIN Cliente c ON c.idregiao = r.idRegiao
        LEFT JOIN Venda v ON v.idCliente = c.idCliente
        GROUP BY r.idRegiao, r.Regnome
    """)).mappings().all()

    return [{"id": r["id"], "nome": r["nome"], "total": float(r["total"])} for r in resultados]


@router.get("/vendedor")
def relatorio_vendedor(db: Session = Depends(get_db)):
    resultados = db.execute(text("""
        SELECT v.idVendedor AS id, v.Vendnome AS nome, COALESCE(SUM(vn.valorTotal), 0) AS total
        FROM Vendedor v
        LEFT JOIN Venda vn ON vn.idVendedor = v.idVendedor
        GROUP BY v.idVendedor, v.Vendnome
    """)).mappings().all()

    return [{"id": r["id"], "nome": r["nome"], "total": float(r["total"])} for r in resultados]


@router.get("/produto")
def relatorio_produto(db: Session = Depends(get_db)):
    resultados = db.execute(text("""
        SELECT p.idProduto AS id, p.ProdNome AS nome, COALESCE(SUM(v.valorTotal), 0) AS total
        FROM Produto p
        LEFT JOIN Venda v ON v.idProduto = p.idProduto
        GROUP BY p.idProduto, p.ProdNome
    """)).mappings().all()

    return [{"id": r["id"], "nome": r["nome"], "total": float(r["total"])} for r in resultados]


@router.get("/cliente")
def relatorio_cliente(db: Session = Depends(get_db)):
    resultados = db.execute(text("""
        SELECT c.idCliente AS id, c.clinome AS nome, COALESCE(SUM(v.valorTotal), 0) AS total
        FROM Cliente c
        LEFT JOIN Venda v ON v.idCliente = c.idCliente
        GROUP BY c.idCliente, c.clinome
    """)).mappings().all()

    return [{"id": r["id"], "nome": r["nome"], "total": float(r["total"])} for r in resultados]


@router.get("/regiao/{id}/vendedores")
def vendedores_por_regiao(id: int, db: Session = Depends(get_db)):
    resultados = db.execute(text("""
        SELECT v.idVendedor AS id, v.Vendnome AS nome, v.VendTelefone AS telefone
        FROM Vendedor v
        WHERE v.idregiao = :id
    """), {"id": id}).mappings().all()

    return [{"id": r["id"], "nome": r["nome"], "telefone": r["telefone"]} for r in resultados]


@router.get("/regiao/{id}/clientes")
def clientes_por_regiao(id: int, db: Session = Depends(get_db)):
    resultados = db.execute(text("""
        SELECT c.idCliente AS id, c.clinome AS nome, c.clitelefone AS telefone
        FROM Cliente c
        WHERE c.idregiao = :id
    """), {"id": id}).mappings().all()

    return [{"id": r["id"], "nome": r["nome"], "telefone": r["telefone"]} for r in resultados]


# ✅ Agora SIM adicionamos o router no APP
app.include_router(router)
