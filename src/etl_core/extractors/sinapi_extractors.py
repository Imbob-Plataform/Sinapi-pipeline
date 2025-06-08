import json
from requests import request, exceptions

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

   def getHttpSinapi(self):
      pass


obj = HttpSinapi.from_json('api.json')
print(obj)
