from typing import Optional
from pydantic import BaseModel


class Languages(BaseModel):
    id: Optional[int] = None
    nome: str
    