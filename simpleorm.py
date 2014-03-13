import sqlite3
import re
from collections import OrderedDict

class SimpleOrmException(Exception):
    pass

_ERROR_01 = "The SQL file {} for the class {} doesn't exist in the directory {} ."
_ERROR_02 = "The column name {} doesn't exist in the class {}."
__ISOLATION_LEVELS = ['DEFERRED', 'IMMEDIATE', 'EXLUSIVE']

class BaseDao(object):
    sql = ''
    def __init__(self, dbfile = None, conn = None, sql_file_dir = '.', return_type = None, isolation_level = None, commit_interval = -1):
        assert(dbfile != None or conn != None)
        assert(isolation_level == None or (isolation_level in __ISOLATION_LEVELS and commit_interval >= 1))
        self.dbfile = dbfile
        self.conn = conn
        self.return_type = return_type
        self.isolation_level = isolation_level
        self.commit_interval = commit_interval
        self.dao_class_name = '_'.join(filter(lambda x: x != '', re.split('([A-Z][a-z]+)', type(self).__name__))).lower()
        if self.sql == '':
            sql_file = '{}/{}.sql'.format(sql_file_dir, self.dao_class_name)
            try:
                with open(sql_file) as f:
                    self.sql = ' '.join([line.strip() for line in f])
            except FileNotFoundError as e:
                raise SimpleOrmException(_ERROR_01.format(sql_file, type(self).__name__, sql_file_dir)) from e

    def execute(self, param):
        assert(isinstance(param, OrderedDict) or isinstance(param, list))
        if self.conn == None:
            self.conn = sqlite3.connect(self.dbfile)
        with self.conn:
            self.conn.isolation_level = self.isolation_level
            if isinstance(param, list):
                cursor = self.conn.cursor()
                count = 0
                for elem in param:
                    cursor.execute(self.sql, tuple(elem[key] for key in elem))
                    count += 1
                    if count % commit_interval == 0:
                        self.conn.commit()
            else: 
                self.conn.row_factory = sqlite3.Row
                cursor = self.conn.cursor()
                cursor.execute(self.sql, tuple(param[key] for key in param))
                if self.conn.isolation_level != None:
                    self.conn.commit()
        if self.dao_class_name.startswith('select'):
            if self.return_type == None:
                return cursor.fetchall()
            else:
                result = []
                return_type_members = [m.lower() for m in dir(self.return_type)]
                for row in cursor.fetchall():
                    description = cursor.description
                    column_size = len(description)
                    obj = self.return_type()
                    for i in range(column_size):
                        column_name = description[i][0].lower()
                        value = row[i]
                        if not column_name in return_type_members:
                            raise SimpleOrmException(_ERROR_02.format(column_name, self.return_type.__name__))
                        else:
                            setattr(obj, column_name, value)
                    result.append(obj)
                return result
        else:
            return cursor.rowcount
