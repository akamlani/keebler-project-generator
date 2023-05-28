import pandas as pd 
import re 

def convert_camelcase_to_snakecase(df:pd.DataFrame) -> pd.DataFrame:
    "convert camelcase to snakecase, e.g, for column transformation"
    def convert(col:str):
        column = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', col)
        column = re.sub('([a-z0-9])([A-Z])',  r'\1_\2', col).lower()
        return column.replace(" ", "_")
        
    df.columns =  map(convert, df.columns)
    return df 

def trsfrm_normalize_columns(df:pd.DataFrame, mapping:dict) -> pd.DataFrame:
    "rename columns from a provided dictionary input matching src:dest format"
    return df.rename(columns=mapping)
