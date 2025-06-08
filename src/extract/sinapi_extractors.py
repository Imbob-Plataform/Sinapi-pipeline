import json
import requests

class HttpSinapi:
   def __init__(self, url, nomeApi) -> None:
      self._url = url
      self._nomeApi = nomeApi
      self._data = None

   @classmethod
   def from_json(cls, path):
      try:
         with open(path, 'r') as file:
            data = json.load(file)
      except FileNotFoundError:
         print("Arquivo Json não encontrado.")
         return None
      else:
         return cls(data['url'], data['nomeApi'])


   def __str__(self):
      return f'Url: {self._url} e o nome da url: {self._nomeApi}'

   def get_http_sinapi(self):
      try:
         response = requests.get(self._url)
         response.raise_for_status()
         self._data = response.json()
         return self._data
      except requests.exceptions.RequestException as e:
         print(f"Erro na requisição HTTP 'get': {e}")
         return None


obj = HttpSinapi.from_json('api.json')
print(obj.get_http_sinapi())
