import pandas as pd

class TransformSinapi:
   def __init__(self, data) -> None:
      self._data = data
      self._df = None

   def transform(self):
      self.update_header_dataframe()
      self.update_columns_dataframe()
      self.remove_columns_dataframe()
      self.transform_column_valor()
      self.transform_column_unidade_federacao()
      self.transform_column_periodo()
      self.transform_column_tipo_projeto()
      self.transform_column_padrao_acabamento()
      return self._df


   def update_header_dataframe(self):
      dataframe = pd.DataFrame(self._data)
      dataframe.columns = dataframe.iloc[0]
      self._df = dataframe[1:].reset_index(drop=True)


   def update_columns_dataframe(self):
      rename_columns = {'Nível Territorial (Código)': 'nivel_territorial_codigo', 'Nível Territorial': 'nivel_territorial', 'Unidade de Medida (Código)':'unidade_de_medida_codigo','Unidade de Medida': 'unidade_de_medida', 'Valor': 'valor',
                  'Unidade da Federação (Código)': 'unidade_da_federacao_codigo', 'Unidade da Federação':'unidade_da_federacao', 'Variável (Código)': 'variavel_codigo', 'Variável': 'variavel','Mês (Código)': 'periodo',
                  'Mês': 'mes', 'Tipo de projeto (Código)': 'tipo_de_projeto_codigo', 'Tipo de projeto':'tipo_de_projeto', 'Padrão de acabamento (Código)': 'padrao_de_acabamento_codigo', 'Padrão de acabamento': 'padrao_de_acabamento'}
      self._df = self._df.rename(columns=rename_columns)

   def remove_columns_dataframe(self):
      colunas_a_remover = ['padrao_de_acabamento_codigo','tipo_de_projeto_codigo', 'nivel_territorial_codigo','nivel_territorial','unidade_de_medida_codigo', 'unidade_de_medida', 'variavel_codigo', 'variavel', 'mes']
      self._df = self._df.drop(columns=colunas_a_remover)

   def transform_column_valor(self):
      self._df['valor'] = self._df['valor'].replace('-', 0)
      self._df['valor'] = self._df['valor'].astype(float)

   def transform_column_unidade_federacao(self):
      self._df['unidade_da_federacao'] = self._df['unidade_da_federacao'].str.title()
      self._df['unidade_da_federacao'] = pd.Categorical(self._df['unidade_da_federacao'])

   def transform_column_periodo(self):
      self._df['periodo'] = self._df['periodo'].astype(str).str.zfill(6)
      self._df['ano'] = self._df['periodo'].str[:4]
      self._df['mes'] = self._df['periodo'].str[4:6]
      self._df['periodo'] = '01/' + self._df['mes'] + '/'+ self._df['ano']
      self._df = self._df.drop(columns=['ano', 'mes'])
      self._df['periodo'] = pd.to_datetime(self._df['periodo'], dayfirst=True, utc=True)

   def transform_column_tipo_projeto(self):
      self._df['tipo_de_projeto'] = self._df['tipo_de_projeto'].astype(str)
      self._df['tipo_de_projeto'] = self._df['tipo_de_projeto'].str[14:]
      self._df['tipo_de_projeto'] = pd.Categorical(self._df['tipo_de_projeto'])

   def transform_column_padrao_acabamento(self):
      self._df['padrao_de_acabamento'] = pd.Categorical(self._df['padrao_de_acabamento'])

