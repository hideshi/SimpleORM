from simpleorm import BaseDao
from collections import OrderedDict

class InsertEmployee(BaseDao):
    sql = 'INSERT INTO EMPLOYEE (ID, NAME, AGE, BOSS) VALUES (?, ?, ?, ?)'

if __name__ == '__main__':
    param = OrderedDict()
    param['id'] = 4
    param['name'] = 'Jiro Tanaka'
    param['age'] = 24
    param['boss'] = 3
    result = InsertEmployee(dbfile = 'test.db').execute(param)
    print('Rows affected:{}'.format(result))
