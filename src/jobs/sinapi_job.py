from src.extract.sinapi_extractors import HttpSinapi
from src.transform.sinapi_transform import TransformSinapi
from src.utils.df_to_pydantic import df_to_pydantic_list
from src.repository.sinapi_repository import save_sinapi_data
from src.db.init_db import init_db

import pandas as pd
class PipelineSinapi:
   def __init__(self) -> None:
      self.extract = HttpSinapi.from_json('api.json')
      if self.extract is None:
         raise ValueError("Falha ao carregar configuração do arquivo 'api.json'")

   def run_pipeline(self):
      data = self.extract.get_http_sinapi()  # type: ignore
      if not data or data is None:
         print("Falha ao obter dados da api")
         return

      data_process = TransformSinapi(data).transform()

      if data_process is None or data_process.empty:
         print('falha na transformação da api')
         return

      try:
         valid_data = df_to_pydantic_list(data_process)
         save_sinapi_data(valid_data)
      except Exception as e:
         raise ValueError("Não consegui validar os dados.")
      else:
         print('dados processados')

if __name__ == '__main__':
   init_db()   
   pipeline = PipelineSinapi()
   pipeline.run_pipeline()
