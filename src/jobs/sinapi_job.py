from src.extract.sinapi_extractors import HttpSinapi
from src.transform.sinapi_transform import TransformSinapi
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
      else:
         print(data_process)

if __name__ == '__main__':
   pipeline = PipelineSinapi()
   pipeline.run_pipeline()
