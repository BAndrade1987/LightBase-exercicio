from pydantic import BaseModel

class ClienteBase(BaseModel):
    nome: str
    telefone: str
    cpf: str
    placa_carro: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True
