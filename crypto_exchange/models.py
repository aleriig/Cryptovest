import requests
import sqlite3

from configuration import API_KEY

class DBManager:
    def __init__(self, route):
        self.route = route
    
    def query_SQL(self, query):
        connection = sqlite3.connect(self.route)
        cursor = connection.cursor()
        cursor.execute(query)
        
        self.movements = []
        column_names = []
        
        for column_description in cursor.description:
            column_names.append(column_description[0])
            
        database = cursor.fetchall()
        for data in database:
            movement = {}
            index = 0
            for name in column_names:
                movement[name] = data[index]
                index += 1
            self.movements.append(movement)
        
        connection.close()
        
        return self.movements
    
    
class APIError(Exception):
    pass
    
class Exchange:
    
    def __init__(self, currency_from, currency_to):
        self.currency_from = currency_from
        self.currency_to = currency_to
        self.exchange = 0.0
        
    def get_exchange(self):
        headers = {
            'X-CoinAPI-Key' : API_KEY
        }
        
        url = f"https://rest.coinapi.io/v1/exchangerate/{self.currency_from}/{self.currency_to}"
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            self.exchange = response.json()["rate"]
        else:
            raise APIError("An error ocurred {} {} while querying the API".format(response.status_code, response.reason))
            