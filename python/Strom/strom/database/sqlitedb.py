""" sub-class of pandadb, utilizes sqlite3 """
import sqlite3 as sql
from pandadb import PandaDB

__version__='0.0.1'
__author__='Adrian Agnic'


class SqliteDB(PandaDB):

    def __init__(self, filename):
        self.db = str(filename)
        self.conn = None
        super().__init__(self.conn)

    def connect(self):
        self.conn = sql.connect(self.db)

    def close(self):
        super().close()

    def select(self, query=None, pars=None, table=None):
        return super().select(query, pars, table)

    def create(self, query, pars=None, df=None, table=None):
        super().create(query, pars, df, table)

    def update(self, query, pars=None, df=None, table=None):
        super().update(query, pars, df, table)

    def delete(self, query, pars):
        super().delete(query, pars)

    def table(self, df, table):
        super().table(df, table)
