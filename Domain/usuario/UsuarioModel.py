from pydantic import BaseModel

class Usuario(BaseModel):
    Documento: str
    Usuario: str
    Clave: str
    Nombres: str
    Apellido: str
    CorreoElectronico: str
    TarjetaCredito: float
    Cvv: int