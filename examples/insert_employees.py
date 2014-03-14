from simpleorm import BaseDao
from collections import OrderedDict

class InsertEmployee(BaseDao):
    sql = 'INSERT INTO EMPLOYEE (ID, NAME, AGE, BOSS) VALUES (?, ?, ?, ?)'

if __name__ == '__main__':
    param = list()
    for i in range(10000):
        elem = OrderedDict()
        elem['id'] = i
        elem['name'] = '{}'.format(i)
        elem['age'] = i
        elem['boss'] = None
        param.append(elem)

    result = InsertEmployee(dbfile = 'test.db', commit_interval = 100, isolation_level = 'DEFERRED').execute(param)
    print('Rows affected:{}'.format(result))
