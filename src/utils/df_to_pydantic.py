from src.schemas.sinapi_schema import SinapiSchema

def df_to_pydantic_list(df):
   records = df.to_dict(orient='records')
   pydantic_objs = [SinapiSchema(**record) for record in records]
   return pydantic_objs
