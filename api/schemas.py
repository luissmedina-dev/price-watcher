from pydantic import BaseModel, Field, HttpUrl, field_validator

class ProdutoCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=60)
    url: HttpUrl 
    precoMaximo: float | None = Field(default=None, ge=0)

class ProdutoUpdate(BaseModel):
    nome: str | None = None
    url: HttpUrl | None = None
    precoMaximo: float | None = Field(default=None, ge=0)

    @field_validator("nome", "url")
    @classmethod
    def validar_campos_obrigatorios(cls,valor):
        if valor is None:
            raise ValueError("O campo não pode ser nulo")

        return valor

