import json
import requests

class HttpSinapi:
   def __init__(self, url, nomeApi) -> None:
      self._url = url
      self._nomeApi = nomeApi

   @classmethod
   def from_json(cls, path):
      with open(path, 'r') as file:
         data = json.load(file)
      return cls(data['url'], data['nomeApi'])

   def __str__(self):
      return f'Url: {self._url} e o nome da url: {self._nomeApi}'

   def get_http_sinapi(self):
      try:
         response = requests.get(self._url)
         response.raise_for_status()
         print(f"Status code da api: {response.status_code}")
      except requests.exceptions.RequestException as e:
         print(f"Erro na requisição HTTP 'get': {e}")
      else:
         print(f"Baixando api: {self._nomeApi}")

obj = HttpSinapi.from_json('api.json')
obj.get_http_sinapi()
