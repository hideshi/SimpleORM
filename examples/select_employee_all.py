from simpleorm import BaseDao
from classes import Employee
from collections import OrderedDict

class SelectEmployeeAll(BaseDao):
    sql = '''
SELECT A.ID
      ,A.NAME
      ,B.NAME AS BOSS_NAME
  FROM EMPLOYEE A
  LEFT OUTER JOIN EMPLOYEE B
    ON B.ID = A.BOSS
'''

if __name__ == '__main__':
    param = OrderedDict()
    result = SelectEmployeeAll(dbfile = 'test.db', return_type = Employee).execute(param)
    for elem in result:
        print(elem.id, elem.name, elem.boss_name)
