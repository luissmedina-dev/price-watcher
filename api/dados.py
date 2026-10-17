from datetime import datetime, timezone

produtos = [
    {
        "id": 1,
        "nome": "Teclado mecânico",
        "url": "https://exemplo.com/produto",
        "precoMaximo": 250,
        "criadoEm": datetime.now(timezone.utc).isoformat()
    }
]

proximo_id = 2

categorias = [
    {
        "id": 1,
        "nome": "Periféricos"
    },
    {
        "id": 2,
        "nome": "Informática"
    },
    {
        "id": 3,
        "nome": "Acessórios"
    }
]

proxima_categoria_id = 4