# src/repository.py
from src.db.db_config import SessionLocal
from src.models.sinapi_model import SinapiModel

def save_sinapi_data(data_list):
   db = SessionLocal()
   try:
      for i,item in enumerate(data_list):
         db_item = SinapiModel(
               valor=item.valor,
               unidade_da_federacao_codigo=item.unidade_da_federacao_codigo,
               unidade_da_federacao=item.unidade_da_federacao,
               periodo=item.periodo,
               tipo_de_projeto=item.tipo_de_projeto,
               padrao_de_acabamento=item.padrao_de_acabamento
            )
         db.add(db_item)
      db.commit()
   except Exception as e:
      db.rollback()
      print(f"Erro ao salvar dados: {e}")
   finally:
      db.close()
