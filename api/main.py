from fastapi import FastAPI, HTTPException, status, Response
from datetime import datetime, timezone
from api.dados import (produtos, proximo_id, categorias, proxima_categoria_id)
from api.schemas import ProdutoCreate, ProdutoUpdate

app = FastAPI(
    title="Estom API",
    description="API para gerenciamento de produtos e acompanhamento de preços.",
    version="1.0.0"
)

# Create
@app.post("/produtos", status_code=status.HTTP_201_CREATED, summary="Cadastrar produto", responses={
    409: {"description": "Produto já cadastrado"},
    422: {"description": "Dados inválidos"}
})
def criar_grupo(produto: ProdutoCreate, response: Response):
    global proximo_id

    for produto_existente in produtos:
        if produto_existente["url"] == str(produto.url):
            raise HTTPException(
                status_code=409,
                detail="Este produto já está cadastrado"
            )

    novo_produto = {
        "id": proximo_id,
        "nome": produto.nome,
        "url": str(produto.url),
        "precoMaximo": produto.precoMaximo,
        "criadoEm": datetime.now(timezone.utc).isoformat()
    }

    produtos.append(novo_produto)
    proximo_id += 1

    response.headers["Location"] = f"/produtos/{novo_produto['id']}"

    return novo_produto

# Update
@app.patch("/produtos/{produto_id}", summary="Atualizar parcialmente produto", responses={
        404: {"description": "Produto não encontrado"},
        422: {"description": "Dados inválidos"}
    })
def atualizar_produto(produto_id: int, dados:ProdutoUpdate):
    for produto in produtos:
        if produto["id"] == produto_id:
            # Retorna apenas os campos que o cliente realmente enviou
            alteracoes = dados.model_dump(exclude_unset=True)

            if "url" in alteracoes:
                alteracoes["url"] = str(alteracoes["url"])
            
            produto.update(alteracoes)
            return produto

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )

@app.put("/produtos/{produto_id}", summary="Substituir produto", responses={
        404: {"description": "Produto não encontrado"},
        422: {"description": "Dados inválidos"}
    })
def atualizar_produto(produto_id: int, dados: ProdutoCreate):
    for produto in produtos:
        if produto["id"] == produto_id:
            alteracoes = dados.model_dump()
            alteracoes["url"] = str(alteracoes["url"])

            produto.update(alteracoes)
            return produto

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )

# Delete
@app.delete("/produtos/{produto_id}", status_code=204, summary="Excluir produto", responses={
        404: {"description": "Produto não encontrado"},
        422: {"description": "ID inválido"}
    })
def deletar_produto(produto_id: int):
    for indice, produto in enumerate(produtos):
        if produto["id"] == produto_id:
            del produtos[indice]
            return
            
    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )

    
# Read
@app.get("/produtos/{produto_id}", summary="Buscar produto por ID", responses={
        404: {"description": "Produto não encontrado"},
        422: {"description": "ID inválido"}
    })
def buscar_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )

@app.get("/produtos", summary="Listar produtos")
def listar_produtos():
    return produtos

@app.get(
    "/categorias",
    summary="Listar categorias"
)
def listar_categorias():
    return categorias


@app.get(
    "/categorias/{categoria_id}",
    summary="Buscar categoria por ID",
    responses={
        404: {"description": "Categoria não encontrada"},
        422: {"description": "ID inválido"}
    }
)
def buscar_categoria(categoria_id: int):
    for categoria in categorias:
        if categoria["id"] == categoria_id:
            return categoria

    raise HTTPException(
        status_code=404,
        detail="Categoria não encontrada"
    )