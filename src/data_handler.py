from multiprocessing.managers import BaseManager
import pandas as pd

def get_df():
    manager = BaseManager(('', 37844), b'password')
    manager.register('get_df')
    manager.connect()
    return manager.get_df()

def data():
    df = get_df()
    return df

if __name__ == '__main__':
    print(data())
