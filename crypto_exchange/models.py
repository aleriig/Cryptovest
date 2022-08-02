import sqlite3

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