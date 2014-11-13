class SQLWrapper:

    def __init__(self):
        self.con = sqlite3.connect()
        self.cursor = self.con.cursor

    def select(self, table, columns):
        statement = "SELECT %s FROM &s" % (" ,".join(columns), table)
        self.cursor.execute(statement)
        return self.cursor.fetchall()

    def update(self, table, data, column, value):
        str_data = ""
        for key in data:
            str_data += "%s = %s, " % (key, data[key])
        statement = "UPDATE %s SET %s WHERE %s = %s" % (table, str_data, column, value)
        self.cursor.exectue(statement)
        self.cursor.commit()
        

    def delete(self, table, column, value):
        statement = "DELETE FROM %s WHERE %s = %s" % (table, columm, value)
        self.cursor.execute(statement)
        self.cursor.commit()

    def insert(self, table, columns, data):

    def create(self, table):
