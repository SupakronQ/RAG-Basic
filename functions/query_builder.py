
class QueryBuilder():

    @staticmethod
    def insert_data_query(table, data):

        # สร้าง SQL และ parameters
        keys = data[0].keys()
        col = ', '.join(keys)
        temp = ', '.join(['%s'] * len(keys)) 

        sql = f"""
            INSERT INTO {table} ({col}) VALUES ({temp})
        """
        values = [ tuple( d[i] for i in d) for d in data]
        return sql, values
    
    @staticmethod
    def vector_search():

        return f"""
            SELECT content, embedding <=> %s::vector as similarity_score
            FROM documents
            ORDER BY similarity_score ASC
            LIMIT %s;
        """