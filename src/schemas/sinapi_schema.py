from pydantic import BaseModel, Field
from datetime import datetime

class SinapiSchema(BaseModel):
   valor: float
   unidade_da_federacao_codigo: str
   unidade_da_federacao: str
   periodo: datetime
   tipo_de_projeto: str
   padrao_de_acabamento: str
