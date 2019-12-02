from multiprocessing.managers import BaseManager
import pandas as pd

def init_dataframe():
    return pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})

def get_df():
    return df

df = init_dataframe()
manager = BaseManager(('', 37844), b'password')
manager.register('get_df', get_df)
server = manager.get_server()
server.serve_forever()
