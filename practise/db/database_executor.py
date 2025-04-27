class DatabaseExecutor:

    def __init__(self, conn):
        self.conn = conn

    def fetch_results(query, conn):
        result = conn.execute(query)
        rows = result.fetchall()
        columns = result.keys()
        return [dict(zip(columns, row)) for row in rows]

    def insert_rows(query, conn):
        conn.execute(query)
        conn.commit()
