from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SinapiModel(Base):
   __tablename__ = "sinapi_dados"

   id = Column(Integer, primary_key=True, autoincrement=True)
   valor = Column(Float, nullable=False)
   unidade_da_federacao_codigo = Column(String, nullable=False)
   unidade_da_federacao = Column(String, nullable=False)
   periodo = Column(DateTime(timezone=True), nullable=False)
   tipo_de_projeto = Column(String, nullable=False)
   padrao_de_acabamento = Column(String, nullable=False)
