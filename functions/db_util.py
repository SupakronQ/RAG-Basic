import psycopg2

class MyDbConnect:

    def __init__(self,conn_info):
        self.connection_info = conn_info
        self.connection = None
    
    def connect(self):
        self.connection = psycopg2.connect(**self.connection_info)

    def execute(self, query, params=None, fetch=True):
        cur = None
        try:
            cur = self.connection.cursor()

            # ตรวจสอบ param
            if params is not None and not isinstance(params, (tuple, list)):
                raise ValueError("params must be a tuple or list")

            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)

            if fetch and cur.description:
                result = cur.fetchall()
            else:
                result = cur.rowcount

            return result, None

        except Exception as err:
            self.connection.rollback()
            return None, err

        finally:
            if cur:
                cur.close()

    def executemany(self, query, param_list):
        cur = None
        try:
            cur = self.connection.cursor()
            cur.executemany(query, param_list)
            return cur.rowcount, None
        except Exception as err:
            self.connection.rollback()
            return None, err
        finally:
            if cur:
                cur.close()

    def commit(self):
        self.connection.commit()
    
    def disconnect(self):
        self.connection.close()

    