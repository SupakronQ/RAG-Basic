import psycopg2

class MyDbConnect:

    def __init__(self,conn_info):
        self.connection_info = conn_info
        self.connection = None
    
    def connect(self):
        self.connection = psycopg2.connect(**self.connection_info)

    def execute_query(self, query, param):
        try:
            
            cur = self.connection.cursor()
            cur.execute(query, param)

            if cur.description:
                result = cur.fetchall()
            else:
                result = None

            return result, None

        except Exception as err:
            return None, err
        
        finally:
            cur.close()

    def commit(self):
        self.connection.commit()
    
    def disconnect(self):
        self.connection.close()

    